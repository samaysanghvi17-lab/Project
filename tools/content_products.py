# -*- coding: utf-8 -*-
"""Product page content for Neo Impex (buttweld fittings and flanges).

Facts come from the supplied Neo Impex landing-page document (sizes, standards,
materials, approvals) plus widely published standard definitions. Anything
numeric that is not in the company document is kept to well-known standard values.
"""

FIT_MATS = ("SS 304/304L, 316/316L, duplex 2205, super duplex 2507, A234 WPB, "
            "A420 WPL6, chrome-moly alloy steel and nickel alloys")
FL_MATS = ("SS 304/304L, 316/316L, duplex F51/F60, super duplex F53/F55, A105, "
           "A350 LF2, chrome-moly alloy steel and nickel alloys")

FIT_COMMON = [
    ("Size range", "Seamless up to 24″ · welded up to 72″ (NPS)"),
    ("End preparation", "Beveled for butt welding (ASME B16.25)"),
    ("Materials", FIT_MATS),
    ("Marking and documents", "MSS SP-25 marking · heat traceable · EN 10204 3.1 certificate"),
]

FL_COMMON = [
    ("Size range", "½″ to 60″"),
    ("Pressure class", "Class 150 to 2500 (size dependent) · PN6 to PN100"),
    ("Facings", "Raised face, ring type joint, flat face, tongue and groove, male and female"),
    ("Materials", FL_MATS),
    ("Marking and documents", "Heat number traceable · EN 10204 3.1 certificate"),
]

