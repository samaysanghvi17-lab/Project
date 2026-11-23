# -*- coding: utf-8 -*-
"""Export-country pages, data sheets and blog posts."""

# ---------------------------------------------------------------- EXPORT
EXPORT = {
 "usa": dict(
  name="United States", h1="Buttweld Fittings and Flanges for the USA",
  title="Buttweld Fittings & Flanges Supplier for the USA",
  desc="Direct from the manufacturer: ASME B16.9 buttweld fittings and B16.5 flanges for US distributors and fabricators, with MTRs, marking and DAP delivery.",
  kw=("buttweld fittings supplier USA", ["flanges manufacturer India export to USA", "ASME B16.9 fittings import from India", "stainless steel flanges USA supplier", "pipe fittings manufacturer Gujarat"]),
  lead="Neo Impex makes buttweld fittings, bends and forged flanges in Vadodara, India, and ships them to US distributors, fabricators and contractors. You buy from the manufacturer, with one set of documents for the whole order.",
  sections=[
   ("What we supply to US buyers", [
    "Buttweld fittings and bends in inch sizes, seamless up to 24″ and welded up to 72″, to ASME B16.9 and MSS SP-43, with MSS SP-25 marking.",
    "Forged flanges from ½″ to 60″ to ASME B16.5 and B16.47, Class 150 to 2500 depending on size, in stainless, duplex, carbon, alloy and nickel alloys."]),
   ("Documents with every shipment", [
    "Heat-traceable EN 10204 3.1 mill test certificates, commercial invoice, packing list, bill of lading and certificate of origin. Additional tests and third-party inspection can be written into your purchase order.",
    "US customs also requires permanent country-of-origin marking on imported goods. Tell us your marking requirement when you order."]),
   ("Terms and delivery", [
    "We quote FOB, CIF or DAP. DAP delivery to your US door is available, so you can compare us on landed cost. Typical entry ports are Houston, New Orleans, New York/New Jersey and Los Angeles.",
    "Send your bill of quantities and we reply with price, lead time and terms within 24 business hours."]),
   ("Duties, tariffs and project rules: check before you order", [
    "US steel tariffs and anti-dumping or countervailing duty orders change often, and some steel flanges and fittings from some countries have been covered. Confirm the current duty position for your product with your customs broker before ordering.",
    "Projects funded by federal or state water and infrastructure money can carry Buy America or American Iron and Steel requirements that imported material may not meet. Tell us if your project has domestic-content rules."]),
  ],
  faqs=[("Do you supply to US distributors and fabricators?", "Yes. We supply buttweld fittings and flanges to US distributors, fabricators and contractors, direct from our works in Vadodara."),
        ("Can you deliver duty paid to my door?", "We can quote DAP delivery. Duties and taxes depend on the product and current rules, so ask your customs broker to confirm before ordering."),
        ("Which certificates do you provide?", "EN 10204 3.1 mill test certificates with heat numbers, plus the shipping documents. Additional tests and third-party inspection can be agreed in your purchase order."),
        ("Which ports do you ship to?", "Typical entry ports are Houston, New Orleans, New York/New Jersey and Los Angeles. Tell us your delivery port or ZIP code.")],
  ports=["Houston", "New Orleans", "New York / New Jersey", "Los Angeles"]),

 "canada": dict(
  name="Canada", h1="Buttweld Fittings and Flanges for Canada",
  title="Buttweld Fittings & Flanges Supplier for Canada",
  desc="ASME B16.9 buttweld fittings and B16.5 flanges direct from the manufacturer for Canadian distributors, fabricators and contractors, with 3.1 certificates.",
  kw=("buttweld fittings supplier Canada", ["flanges supplier Canada from India", "ASME B16.5 flanges Canada import", "pipe fittings exporter India Canada", "low temperature flanges A350 LF2 Canada"]),
  lead="Neo Impex makes buttweld fittings, bends and forged flanges in Vadodara, India, for Canadian distributors, fabricators and contractors. Cold-climate service, large sizes and special alloys are our strengths.",
  sections=[
   ("What we supply to Canadian buyers", [
    "Buttweld fittings and bends to ASME B16.9 and MSS SP-43, seamless up to 24″ and welded up to 72″, and forged flanges from ½″ to 60″ to ASME B16.5 and B16.47.",
    "For cold-climate service we supply impact-tested A350 LF2 flanges and A420 WPL6 fittings (tested at −46 °C), as well as stainless, duplex, alloy and nickel alloys."]),
   ("Documents and importing", [
    "Every order ships with heat-traceable EN 10204 3.1 certificates, a commercial invoice, packing list, bill of lading and certificate of origin. Most Canadian importers use a customs broker to file with the Canada Border Services Agency (CBSA).",
    "Typical entry ports are Vancouver, Prince Rupert, Montreal and Halifax, with onward rail or truck to Alberta and Ontario."]),
   ("Pressure equipment registration (CRN)", [
    "Canadian provinces regulate pressure equipment, and some fittings need a Canadian Registration Number (CRN) under provincial rules. Standard ASME B16 fittings are often accepted, but requirements vary by province and by use. Check with your provincial authority (such as TSSA in Ontario, ABSA in Alberta or Technical Safety BC) before ordering, and tell us what documents your project needs."]),
   ("Duties and trade measures: check before you order", [
    "Canada applies tariffs and trade measures to some steel products, and they have changed repeatedly. Ask your customs broker to confirm the current position for your product and country of origin."]),
  ],
  faqs=[("Do you supply Canadian distributors and fabricators?", "Yes. We supply buttweld fittings and flanges to Canadian distributors, fabricators and contractors."),
        ("Do you have low-temperature material for Canadian winters?", "Yes. We supply A350 LF2 flanges and A420 WPL6 fittings, impact tested at −46 °C. Confirm your minimum design metal temperature with your engineer."),
        ("Do your fittings have a CRN?", "Requirements depend on the fitting, the province and the use. Contact us with your project details and your provincial authority’s requirement, and we will tell you what documents we can supply."),
        ("Which ports do you ship to?", "Typical entry ports are Vancouver, Prince Rupert, Montreal and Halifax. Tell us your delivery location.")],
  ports=["Vancouver", "Prince Rupert", "Montreal", "Halifax"]),
}

