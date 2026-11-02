using System.IO;
using File = System.IO.File;
using Path = System.IO.Path;
using Directory = System.IO.Directory;
// Renders engine builds on the garage's engine stand with the game's own renderer, offscreen.
//   StandShot <out dir> <mod id> [build-id-substring ...]
// Content: <exe dir>\Content (a junction to the game's).
using System.Reflection;
using AcTools.Render.Base;
using AcTools.Render.Kn5SpecificForwardDark.Lights;
using SlimDX;
using StreetCorsa.Configuration;
using StreetCorsa.Controls;
using StreetCorsa.Logging;
using StreetCorsa.Mods;
using StreetCorsa.Parts;
using StreetCorsa.Parts.Cars;

static class Program
{
    static readonly Assembly Game = typeof(GarageRenderer).Assembly;

    static object? CallStatic(string type, string method, params object?[] args)
    {
        var t = Game.GetType(type, true)!;
        var m = t.GetMethods(BindingFlags.Static | BindingFlags.Public | BindingFlags.NonPublic).First(x => x.Name == method && x.GetParameters().Length == args.Length);
        return m.Invoke(null, args);
    }

    [STAThread]
    static int Main(string[] args)
    {
        var outDir = Path.GetFullPath(args[0]);
        var modId = args[1];
        var filters = args.Skip(2).ToArray();
        var width = int.Parse(Environment.GetEnvironmentVariable("SHOT_W") ?? "1600");
        var height = int.Parse(Environment.GetEnvironmentVariable("SHOT_H") ?? "900");
        Directory.CreateDirectory(outDir);

        var en = System.Globalization.CultureInfo.GetCultureInfo("en-US");
        System.Globalization.CultureInfo.DefaultThreadCurrentCulture = en;
        System.Globalization.CultureInfo.CurrentCulture = en;
        AppLoggerFactory.Initialize();
        var mods = ModSet.PlayedIn("streetrod");
        ModSet.Play(mods);
        Console.WriteLine($"Mods: {string.Join(", ", mods.Mods.Select(m => m.Id))}");

        var catalog = PartsCatalog.Load(mods.ContentOf(ContentTypes.Parts).ToList(), mods);
        var index = EngineBuildIndex.Create(catalog);
        var builds = index.Runnable.Where(b => b.Build.Id.StartsWith(modId + "/", StringComparison.OrdinalIgnoreCase) || OwnedBy(catalog, b, modId)).ToList();
        if (filters.Length > 0) builds = builds.Where(b => filters.Any(f => b.Build.Id.Contains(f, StringComparison.OrdinalIgnoreCase))).ToList();
        Console.WriteLine($"{builds.Count} builds");
        foreach (var f in index.Faults.Take(5)) Console.WriteLine($"  fault: {f}");

        var showroom = AppSettings.Instance.GarageKn5Of(mods);
        Console.WriteLine($"Garage: {showroom}");
        var problems = new List<string>();
        var stand = StreetCorsa.Services.Garage.GarageProps.Find(mods, EngineStandLayout.PropId, showroom, problems, builtIn: true);
        EngineStandLayout.PlaceAt(stand?.Position, stand?.Model);
        Console.WriteLine($"Stand at {EngineStandLayout.Spot}, model {EngineStandLayout.Model ?? "(boxes)"}");

        using var renderer = new GarageRenderer(null, showroom)
        {
            UseMsaa = true, VisibleUi = false, AutoRotate = false, UseFxaa = true, UseSslr = true, UseAo = true,
            UseBloom = true, EnableShadows = true, UsePcss = true, Width = width, Height = height
        };
        renderer.Initialize();
        renderer.AutoAdjustTarget = false;

        // The room's lights, as the garage screen has them by day
        var garageId = Path.GetFileName(Path.GetDirectoryName(showroom))!;
        var room = StreetCorsa.Services.Garage.GarageRooms.Load(mods, garageId);
        var light = Enum.Parse<StreetCorsa.Services.Street.StreetLight>(Environment.GetEnvironmentVariable("SHOT_LIGHT") ?? "Day");
        if (room.IsLit)
        {
            var dressing = room.Dress(light);
            var lot = new LotDressing(dressing.Lighting, dressing.Sun, new Dictionary<string, string>(), dressing.Glow);
            CallStatic("StreetCorsa.Controls.SceneDressing", "Apply", renderer, lot, new List<DarkLightBase>(), AppLoggerFactory.CreateLogger("Shot"));
            CallStatic("StreetCorsa.Controls.SceneDressing", "ShowSky", renderer, StreetCorsa.Services.Garage.GarageRoom.SkyPrefix, dressing.Sky);
        }

        // The garage's props (shelves, benches...), as the screen dresses it
        var own = new[] { "radio", "workbench", "lift", EngineStandLayout.PropId };
        var props = StreetCorsa.Services.Garage.GarageProps.FindAll(mods, showroom, own, problems);
        var models = props.Select(p => p.Model).Distinct(StringComparer.OrdinalIgnoreCase).ToDictionary(m => m, m => AcTools.Kn5File.Kn5.FromFile(m), StringComparer.OrdinalIgnoreCase);
        var placement = typeof(CarViewport3D).GetMethod("DressingPlacement", BindingFlags.Static | BindingFlags.NonPublic)!;
        renderer.SetDressing(props.Select(p => (models[p.Model], ToSlim((System.Numerics.Matrix4x4)placement.Invoke(null, [p, models[p.Model]])!))));
        foreach (var p in problems) Console.WriteLine($"  props: {p}");

        var views = new (string Name, float Alpha, float Beta, float Radius)[]
        {
            ("front", 0.95f, 0.30f, 2.25f),
            ("side", 2.3f, 0.26f, 2.25f),
            ("rear", -0.8f, 0.34f, 2.45f),
            ("top", 1.6f, 0.85f, 2.0f),
        };

        foreach (var build in builds)
        {
            var built = EngineFactory.CreateStock(catalog, build, 1.0, new Random(1));
            if (built == null || PartTrees.ToInstalled(catalog, built.Root) is not { } live) { Console.WriteLine($"  skip {build.Build.Id}"); continue; }
            var engine = live.Root;

            var parts = EngineStandLayout.Build(catalog, engine);
            if (Environment.GetEnvironmentVariable("SHOT_RADIATOR") != "1")
                parts = parts.Where(p => !p.Part.Id.Contains("radiator", StringComparison.OrdinalIgnoreCase)).ToList();
            var model = PartAssembler.BuildModel(catalog, "stand", parts);
            EngineStandLayout.AddTo(model.Kn5, EngineStandLayout.HeadZ(catalog, engine));
            renderer.StandActive = true;
            renderer.GhostCar = false;
            renderer.SetProp(model.Kn5, Matrix.Identity);
            renderer.SettleEngineTurn();

            var spot = EngineStandLayout.Spot;
            var orbit = renderer.CameraOrbit;
            orbit.Target = new Vector3(spot.X, EngineStandLayout.Spindle.Y - 0.05f, spot.Z - 0.1f) + new Vector3(0f, 0.14f, 0f);
            var name = build.Build.Id.Split('/').Last();
            foreach (var v in views)
            {
                orbit.Alpha = v.Alpha; orbit.Beta = v.Beta; orbit.Radius = v.Radius;
                renderer.RefreshShadows();
                for (var i = 0; i < 8; i++) renderer.Draw();
                var file = Path.Combine(outDir, $"{name}_{v.Name}.png");
                using (var stream = File.Create(file))
                    renderer.Shot(width, height, 1d, 1d, stream, RendererShotFormat.Png, null, CancellationToken.None);
                Console.WriteLine($"  {file}");
            }
        }

        return 0;
    }

    static bool OwnedBy(PartsCatalog catalog, RatedBuild build, string modId) =>
        catalog.Parts.TryGetValue(build.BlockId, out var block) && string.Equals(block.ModId, modId, StringComparison.OrdinalIgnoreCase);

    static Matrix ToSlim(System.Numerics.Matrix4x4 m) => new()
    {
        M11 = m.M11, M12 = m.M12, M13 = m.M13, M14 = m.M14, M21 = m.M21, M22 = m.M22, M23 = m.M23, M24 = m.M24,
        M31 = m.M31, M32 = m.M32, M33 = m.M33, M34 = m.M34, M41 = m.M41, M42 = m.M42, M43 = m.M43, M44 = m.M44
    };
}