FITTINGS = {
 "elbows": dict(
  name="Buttweld Elbows", short="45°, 90° and 180° · long and short radius",
  h1="Buttweld Elbows: 45°, 90° and 180°",
  title="Buttweld Elbows Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.9 buttweld elbows in 45°, 90° and 180°, long and short radius. Stainless, duplex, carbon, alloy, nickel. Seamless to 24″, welded to 72″.",
  kw=("buttweld elbow manufacturer", ["ASME B16.9 elbow supplier", "90 degree long radius elbow", "stainless steel butt weld elbow USA", "short radius elbow B16.28"]),
  chips=["ASME B16.9 · B16.28", "Seamless to 24″", "Welded to 72″"],
  intro=[
   "A buttweld elbow changes the direction of a pipeline by 45°, 90° or 180° while keeping the bore and wall of the pipe it joins. Neo Impex makes long-radius elbows (centerline radius of 1.5 × nominal pipe size) and short-radius elbows (1 × nominal pipe size) in stainless steel, duplex, carbon, alloy and nickel alloys.",
   "Elbows are seamless up to 24″ and welded up to 72″, with 100% radiography on welded seams. Each piece is marked with grade, size, schedule and heat number and ships with an EN 10204 3.1 certificate, so your inspector can trace it to the mill test."],
  spec=[("Standards", "ASME B16.9 (long radius) · ASME B16.28 (short radius) · MSS SP-43 (light-wall stainless) · EN 10253"),
        ("Angles", "45°, 90°, 180°"), ("Radius", "Long radius 1.5D · short radius 1.0D"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Smooth full-radius forming for low pressure drop", "Dimensions to ASME B16.9 for direct fit-up", "Weld-ready bevels to ASME B16.25", "Heat-traceable and marked to MSS SP-25", "Welded large-diameter elbows up to 72″"],
  apps=["Refinery and chemical process piping", "Power and steam lines", "Water and wastewater systems", "Pharma and food-grade stainless lines", "Pipe spools built by fabricators"],
  faqs=[("What is the difference between long radius and short radius elbows?",
         "A long-radius elbow has a centerline radius of 1.5 times the nominal pipe size and gives smoother flow and lower pressure drop. A short-radius elbow (ASME B16.28) has a radius equal to the nominal size and is used where space is tight. Long radius is the default unless your drawing says otherwise."),
        ("Do you supply both seamless and welded elbows?",
         "Yes. Elbows are seamless up to 24″ and welded from plate up to 72″. Welded seams are 100% radiographed."),
        ("Which certificates ship with elbows?",
         "EN 10204 3.1 mill test certificates with heat numbers. Extra tests and third-party inspection can be agreed in your purchase order.")],
  related=["tees", "reducers", "pipe-bends"], art="elbow", photo=None),

 "tees": dict(
  name="Buttweld Tees", short="Equal and reducing tees for branch lines",
  h1="Buttweld Tees: Equal and Reducing",
  title="Buttweld Tees Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.9 equal and reducing buttweld tees in stainless, duplex, carbon, alloy and nickel alloys. Seamless to 24″, welded to 72″. Export to USA and Canada.",
  kw=("buttweld tee manufacturer", ["ASME B16.9 tee supplier", "reducing tee butt weld", "stainless steel butt weld tee", "equal tee pipe fitting"]),
  chips=["ASME B16.9", "Equal and reducing", "Welded to 72″"],
  intro=[
   "A buttweld tee creates a 90° branch off a main run. Equal tees have the same size on all three ends; reducing tees have a smaller branch outlet. Neo Impex makes tees to ASME B16.9 in stainless, duplex, carbon, alloy and nickel alloys.",
   "Seamless tees are hot-formed from pipe up to 24″. Larger tees are fabricated from plate up to 72″ and radiographed along the weld. Every tee carries heat-number marking and an EN 10204 3.1 certificate."],
  spec=[("Standards", "ASME B16.9 · MSS SP-43 · EN 10253"), ("Types", "Equal (straight) tee · reducing tee"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Equal and reducing outlets", "Hot-formed seamless tees up to 24″", "Plate-fabricated tees up to 72″ with radiography", "Dimensions to ASME B16.9", "Heat-traceable marking"],
  apps=["Branch connections on process lines", "Pipeline headers and manifolds", "Water and wastewater distribution", "Fabricated pipe spools and skids"],
  faqs=[("What is a reducing tee?", "A tee whose branch is smaller than the run, for example 8″ × 8″ × 4″. Sizes are quoted run × run × branch."),
        ("How are large-diameter tees made?", "Above 24″ they are fabricated from plate and welded. Welds are 100% radiographed."),
        ("How do I specify a tee?", "Give nominal size (run × branch), schedule or wall on each end, material grade and standard, for example: 8″ × 4″ SCH 40S, ASTM A403 WP316L, ASME B16.9.")],
  related=["reducers", "crosses", "elbows"], art="tee", photo="tees.jpg"),

 "reducers": dict(
  name="Buttweld Reducers", short="Concentric and eccentric reducers",
  h1="Buttweld Reducers: Concentric and Eccentric",
  title="Buttweld Reducers Manufacturer & Exporter | USA, Canada",
  desc="Concentric and eccentric ASME B16.9 buttweld reducers in stainless, duplex, carbon, alloy and nickel. Seamless to 24″, welded to 72″. Export to USA, Canada.",
  kw=("buttweld reducer manufacturer", ["concentric reducer ASME B16.9", "eccentric reducer supplier", "stainless steel butt weld reducer", "pipe reducer exporter India"]),
  chips=["ASME B16.9", "Concentric", "Eccentric"],
  intro=[
   "A buttweld reducer joins two pipes of different sizes. A concentric reducer keeps both ends on the same centerline; an eccentric reducer keeps one side flat so the pipe can stay level on top or bottom.",
   "Neo Impex makes reducers to ASME B16.9 in stainless, duplex, carbon, alloy and nickel alloys. Seamless reducers are formed from pipe up to 24″; larger sizes are fabricated from plate up to 72″."],
  spec=[("Standards", "ASME B16.9 · MSS SP-43 · EN 10253"), ("Types", "Concentric · eccentric"),
        ("Wall thickness", "Sch 5S to XXS, or to match each pipe end")] + FIT_COMMON,
  features=["Concentric and eccentric patterns", "Wall thickness matched to each pipe end", "Dimensions to ASME B16.9", "Marked with grade, size, schedule and heat number"],
  apps=["Pump suction and discharge lines", "Pipe racks and headers", "Process skids", "Changes in line size on water and gas systems"],
  faqs=[("When should I use an eccentric reducer?", "Use an eccentric reducer when the pipe must keep a flat top or bottom: flat-on-top on pump suction lines to avoid trapped air, flat-on-bottom on pipe racks to keep the underside level. Concentric reducers suit vertical lines and symmetric changes."),
        ("How is a reducer specified?", "Larger end × smaller end, schedule on each end, material and standard, for example: 10″ × 6″ SCH 40, ASTM A234 WPB, eccentric, ASME B16.9.")],
  related=["tees", "elbows", "caps"], art="reducer", photo=None),

 "caps": dict(
  name="Buttweld Pipe End Caps", short="Close the end of a pipe permanently",
  h1="Buttweld Pipe End Caps",
  title="Buttweld End Caps Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.9 buttweld pipe end caps in stainless, duplex, carbon, alloy and nickel alloys. Seamless to 24″, welded to 72″. Export to USA and Canada.",
  kw=("buttweld end cap manufacturer", ["pipe end cap ASME B16.9", "stainless steel butt weld cap", "welded pipe cap supplier"]),
  chips=["ASME B16.9", "Seamless to 24″", "Welded to 72″"],
  intro=[
   "A buttweld cap closes the end of a pipe permanently. It is welded on, has a domed (ellipsoidal) head, and is designed to carry the same pressure as the pipe it closes.",
   "Neo Impex makes caps in stainless, duplex, carbon, alloy and nickel alloys, seamless up to 24″ and welded up to 72″, with heat-traceable marking and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.9 · MSS SP-43 · EN 10253"), ("Head form", "Ellipsoidal (domed)"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Domed head for strength and smooth stress distribution", "Same wall as the pipe for equal pressure rating", "Dimensions to ASME B16.9", "Heat-traceable marking"],
  apps=["Line ends and future tie-ins", "Pressure vessel and tank nozzles", "Pipe spools and headers", "Pigging and test headers"],
  faqs=[("Should I use a cap or a blind flange?", "A cap is welded on and is permanent. A blind flange is bolted so the line can be reopened. Use a cap for a final end and a blind flange where you may need access."),
        ("Can caps be supplied in large sizes?", "Yes. Caps are seamless up to 24″ and welded from plate up to 72″.")],
  related=["reducers", "stub-ends", "elbows"], art="cap", photo=None),

 "stub-ends": dict(
  name="Stub Ends", short="Long and short pattern, for lap joint flanges",
  h1="Stub Ends: Long and Short Pattern",
  title="Stub Ends Manufacturer & Exporter | USA, Canada",
  desc="Long and short pattern buttweld stub ends to ASME B16.9 and MSS SP-43 in stainless, duplex, carbon, alloy and nickel alloys. Export to USA and Canada.",
  kw=("stub end manufacturer", ["lap joint stub end ASME B16.9", "MSS SP-43 stub end", "stainless steel stub end supplier"]),
  chips=["ASME B16.9", "MSS SP-43", "Long and short"],
  intro=[
   "A stub end is the welded half of a lap joint: it is butt-welded to the pipe and a loose lap joint flange rotates behind its lip. This makes bolt-hole alignment easy and lets you use a cheaper flange material with a corrosion-resistant stub end.",
   "Neo Impex makes stub ends in long and short patterns, in stainless, duplex, carbon, alloy and nickel alloys, with heat-traceable marking and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.9 (long pattern) · MSS SP-43 (short pattern) · EN 10253"), ("Patterns", "Long and short"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Long and short patterns", "Pairs with lap joint flanges", "Lets the flange be a lower-cost material", "Heat-traceable marking"],
  apps=["Lines that are dismantled often", "Stainless lines with carbon-steel lap joint flanges", "Systems that need easy bolt-hole alignment"],
  faqs=[("What is the difference between short and long pattern stub ends?", "The long pattern (ASME B16.9) has a longer barrel, so it can be re-cut and re-welded several times. The short pattern (MSS SP-43) is shorter and lighter. Choose according to your line specification."),
        ("What do I pair a stub end with?", "A lap joint flange of the same size and class. See our lap joint flange page for details.")],
  related=["elbows", "caps", "tees"], art="stub", photo=None),

 "crosses": dict(
  name="Buttweld Crosses", short="Four-way branch connections",
  h1="Buttweld Crosses",
  title="Buttweld Crosses Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.9 straight and reducing buttweld crosses in stainless, duplex, carbon, alloy and nickel alloys. Seamless to 24″, welded to 72″. Export to USA and Canada.",
  kw=("buttweld cross manufacturer", ["ASME B16.9 cross", "stainless steel butt weld cross", "four way pipe fitting"]),
  chips=["ASME B16.9", "Straight and reducing"],
  intro=[
   "A buttweld cross joins four pipes at a single point: a run with a branch on each side. Neo Impex makes straight and reducing crosses to ASME B16.9 in stainless, duplex, carbon, alloy and nickel alloys.",
   "Crosses concentrate stress at the intersection, so many designers use two offset tees instead. Where a cross is specified, we supply it with heat-traceable marking and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.9 · EN 10253"), ("Types", "Straight cross · reducing cross"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Straight and reducing patterns", "Dimensions to ASME B16.9", "Heat-traceable marking"],
  apps=["Manifolds and headers", "Compact piping layouts", "Process skids"],
  faqs=[("Why are crosses used less than tees?", "A cross has more stress concentration at the junction than a tee. Many piping specifications limit or avoid them, so check your code and line class before ordering.")],
  related=["tees", "elbows", "reducers"], art="cross", photo=None),

 "return-bends": dict(
  name="180° Return Bends", short="U-turns for heaters and coils",
  h1="180° Return Bends",
  title="180° Return Bends Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.9 and B16.28 180° long and short radius return bends in stainless, duplex, carbon, alloy and nickel alloys. Export to USA and Canada.",
  kw=("180 degree return bend manufacturer", ["ASME B16.9 return bend", "long radius return bend", "stainless steel U bend fitting"]),
  chips=["ASME B16.9 · B16.28", "Long and short radius"],
  intro=[
   "A 180° return bend turns a line back on itself, a U-turn with two welded ends. Long-radius returns have a centerline-to-centerline distance of three times the nominal size; short-radius returns (ASME B16.28) use two times.",
   "Neo Impex supplies return bends in stainless, duplex, carbon, alloy and nickel alloys, with heat-traceable marking and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.9 (long radius) · ASME B16.28 (short radius)"),
        ("Centerline spacing", "Long radius 3 × NPS · short radius 2 × NPS"),
        ("Wall thickness", "Sch 5S to XXS, or to match your pipe")] + FIT_COMMON,
  features=["Long and short radius", "Compact U-turn layouts", "Heat-traceable marking"],
  apps=["Heater and furnace coils", "Heat exchangers", "Cooling and heating loops"],
  faqs=[("Can I get a return bend with a custom radius?", "Yes. Send your drawing; custom-radius bends are made in our bending shop.")],
  related=["elbows", "pipe-bends", "tees"], art="return", photo=None),

 "pipe-bends": dict(
  name="Pipe Bends: 3D, 5D, 10D and Piggable", short="3D / 5D / 10D, induction and piggable bends",
  h1="Pipe Bends: 3D, 5D, 10D, Induction and Piggable",
  title="Pipe Bends 3D 5D 10D & Piggable Bends | Exporter",
  desc="3D, 5D and 10D pipe bends, induction bends and piggable bends to R = 22D, up to 24″. Made in our own bending shop. Export to USA and Canada.",
  kw=("pipe bend manufacturer", ["induction bend supplier", "piggable bend 5D 10D", "3D 5D pipe bend", "ASME B16.49 induction bend"]),
  chips=["3D · 5D · 10D", "Up to 24″", "Piggable to R = 22D"],
  intro=[
   "A pipe bend gives a gentler change of direction than a standard elbow. The radius is quoted as a multiple of the pipe diameter: a 5D bend has a centerline radius of five times the nominal diameter. Larger radii mean lower pressure drop and easier passage for in-line inspection tools.",
   "Neo Impex makes 3D, 5D and 10D bends, induction (hot) bends and piggable bends up to 24″ and radii to R = 22D in our own bending shop. Bends ship with heat-traceable marking and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.49 (induction bends) · ASME B31.4 / B31.8 for pipelines · customer specification"),
        ("Radius", "3D, 5D, 10D and to R = 22D"), ("Size range", "Up to 24″ (NPS)"),
        ("Bending method", "Induction (hot) bending and cold bending, per material and size"),
        ("Materials", "Stainless, duplex, carbon and alloy steel pipe to your specification"),
        ("Marking and documents", "Heat traceable · EN 10204 3.1 certificate")],
  features=["Long radii for low pressure drop", "Piggable bends for pipeline inspection tools", "Made in our own bending shop", "Custom angles and tangents to your drawing"],
  apps=["Oil, gas and product pipelines", "Pipeline launchers and receivers", "Compact process lines needing gentle bends", "Heat exchanger and heater piping"],
  faqs=[("What does 5D mean?", "The centerline bend radius equals five times the nominal pipe diameter. A 3D bend is tighter, a 10D bend is gentler."),
        ("What is a piggable bend?", "A bend with a radius large enough for in-line inspection and cleaning tools (pigs) to pass. We make piggable bends up to 24″ and to R = 22D."),
        ("Can you bend to my drawing?", "Yes. Send the drawing with angle, radius, tangents, material and standard, and we will quote.")],
  related=["elbows", "return-bends", "tees"], art="bend", photo=None),
}

FITTINGS_ORDER = ["elbows", "tees", "reducers", "caps", "stub-ends", "crosses", "return-bends", "pipe-bends"]

FLANGES = {
 "weld-neck": dict(
  name="Weld Neck Flanges", short="WNRF and RTJ for high-pressure and critical service",
  h1="Weld Neck Flanges (WNRF, RTJ)",
  title="Weld Neck Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 and B16.47 weld neck flanges, raised face and RTJ, ½″ to 60″, Class 150 to 2500. Stainless, duplex, carbon, alloy, nickel. Export to USA and Canada.",
  kw=("weld neck flange manufacturer", ["ASME B16.5 weld neck flange", "WNRF flange supplier", "A105 weld neck flange", "stainless steel weld neck flange USA"]),
  chips=["ASME B16.5 · B16.47", "½″ to 60″", "Class 150–2500"],
  intro=[
   "A weld neck flange has a long tapered hub that is butt-welded to the pipe. The hub carries stress smoothly from the pipe into the flange, so weld neck flanges are the usual choice for high pressure, high temperature, cyclic and critical service.",
   "Neo Impex forges weld neck flanges from ½″ to 60″ in Class 150 to 2500 (size dependent), with raised face, ring type joint and other facings. The bore is machined to match your pipe schedule."],
  spec=[("Standards", "ASME B16.5 (NPS ½–24) · ASME B16.47 (NPS 26–60) · EN 1092-1 · BS 4504 · BS 10 · DIN"),
        ("Bore", "Machined to match pipe schedule")] + FL_COMMON,
  features=["Hub transfers stress smoothly into the pipe", "Suits high-pressure and cyclic service", "Bore matched to pipe schedule for smooth flow", "Radiography-friendly butt weld joint"],
  apps=["Refinery and petrochemical piping", "Oil and gas pipelines", "Power plant steam lines", "High-pressure chemical service"],
  faqs=[("What does WNRF mean?", "Weld neck, raised face. WNRTJ means weld neck with a ring type joint facing."),
        ("Why must the bore match the pipe?", "A step between the flange bore and the pipe bore disturbs flow and can cause erosion. Specify the pipe schedule so we machine the bore to match."),
        ("Weld neck or slip-on?", "Choose weld neck for high pressure, temperature swings or critical lines. Slip-on is lower cost for moderate service. Our blog compares them in detail.")],
  related=["slip-on", "long-weld-neck", "ring-type-joint"], art="weldneck", photo="weld-neck.jpg"),

 "slip-on": dict(
  name="Slip-On Flanges", short="SORF for low-pressure lines where cost and fit-up matter",
  h1="Slip-On Flanges (SORF)",
  title="Slip-On Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 slip-on raised face flanges, ½″ to 24″, in stainless, duplex, carbon, alloy and nickel alloys. Forged in India. Export to USA and Canada.",
  kw=("slip on flange manufacturer", ["SORF flange supplier", "ASME B16.5 slip-on flange", "stainless steel slip on flange", "A105 slip on flange"]),
  chips=["ASME B16.5", "SORF", "Class 150–600"],
  intro=[
   "A slip-on flange slides over the pipe and is welded inside and outside with two fillet welds. It costs less than a weld neck flange and is easier to align, which makes it popular for low-pressure, non-critical lines.",
   "Neo Impex forges slip-on flanges to ASME B16.5 in stainless, duplex, carbon, alloy and nickel alloys, with raised face and other facings, supplied with heat-number traceability and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.5 · EN 1092-1 · BS 4504 · BS 10 · DIN"),
        ("Welds", "Two fillet welds (inside and outside)")] + FL_COMMON,
  features=["Lower cost than weld neck", "Easy alignment and fit-up", "Raised face and other facings", "Heat-number traceability"],
  apps=["Water and utility lines", "Low-pressure process piping", "Fire protection and cooling water", "Non-critical chemical lines"],
  faqs=[("What does SORF mean?", "Slip-on, raised face."),
        ("When is a slip-on flange not suitable?", "Avoid slip-on flanges for severe cyclic loading or high pressure and temperature, where a weld neck flange has better fatigue performance. Your piping code and line class decide.")],
  related=["weld-neck", "blind", "lap-joint"], art="slipon", photo="slip-on.jpg"),

 "blind": dict(
  name="Blind Flanges", short="Close pipe ends, valves and vessel nozzles",
  h1="Blind Flanges",
  title="Blind Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 and B16.47 blind flanges, ½″ to 60″, Class 150 to 2500. Stainless, duplex, carbon, alloy and nickel alloys. Export to USA and Canada.",
  kw=("blind flange manufacturer", ["ASME B16.5 blind flange", "A105 blind flange supplier", "stainless steel blind flange", "large diameter blind flange"]),
  chips=["ASME B16.5 · B16.47", "½″ to 60″", "Class 150–2500"],
  intro=[
   "A blind flange is a solid disc with bolt holes and no bore. It closes the end of a pipe, a valve or a vessel nozzle, and can be unbolted when you need access.",
   "Neo Impex forges blind flanges from ½″ to 60″ in Class 150 to 2500 (size dependent), in stainless, duplex, carbon, alloy and nickel alloys, with raised face, ring type joint and other facings."],
  spec=[("Standards", "ASME B16.5 (NPS ½–24) · ASME B16.47 (NPS 26–60) · EN 1092-1 · BS 4504 · BS 10 · DIN")] + FL_COMMON,
  features=["Solid forged disc, no bore", "Sizes to 60″ for large vessels", "Raised face, RTJ and other facings", "Heat-number traceability"],
  apps=["Line ends and future tie-ins", "Vessel and tank manways and nozzles", "Pressure test closures", "Valve and equipment isolation"],
  faqs=[("What is a spectacle blind?", "A figure-eight plate with one solid and one open disc, used for positive isolation (ASME B16.48). Send us your specification for a quote."),
        ("Blind flange or cap?", "A blind flange can be reopened; a buttweld cap is welded on permanently.")],
  related=["weld-neck", "slip-on", "ring-type-joint"], art="blind", photo="blind.jpg"),

 "socket-weld": dict(
  name="Socket Weld Flanges", short="Small-bore, high-pressure lines",
  h1="Socket Weld Flanges (SWRF)",
  title="Socket Weld Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 socket weld raised face flanges for small-bore, high-pressure lines in stainless, duplex, carbon, alloy and nickel alloys. Export to USA and Canada.",
  kw=("socket weld flange manufacturer", ["SWRF flange supplier", "ASME B16.5 socket weld flange", "stainless steel socket weld flange"]),
  chips=["ASME B16.5", "SWRF", "Small bore"],
  intro=[
   "A socket weld flange has a recess (socket) into which the pipe is inserted and fillet-welded. It is used on small-bore, high-pressure lines, where its smooth bore and easy fit-up are an advantage.",
   "Neo Impex forges socket weld flanges to ASME B16.5 in stainless, duplex, carbon, alloy and nickel alloys, with heat-number traceability and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.5 · EN 1092-1 · BS 4504"), ("Typical sizes", "Small bore (typically up to NPS 3)")] + FL_COMMON,
  features=["Suits small-bore, high-pressure lines", "Simple fit-up with a single fillet weld", "Smooth bore", "Heat-number traceability"],
  apps=["Instrument and sampling lines", "Hydraulic and lube oil systems", "High-pressure small-bore process piping"],
  faqs=[("Why is there a gap when welding a socket weld flange?", "The pipe is inserted to the bottom of the socket and then pulled back about 1.6 mm (1/16″) before welding, to allow for thermal expansion during welding."),
        ("What size range is typical?", "Socket weld flanges are used on small bore, typically up to NPS 3. Larger sizes use weld neck or slip-on flanges.")],
  related=["threaded", "weld-neck", "slip-on"], art="socket", photo=None),

 "threaded": dict(
  name="Threaded Flanges", short="NPT screwed flanges where welding isn’t allowed",
  h1="Threaded Flanges (NPT)",
  title="Threaded Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 threaded (NPT screwed) flanges in stainless, duplex, carbon, alloy and nickel alloys. Forged in India. Export to USA and Canada with test certificates.",
  kw=("threaded flange manufacturer", ["NPT threaded flange supplier", "ASME B16.5 threaded flange", "stainless steel threaded flange", "screwed flange"]),
  chips=["ASME B16.5", "NPT", "No welding"],
  intro=[
   "A threaded flange has an internal taper thread, so it screws onto the pipe without welding. It is used where welding is not allowed, for example in explosive atmospheres, and on small lines.",
   "Neo Impex forges threaded flanges to ASME B16.5 with NPT threads in stainless, duplex, carbon, alloy and nickel alloys, with heat-number traceability and EN 10204 3.1 certificates."],
  spec=[("Standards", "ASME B16.5 · EN 1092-1 · BS 4504"), ("Thread", "NPT (US standard taper) · BSP on request")] + FL_COMMON,
  features=["No welding on site", "NPT threads for US and Canadian systems", "Forged from solid material", "Heat-number traceability"],
  apps=["Lines where hot work is not permitted", "Water and utility piping", "Low-temperature, non-cyclic service"],
  faqs=[("NPT or BSP threads?", "NPT is the standard in the USA and Canada. BSP is used in many other markets. State the thread type with your order."),
        ("Are threaded flanges suitable for high temperature?", "Not usually. Threaded joints can loosen under cyclic or high-temperature service, so use weld neck flanges there.")],
  related=["socket-weld", "slip-on", "blind"], art="threaded", photo="threaded.jpg"),

 "lap-joint": dict(
  name="Lap Joint Flanges", short="Loose flange for lines that are often dismantled",
  h1="Lap Joint Flanges",
  title="Lap Joint Flanges Manufacturer & Exporter | USA, Canada",
  desc="ASME B16.5 lap joint flanges for use with stub ends, in stainless, duplex, carbon, alloy and nickel alloys. Forged in India. Export to USA and Canada.",
  kw=("lap joint flange manufacturer", ["ASME B16.5 lap joint flange", "LJ flange with stub end", "stainless steel lap joint flange"]),
  chips=["ASME B16.5", "Use with stub end"],
  intro=[
   "A lap joint flange is a loose ring that slides over a stub end and is held behind its lip. Because it rotates freely, bolt holes line up easily, which suits lines that are dismantled often for cleaning or inspection.",
   "Neo Impex forges lap joint flanges to ASME B16.5 in stainless, duplex, carbon, alloy and nickel alloys. A carbon-steel flange with a stainless stub end is a common way to save cost."],
  spec=[("Standards", "ASME B16.5 · EN 1092-1 · BS 4504"), ("Used with", "Stub ends (ASME B16.9 / MSS SP-43)")] + FL_COMMON,
  features=["Rotates freely for easy bolt-hole alignment", "Allows a lower-cost flange material", "Pairs with long or short pattern stub ends"],
  apps=["Lines that are dismantled often", "Stainless piping with carbon-steel flanges", "Systems with tight alignment tolerances"],
  faqs=[("Does a lap joint flange touch the process fluid?", "No. The fluid contacts the stub end and gasket, so the flange can be a lower-cost material.")],
  related=["stub-ends", "slip-on", "weld-neck"], art="lap", photo=None),

 "ring-type-joint": dict(
  name="Ring Type Joint (RTJ) Flanges", short="Ring joint grooves for Class 600–2500 oil and gas",
  h1="Ring Type Joint (RTJ) Flanges",
  title="RTJ Flanges Manufacturer & Exporter | USA, Canada",
  desc="Ring type joint (RTJ) flanges to ASME B16.5 for high-pressure oil and gas, Class 600 to 2500. Weld neck and blind RTJ flanges. Export to USA and Canada.",
  kw=("RTJ flange manufacturer", ["ring type joint flange", "ASME B16.5 RTJ flange", "Class 600 RTJ weld neck flange", "RTJ blind flange"]),
  chips=["ASME B16.5", "Class 600–2500", "Ring groove"],
  intro=[
   "A ring type joint flange has a machined groove on its face that holds a metal ring gasket. When the flanges are bolted together the ring seals metal-to-metal, which suits high pressure and temperature.",
   "Neo Impex forges RTJ flanges from ½″ to 24″ to ASME B16.5, most often in Class 600 to 2500 for oil and gas, in carbon, alloy, stainless, duplex and nickel alloys."],
  spec=[("Standards", "ASME B16.5 · ring gaskets to ASME B16.20"), ("Facing", "Ring type joint with machined groove"),
        ("Common types", "Weld neck RTJ, blind RTJ")] + FL_COMMON,
  features=["Metal-to-metal sealing for high pressure", "Grooves machined to ring gasket dimensions", "Weld neck and blind RTJ available"],
  apps=["Wellhead and manifold piping", "High-pressure pipelines", "Refinery high-pressure units"],
  faqs=[("Can I reuse a ring gasket?", "Ring gaskets are normally replaced each time a joint is opened. Check your project specification.")],
  related=["weld-neck", "blind", "long-weld-neck"], art="rtj", photo=None),

 "long-weld-neck": dict(
  name="Long Weld Neck Flanges", short="Extended hubs for vessels and column nozzles",
  h1="Long Weld Neck (LWN) Flanges",
  title="Long Weld Neck Flanges Manufacturer & Exporter | USA",
  desc="Long weld neck (LWN) flanges with extended hubs for pressure vessel and column nozzles, made to your drawing. Export to USA and Canada.",
  kw=("long weld neck flange manufacturer", ["LWN flange supplier", "extended weld neck flange", "vessel nozzle flange"]),
  chips=["Made to drawing", "Extended hub"],
  intro=[
   "A long weld neck flange has an extended hub that acts as the nozzle neck on a pressure vessel, column or heat exchanger. The long hub removes a weld near the flange and gives extra strength.",
   "Hub lengths are not fixed by ASME B16.5, so long weld neck flanges are made to your drawing. Neo Impex forges them in carbon, alloy, stainless, duplex and nickel alloys."],
  spec=[("Standards", "Flange dimensions to ASME B16.5 · hub length to customer drawing"), ("Bore", "Machined to drawing")] + FL_COMMON,
  features=["Extended hub for vessel nozzles", "Made to your drawing", "Fewer welds near the flange"],
  apps=["Pressure vessel nozzles", "Distillation columns", "Heat exchangers and reactors"],
  faqs=[("What do you need to quote a long weld neck flange?", "A drawing or sketch with size, class, facing, bore, overall length, material and standard.")],
  related=["weld-neck", "blind", "ring-type-joint"], art="lwn", photo=None),
}

FLANGES_ORDER = ["weld-neck", "slip-on", "blind", "socket-weld", "threaded", "lap-joint", "ring-type-joint", "long-weld-neck"]