EXPORT_HUB = dict(
  title="Export of Buttweld Fittings & Flanges | USA, Canada",
  desc="Neo Impex exports ASME buttweld fittings and flanges from India to the USA and Canada with 3.1 certificates, marking and DAP delivery. Quote in 24 hours.",
  h1="Export of Buttweld Fittings and Flanges")

# ---------------------------------------------------------------- DATA SHEETS
PIPE = [  # NPS, DN, OD in, OD mm, S40 in, S40 mm, S80 in, S80 mm
 ("½", 15, "0.840", "21.3", "0.109", "2.77", "0.147", "3.73"),
 ("¾", 20, "1.050", "26.7", "0.113", "2.87", "0.154", "3.91"),
 ("1", 25, "1.315", "33.4", "0.133", "3.38", "0.179", "4.55"),
 ("1¼", 32, "1.660", "42.2", "0.140", "3.56", "0.191", "4.85"),
 ("1½", 40, "1.900", "48.3", "0.145", "3.68", "0.200", "5.08"),
 ("2", 50, "2.375", "60.3", "0.154", "3.91", "0.218", "5.54"),
 ("2½", 65, "2.875", "73.0", "0.203", "5.16", "0.276", "7.01"),
 ("3", 80, "3.500", "88.9", "0.216", "5.49", "0.300", "7.62"),
 ("4", 100, "4.500", "114.3", "0.237", "6.02", "0.337", "8.56"),
 ("6", 150, "6.625", "168.3", "0.280", "7.11", "0.432", "10.97"),
 ("8", 200, "8.625", "219.1", "0.322", "8.18", "0.500", "12.70"),
 ("10", 250, "10.750", "273.1", "0.365", "9.27", "0.594", "15.09"),
 ("12", 300, "12.750", "323.9", "0.406", "10.31", "0.688", "17.48"),
 ("14", 350, "14.000", "355.6", "0.438", "11.13", "0.750", "19.05"),
 ("16", 400, "16.000", "406.4", "0.500", "12.70", "0.844", "21.44"),
 ("18", 450, "18.000", "457.2", "0.562", "14.27", "0.938", "23.83"),
 ("20", 500, "20.000", "508.0", "0.594", "15.09", "1.031", "26.19"),
 ("24", 600, "24.000", "609.6", "0.688", "17.48", "1.218", "30.96"),
]

# 90 degree elbow center-to-end (ASME B16.9 / B16.28): long radius = 1.5 x NPS, short radius = 1.0 x NPS, NPS 1 and larger
ELBOW_SIZES = [("1", 1.0, 38, 25), ("1¼", 1.25, 48, 32), ("1½", 1.5, 57, 38), ("2", 2, 76, 51), ("2½", 2.5, 95, 64),
               ("3", 3, 114, 76), ("4", 4, 152, 102), ("6", 6, 229, 152), ("8", 8, 305, 203), ("10", 10, 381, 254),
               ("12", 12, 457, 305), ("14", 14, 533, 356), ("16", 16, 610, 406), ("18", 18, 686, 457), ("20", 20, 762, 508), ("24", 24, 914, 610)]

DS_NOTE = ("Reference values for quotation and planning. Final dimensions and tolerances follow the applicable standard "
           "and the approved drawing or purchase order.")

DATASHEETS = {
 "buttweld-fittings": dict(
  title="Buttweld Fittings Data Sheet | ASME B16.9, MSS SP-43",
  desc="Data sheet for Neo Impex buttweld fittings: standards, sizes, materials, wall thickness, testing, marking and documents. Print or save as PDF.",
  h1="Buttweld Fittings Data Sheet",
  kw=("buttweld fittings data sheet", ["ASME B16.9 specification sheet", "butt weld fittings dimensions chart"])),
 "flanges": dict(
  title="Forged Flanges Data Sheet | ASME B16.5, B16.47",
  desc="Data sheet for Neo Impex forged flanges: standards, types, sizes, pressure classes, facings, materials, marking and documents. Print or save as PDF.",
  h1="Forged Flanges Data Sheet",
  kw=("flanges data sheet", ["ASME B16.5 specification sheet", "forged flange specification"])),
 "pipe-schedule-chart": dict(
  title="Pipe Schedule Chart | NPS, OD and Wall Thickness",
  desc="Free pipe schedule chart: NPS, DN, outside diameter and Sch 40 and Sch 80 wall thickness in inches and mm, plus 90° elbow center-to-end dimensions.",
  h1="Pipe Schedule Chart and Elbow Dimensions",
  kw=("pipe schedule chart", ["pipe schedule 40 80 dimensions", "NPS OD wall thickness chart", "90 degree elbow center to end dimensions"])),
}

# ---------------------------------------------------------------- BLOG
BLOG = [
 dict(slug="seamless-vs-welded-buttweld-fittings", date="2026-11-22",
  title="Seamless vs Welded Buttweld Fittings: Which to Choose",
  h1="Seamless vs Welded Buttweld Fittings: Which Should You Choose?",
  desc="How seamless and welded buttweld fittings are made, where each is used, and what to ask your supplier about size limits, radiography and certificates.",
  kw=("seamless vs welded fittings", ["seamless buttweld fittings", "welded butt weld fittings"]),
  intro="Both seamless and welded buttweld fittings are made to ASME B16.9 and fit the same pipe. The difference is how they are made, and that affects size range, cost and what you should ask for in the purchase order.",
  body=[
   ("How seamless fittings are made", ["Seamless fittings are formed from a length of seamless pipe or a forged billet. The pipe is heated and pushed over a die (hot forming) so it takes the shape of an elbow, tee or reducer. There is no longitudinal weld seam in the body.", "Neo Impex makes seamless fittings up to 24″."]),
   ("How welded fittings are made", ["Welded fittings are made from plate or welded pipe, formed into shape and joined with one or more welds. This is how most large-diameter fittings are made, because seamless pipe and forming equipment are limited at big sizes.", "Neo Impex makes welded fittings up to 72″ and radiographs 100% of the welded seams."]),
   ("Which should you choose?", ["Use seamless where your specification requires it or for sizes up to 24″ where lead time and cost are similar. Use welded for large diameters, for heavy walls in special alloys, and where the design allows welded fittings with full radiography.", "Many piping classes allow both. Check your line class and code, because the design factors for welded fittings depend on the extent of examination."]),
   ("What to ask your supplier", ["Ask for the heat number on every piece, the EN 10204 3.1 certificate, and confirmation of radiography on welded seams. For stainless steels, ask for the heat treatment (solution annealing) record.", "State seamless or welded clearly in the purchase order, together with the size, schedule, grade and standard."]),
  ],
  related=[("/buttweld-fittings/elbows/", "Buttweld elbows"), ("/buttweld-fittings/tees/", "Buttweld tees"), ("/data-sheets/buttweld-fittings/", "Buttweld fittings data sheet")]),

 dict(slug="316-vs-316l-stainless-steel", date="2026-11-22",
  title="316 vs 316L Stainless Steel for Flanges and Fittings",
  h1="316 vs 316L Stainless Steel: What Is the Difference?",
  desc="316 and 316L stainless differ mainly in carbon content. What that means for welding, strength and dual certification when buying flanges and fittings.",
  kw=("316 vs 316L stainless steel", ["316L flanges", "dual certified 316/316L"]),
  intro="Grades 316 and 316L are the same alloy family, both with about 2–3% molybdenum for resistance to chlorides. The difference that matters when you buy flanges and fittings is the carbon limit.",
  body=[
   ("The carbon difference", ["316 allows up to 0.08% carbon. 316L allows up to 0.030%. The lower carbon in 316L reduces the risk of carbide precipitation (sensitization) in the heat-affected zone when you weld, which can otherwise lower corrosion resistance at the weld."]),
   ("What about strength?", ["The ASTM minimum tensile strengths are 515 MPa (75 ksi) for 316 and 485 MPa (70 ksi) for 316L, and the minimum yield strengths are 205 MPa (30 ksi) and 170 MPa (25 ksi). Actual strength on your certificate is usually above these minimums."]),
   ("Dual certification", ["Modern melts often meet both grades at once, so mills certify material as dual-grade 316/316L. This lets you use one stock for both. If your specification requires a single grade, say so when you order."]),
   ("Which should you specify?", ["Specify 316L (or dual-certified 316/316L) for welded construction. Specify 316 where the part is not welded or where the higher carbon is acceptable. For very high chloride service, consider duplex or super duplex instead."]),
  ],
  related=[("/buttweld-fittings/materials/ss-316-316l/", "316/316L buttweld fittings"), ("/flanges/materials/ss-316-316l/", "316/316L flanges")]),

 dict(slug="asme-b16-9-vs-mss-sp-43", date="2026-11-22",
  title="ASME B16.9 vs MSS SP-43: Standard and Light-Wall Fittings",
  h1="ASME B16.9 vs MSS SP-43: Standard and Light-Wall Stainless Fittings",
  desc="ASME B16.9 and MSS SP-43 both cover buttweld fittings. Learn how they differ, when light-wall fittings are used and what to state in your purchase order.",
  kw=("ASME B16.9 vs MSS SP-43", ["MSS SP-43 fittings", "light wall stainless fittings"]),
  intro="ASME B16.9 and MSS SP-43 both cover factory-made wrought buttweld fittings, but they serve different piping. Choosing the wrong one gives you fittings with the wrong wall thickness.",
  body=[
   ("ASME B16.9", ["ASME B16.9 covers wrought buttweld fittings in carbon and alloy steels and in stainless steel, in wall thicknesses that match standard pipe schedules. It sets dimensions, tolerances, marking and testing. It is the default standard for most process and pipeline fittings."]),
   ("MSS SP-43", ["MSS SP-43 covers wrought stainless steel and nickel alloy buttweld fittings in lighter wall thicknesses, typically for corrosion-resistant piping at lower pressure. The walls correspond to light schedules such as 5S and 10S."]),
   ("Which to choose", ["Choose ASME B16.9 when you need pipe-schedule walls or higher pressure. Choose MSS SP-43 for light-wall stainless systems such as food, pharma and water, where the pipe itself is thin-walled. The fitting wall should match the pipe wall so that welding and flow are smooth."]),
   ("What to put on the purchase order", ["State the standard, the size, the wall thickness or schedule on each end, the material grade and ASTM specification, seamless or welded, and any extra tests. Neo Impex supplies both standards."]),
  ],
  related=[("/buttweld-fittings/elbows/", "Buttweld elbows"), ("/buttweld-fittings/stub-ends/", "Stub ends"), ("/data-sheets/pipe-schedule-chart/", "Pipe schedule chart")]),

 dict(slug="weld-neck-vs-slip-on-flange", date="2026-11-22",
  title="Weld Neck vs Slip-On Flanges: How to Choose",
  h1="Weld Neck vs Slip-On Flanges: How to Choose",
  desc="Compare weld neck and slip-on flanges on strength, cost, welding and typical use, so you can specify the right flange for your piping.",
  kw=("weld neck vs slip on flange", ["WNRF vs SORF", "which flange to choose"]),
  intro="Weld neck and slip-on flanges both bolt to the same ASME B16.5 pattern, so they connect to each other. They differ in how they are attached to the pipe, and that affects strength, cost and inspection.",
  body=[
   ("Weld neck flanges", ["A weld neck flange has a long tapered hub that is butt-welded to the pipe. The hub carries stress smoothly into the pipe, and the butt weld can be radiographed. This makes weld neck the usual choice for high pressure, high temperature, cyclic and critical service."]),
   ("Slip-on flanges", ["A slip-on flange slides over the pipe and is fillet-welded inside and outside. It costs less, needs less precise cutting and is easier to align. It is lower in strength and fatigue life than a weld neck flange, so it suits moderate pressure and non-critical lines."]),
   ("Quick comparison", ["Strength and fatigue: weld neck is better. Cost: slip-on is lower. Alignment: slip-on is easier. Inspection: weld neck butt weld can be radiographed. Typical use: weld neck for critical and high-pressure lines, slip-on for utility and low-pressure lines."]),
   ("What to specify", ["For either flange, state size, pressure class, facing (raised face, RTJ), material and standard. For weld neck flanges also state the pipe schedule so the bore is machined to match."]),
  ],
  related=[("/flanges/weld-neck/", "Weld neck flanges"), ("/flanges/slip-on/", "Slip-on flanges")]),

 dict(slug="how-to-read-flange-markings", date="2026-11-22",
  title="How to Read ASME B16.5 Flange Markings",
  h1="How to Read ASME B16.5 Flange Markings",
  desc="What the stamps on a flange rim mean: manufacturer, ASTM material, class, standard, size and heat number, and how to check them on the certificate.",
  kw=("flange markings", ["ASME B16.5 flange marking", "how to read flange stamp", "flange heat number"]),
  intro="Flange rims are stamped so that every piece can be identified and traced. Learning to read the marks is the quickest way to check that what arrived matches what you ordered.",
  body=[
   ("What is usually marked", ["Typical marks on a forged flange are the manufacturer’s name or trademark, the ASTM material specification and grade (for example A105 or A182 F316L), the pressure class (for example 150 or 300), the standard (B16.5), the nominal size, and a heat number."]),
   ("An example", ["A stainless flange rim might read: 150, B16.5, A182 F304, with a heat number. That tells you it is Class 150, made to ASME B16.5, from ASTM A182 grade F304, and traceable to a specific heat."]),
   ("Matching marks to the certificate", ["Take the heat number from the flange and find it on the EN 10204 3.1 mill test certificate. The certificate should show the chemistry and mechanical properties for that heat and match the grade stamped on the flange."]),
   ("If marks do not match", ["If the grade, class or heat number does not match the paperwork, do not install the flange. Contact the supplier and keep the piece for inspection."]),
  ],
  related=[("/flanges/", "Forged flanges"), ("/flanges/weld-neck/", "Weld neck flanges")]),

 dict(slug="import-buttweld-fittings-flanges-india-to-usa", date="2026-11-22",
  title="Importing Buttweld Fittings and Flanges from India to the USA",
  h1="Importing Buttweld Fittings and Flanges from India to the USA",
  desc="A checklist for US importers: documents, marking, HTS codes, security filing, duties and Buy America checks when buying fittings and flanges from India.",
  kw=("import pipe fittings from India to USA", ["importing flanges from India", "HTS code butt welding fittings", "buy flanges from India"]),
  intro="Buying fittings and flanges direct from an Indian manufacturer can cut cost and give you access to special sizes and alloys. A good import goes smoothly when you have the paperwork, marking and duty position settled before you order. This is a general checklist, not legal or customs advice.",
  body=[
   ("1. Check the duty position first", ["US steel tariffs and anti-dumping or countervailing duty orders change often. Before you order, ask your customs broker to confirm the current position for your exact product and country of origin."]),
   ("2. Classify the goods", ["Pipe fittings and flanges of iron or steel fall under Harmonized Tariff Schedule heading 7307. Butt welding fittings and flanges are separate subheadings, with separate lines for stainless and other steel. Your broker should confirm the exact code."]),
   ("3. Gather the documents", ["Typical documents are the commercial invoice, packing list, bill of lading, certificate of origin and EN 10204 3.1 mill test certificates. Ocean cargo also needs an Importer Security Filing, usually made by your broker, before the goods are loaded."]),
   ("4. Plan the marking", ["US customs requires permanent country-of-origin marking on imported goods. Fittings are also marked to MSS SP-25 with grade, size, schedule and heat number. Agree both with your supplier."]),
   ("5. Check project rules", ["Projects funded with federal or state water and infrastructure money can carry Buy America or American Iron and Steel requirements that imported material may not satisfy. Confirm this before you source."]),
   ("6. Choose the delivery term", ["FOB and CIF leave customs clearance and inland delivery to you. DAP or DDP puts more of the logistics on the seller. Compare quotes on landed cost, not just the factory price."]),
  ],
  related=[("/export/usa/", "Supply to the USA"), ("/blog/incoterms-for-pipe-fittings-export/", "Incoterms for pipe fittings")]),

 dict(slug="incoterms-for-pipe-fittings-export", date="2026-11-22",
  title="Incoterms for Pipe Fittings Export: FOB, CIF, DAP, DDP",
  h1="Incoterms for Pipe Fittings Export: FOB, CIF, DAP and DDP",
  desc="What FOB, CIF, DAP and DDP mean when you buy buttweld fittings and flanges from India, who pays for what, and how to compare quotes on landed cost.",
  kw=("incoterms pipe fittings", ["FOB vs CIF vs DAP", "DAP delivery pipe fittings", "landed cost flanges"]),
  intro="Incoterms say who pays for freight, insurance, customs and risk at each step of an export. When you compare quotes for buttweld fittings and flanges, the term decides whether two prices are really comparable.",
  body=[
   ("FOB: free on board", ["The seller delivers the goods on board the ship at the Indian port. You pay the ocean freight, insurance, import customs and delivery from the port of arrival. FOB gives the buyer most control and the lowest quoted price."]),
   ("CIF: cost, insurance and freight", ["The seller pays freight and minimum insurance to your destination port. You pay import customs and inland delivery. The price is higher than FOB because it includes freight."]),
   ("DAP: delivered at place", ["The seller delivers to the named place, for example your warehouse, ready for unloading, and pays freight to there. You pay import customs and duties."]),
   ("DDP: delivered duty paid", ["The seller handles delivery and import clearance and pays duties. It is the simplest for the buyer but needs the seller to act as importer, so it is used less often for steel products."]),
   ("Comparing quotes", ["Convert every quote to landed cost: price, freight, insurance, duty and delivery. A low FOB price can cost more than a DAP quote once freight and fees are added. Tell us your delivery port or ZIP code and we will quote on your terms."]),
  ],
  related=[("/export/usa/", "Supply to the USA"), ("/export/canada/", "Supply to Canada")]),
]

# ---------------------------------------------------------------- MORE BLOG POSTS
BLOG += [
 dict(slug="long-radius-vs-short-radius-elbows", date="2026-11-23",
  title="Long Radius vs Short Radius Elbows: How to Choose",
  h1="Long Radius vs Short Radius Elbows: How to Choose",
  desc="Long radius elbows have a radius of 1.5 times the pipe size and short radius elbows 1.0. Learn when to use each and what to state on the purchase order.",
  kw=("long radius vs short radius elbow", ["ASME B16.9 long radius elbow", "ASME B16.28 short radius elbow", "1.5D elbow"]),
  intro="Buttweld elbows come in two standard radii. The choice changes how much room the elbow needs and how much pressure the fluid loses going round the bend.",
  body=[
   ("The two radii", ["A long radius (LR) elbow has a centerline radius of 1.5 times the nominal pipe size, written 1.5D. It is covered by ASME B16.9. A short radius (SR) elbow has a radius equal to the nominal pipe size, written 1D, and is covered by ASME B16.28."]),
   ("Flow and space", ["The gentler curve of a long radius elbow gives lower pressure drop and less erosion at the bend. A short radius elbow turns in a smaller space, so it suits tight layouts, but it adds more resistance to flow."]),
   ("Which one is the default?", ["Long radius is the default for most process and pipeline systems, and it is what a drawing means if it only says “elbow”. Use short radius only where space is limited and your design allows the extra pressure drop."]),
   ("What to write on the order", ["State the angle (45°, 90° or 180°), long or short radius, nominal size, schedule, material grade and standard, for example: 6″ 90° LR elbow, SCH 40S, ASTM A403 WP316L, ASME B16.9."]),
  ],
  related=[("/buttweld-fittings/elbows/", "Buttweld elbows"), ("/buttweld-fittings/return-bends/", "180° return bends"), ("/data-sheets/pipe-schedule-chart/", "Elbow dimensions chart")]),

 dict(slug="concentric-vs-eccentric-reducers", date="2026-11-23",
  title="Concentric vs Eccentric Reducers: When to Use Each",
  h1="Concentric vs Eccentric Reducers: When to Use Each",
  desc="A concentric reducer keeps both ends on one centerline; an eccentric reducer keeps one side flat. See where each is used and how to specify a reducer.",
  kw=("concentric vs eccentric reducer", ["eccentric reducer pump suction", "buttweld reducer"]),
  intro="Both reducers change pipe size. The difference is where the center of the smaller end sits, and that decides how air, liquid and supports behave in the line.",
  body=[
   ("Concentric reducers", ["Both ends share the same centerline and the cone is symmetrical. Concentric reducers are common on vertical lines and in places where a symmetric change in size is fine."]),
   ("Eccentric reducers", ["The smaller end is offset, so one side of the fitting stays straight. This keeps the pipe top or bottom level, which avoids trapping air or liquid and keeps the underside of a rack flat."]),
   ("Common practice", ["On horizontal pump suction lines, an eccentric reducer is usually installed flat on top so air can escape and does not collect in the pump. On pipe racks, flat on bottom keeps the pipe at a constant support height. Always follow your piping design."]),
   ("How to specify", ["Give the large end by the small end, the schedule on each end, concentric or eccentric, the material grade and the standard, for example: 10″ × 6″ eccentric reducer, SCH 40, ASTM A234 WPB, ASME B16.9."]),
  ],
  related=[("/buttweld-fittings/reducers/", "Buttweld reducers"), ("/buttweld-fittings/tees/", "Buttweld tees")]),

 dict(slug="flange-pressure-classes-explained", date="2026-11-23",
  title="Flange Pressure Classes: Class 150 to 2500 Explained",
  h1="Flange Pressure Classes: Class 150, 300, 600, 900, 1500 and 2500",
  desc="What ASME B16.5 flange classes mean, why a class number is not a pressure in psi, and how material and temperature change the allowed pressure.",
  kw=("flange pressure class", ["Class 150 vs 300 flange", "ASME B16.5 pressure temperature rating", "Class 600 flange"]),
  intro="A flange class such as 150 or 300 is a rating category, not a pressure in psi. The pressure a flange can hold depends on the class, the material and the temperature.",
  body=[
   ("The classes", ["ASME B16.5 covers Class 150, 300, 400, 600, 900, 1500 and 2500. Higher classes have thicker flanges and larger bolting, so they hold more pressure."]),
   ("Why class is not psi", ["The allowed working pressure falls as temperature rises and differs between material groups. As an example, for carbon steel A105 at ambient temperature (up to about 38 °C or 100 °F), B16.5 gives roughly 285 psig for Class 150, 740 for Class 300, 1480 for Class 600, 2220 for Class 900, 3705 for Class 1500 and 6170 for Class 2500. At higher temperatures the values are lower."]),
   ("How to choose", ["Take the design pressure and temperature of the line, find the material group of your flange in the ASME B16.5 pressure-temperature tables, and pick the lowest class that covers both. Your line class specification normally does this for you."]),
   ("What to put on the order", ["State size, class, facing, flange type, material grade and standard, for example: 4″ Class 300 WNRF, SCH 80, ASTM A105, ASME B16.5. The figures above are for orientation only; always use the current standard for design."]),
  ],
  related=[("/flanges/weld-neck/", "Weld neck flanges"), ("/flanges/blind/", "Blind flanges"), ("/data-sheets/flanges/", "Flanges data sheet")]),

 dict(slug="raised-face-vs-ring-type-joint-flanges", date="2026-11-23",
  title="Raised Face vs Ring Type Joint Flanges",
  h1="Raised Face vs Ring Type Joint Flanges: What Is the Difference?",
  desc="Raised face flanges seal with a gasket; ring type joint flanges seal with a metal ring in a machined groove. See when each is used and how they must match.",
  kw=("raised face vs ring type joint flange", ["RTJ flange", "RF flange", "RTJ ring gasket"]),
  intro="The flange face is where the seal is made. Raised face and ring type joint flanges bolt to the same pattern in many sizes, but they seal in different ways and cannot be mixed.",
  body=[
   ("Raised face (RF)", ["A raised face flange has a slightly raised circle around the bore that concentrates bolt load on a flat gasket, such as spiral wound or sheet. RF is the most common facing and suits a wide range of pressures and fluids."]),
   ("Ring type joint (RTJ)", ["An RTJ flange has a machined groove in its face that holds a metal ring gasket. When the bolts are tightened the ring deforms into the groove and seals metal to metal. RTJ is common for high pressure and temperature, often Class 600 and above in oil and gas."]),
   ("They must match", ["An RTJ flange mates with another RTJ flange of the same size and class, and the ring must match the groove. Ring dimensions are covered by ASME B16.20. Rings are normally replaced each time the joint is opened."]),
   ("What to specify", ["State the facing with the flange: for example 6″ Class 900 WNRTJ, ASTM A105, ASME B16.5, with the ring type and material if you need us to supply rings."]),
  ],
  related=[("/flanges/ring-type-joint/", "RTJ flanges"), ("/flanges/weld-neck/", "Weld neck flanges")]),

 dict(slug="how-to-read-an-en-10204-3-1-certificate", date="2026-11-23",
  title="How to Read an EN 10204 3.1 Mill Test Certificate",
  h1="How to Read an EN 10204 3.1 Mill Test Certificate",
  desc="What an EN 10204 3.1 certificate contains, how to match its heat number to your fittings and flanges, and how it differs from type 3.2.",
  kw=("EN 10204 3.1 certificate", ["mill test certificate", "MTC for flanges and fittings", "EN 10204 3.2"]),
  intro="An EN 10204 type 3.1 certificate is the manufacturer’s statement that the material meets its order and standard, backed by test results. Reading it takes a few minutes and avoids most material mix-ups.",
  body=[
   ("What it contains", ["The certificate lists the manufacturer, the heat or cast number, the product and size, the material standard and grade, the chemical composition, and the mechanical test results such as yield strength, tensile strength and elongation. It may also show hardness, impact tests and the heat treatment."]),
   ("Who signs it", ["A type 3.1 certificate is validated by the manufacturer’s authorized inspection representative, who is independent of the production department. A type 3.2 certificate is also validated by an independent party, such as the purchaser’s inspector or a third-party inspection body."]),
   ("How to check it", ["Find the heat number stamped on your flange or fitting and look for the same number on the certificate. Then compare the grade and standard with your order, and check that the chemistry and test values sit within the limits for that grade."]),
   ("If something does not match", ["If the heat number, grade or values do not match, do not install the part. Contact the supplier and keep the piece for inspection. Neo Impex ships heat-traceable parts with a 3.1 certificate, and can arrange third-party inspection if you need a 3.2."]),
  ],
  related=[("/blog/how-to-read-flange-markings/", "How to read flange markings"), ("/data-sheets/buttweld-fittings/", "Buttweld fittings data sheet")]),

 dict(slug="buttweld-end-preparation-asme-b16-25", date="2026-11-23",
  title="Buttweld End Preparation: ASME B16.25 Bevels Explained",
  h1="Buttweld End Preparation: ASME B16.25 Bevels Explained",
  desc="ASME B16.25 defines the bevels on buttweld fittings and flanges. Learn the standard bevel angle, root face and why the end must match the pipe.",
  kw=("ASME B16.25 bevel", ["buttweld end preparation", "37.5 degree bevel", "weld bevel for fittings"]),
  intro="Buttweld fittings and weld neck flanges are welded to the pipe at a beveled end. ASME B16.25 sets the shape of that bevel so that welders and fittings from different makers fit together.",
  body=[
   ("The standard bevel", ["For the usual wall thicknesses, the standard bevel is 37.5° (with a tolerance of ±2.5°), leaving a small flat land at the root called the root face, about 1.6 mm (1/16 in). For heavier walls, a compound bevel is used."]),
   ("Why the ends must match", ["The bore and wall at the fitting end should match the pipe. A step between the two disturbs flow and makes a poor weld. Tell us the pipe schedule or wall thickness so the fitting or flange bore is made to suit."]),
   ("Special preparations", ["Some jobs need a different bevel, a counterbore, or a plain end, for example for automatic welding. State this on the drawing or order so it is made at the works instead of on site."]),
   ("What to write on the order", ["State the standard (ASME B16.25), the wall thickness or schedule at each end, and any special bevel. If you give no instruction, the standard bevel is supplied."]),
  ],
  related=[("/buttweld-fittings/", "Buttweld fittings"), ("/flanges/weld-neck/", "Weld neck flanges"), ("/data-sheets/pipe-schedule-chart/", "Pipe schedule chart")]),
]
