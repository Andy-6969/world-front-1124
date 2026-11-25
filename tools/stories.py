"""Every story on the page, as reported on Tuesday 24 November 2026. docs/sources.md has the links.

tag: CONFIRMED = two or more outlets; OFFICIAL = on the record from the body named; REPORTED = one outlet;
CLAIM = one side's word, not independently confirmed.
"""

DATE = "Tuesday 24 November 2026"

REGIONS = {  # key: (label, colour)
    "eu": ("Europe", "#2457a3"),
    "me": ("Middle East", "#b42318"),
    "af": ("Africa", "#b45309"),
    "sa": ("South Asia", "#15803d"),
    "ea": ("East & SE Asia", "#0e7490"),
    "na": ("North America", "#6d28d9"),
    "la": ("Latin America", "#be185d"),
    "oc": ("Oceania", "#0369a1"),
    "gl": ("World", "#374151"),
}

# Three leads, drawn large. pic names a drawing in tools/pictures.py.
LEADS = [
    dict(region="ea", place="SHANGHAI, CHINA", field="POLITICS", tag="OFFICIAL",
         lon=121.47, lat=31.23, pic="probe", big="POLITBURO", small="MEMBER PROBED",
         head="China probes Shanghai's party chief, Chen Jining",
         dek="The 4th Politburo member probed since last year.",
         src="Xinhua · Al Jazeera · Reuters"),
    dict(region="na", place="NEW YORK, US", field="COURTS", tag="CONFIRMED",
         lon=-73.95, lat=40.65, pic="verdict", big="10 OF 12", small="COUNTS GUILTY",
         head="US jury convicts Huawei of stealing trade secrets",
         dek="Tuesday's verdict in the case first filed in 2018.",
         src="The Guardian · AP · Reuters"),
    dict(region="eu", place="ZAPORIZHZHIA, UKRAINE", field="WAR", tag="CONFIRMED",
         lon=35.14, lat=47.84, pic="apartment", big="2 KILLED", small="OVER 40 HURT",
         head="Russian strike on a Zaporizhzhia block kills 2",
         dek="A five-storey building is hit in a dawn raid.",
         src="Al Jazeera · AP"),
]

# Eight drawn cards. The brief is the one-line form used if a variant drops the card into the list.
CARDS = [
    dict(region="na", place="CALIFORNIA, US", field="TECH", tag="CONFIRMED",
         lon=-121.95, lat=37.35, pic="chipdown", big="−6%", small="NVIDIA SHARES",
         head="Nvidia boss apologises to staff; shares slide",
         dek="Huang: “I made some terrible mistakes.”",
         brief=("US", "Nvidia's Huang apologises to staff; shares fall"), src="The Guardian · Al Jazeera"),
    dict(region="eu", place="PARIS, FRANCE", field="BUSINESS", tag="OFFICIAL",
         lon=2.35, lat=48.86, pic="pill", big="$41bn", small="SANOFI + INSMED",
         head="Sanofi agrees to buy Insmed for $41bn",
         dek="$175 a share in cash for the US firm.",
         brief=("France", "Sanofi to buy Insmed for $41bn"), src="Sanofi"),
    dict(region="af", place="DAKAR · FOOTBALL", field="SPORT", tag="CONFIRMED",
         lon=-17.45, lat=14.69, pic="trophy", big="CAS RULING", small="TITLE RESTORED",
         head="Sports court restores Senegal's AFCON title",
         dek="Senegal are African champions again.",
         brief=("Senegal", "CAS restores its AFCON title"), src="AP · The Guardian"),
    dict(region="me", place="RIYADH, SAUDI ARABIA", field="ATTACK", tag="CONFIRMED",
         lon=46.68, lat=24.71, pic="tower", big="11 HURT", small="DRONE HITS TOWER",
         head="Drone strikes a Riyadh financial-district tower",
         dek="Coalition blames the Houthis.",
         brief=("Riyadh", "drone hits a tower, 11 hurt"), src="Al Jazeera · AFP"),
    dict(region="ea", place="ULLEUNGDO, S. KOREA", field="SECURITY", tag="OFFICIAL",
         lon=130.9, lat=37.5, pic="jets", big="TAKE SHELTER", small="RUSSIAN JETS NEAR",
         head="Russian jets set off a Korean air-raid alert",
         dek="About five enter Seoul's air zone.",
         brief=("S. Korea", "Russian jets trigger air-raid alert"), src="Joint Chiefs · Al Jazeera"),
    dict(region="me", place="GAZA", field="WAR", tag="CONFIRMED",
         lon=34.45, lat=31.5, pic="gaza", big="DRONE STRIKE", small="HAMAS SECURITY CHIEF",
         head="Israel kills Hamas's internal security chief",
         dek="Naim Abu Nahl dies in a drone strike.",
         brief=("Gaza", "Israeli strike kills Hamas security chief"), src="Al Jazeera · The Guardian"),
    dict(region="eu", place="ENGLAND, UK", field="HEALTH", tag="OFFICIAL",
         lon=-1.5, lat=52.5, pic="thermo", big="5,258", small="HEAT DEATHS",
         head="Record 5,258 summer heat deaths in England",
         dek="UKHSA: the old record was 2,985, in 2022.",
         brief=("England", "record 5,258 summer heat deaths"), src="UKHSA · Reuters"),
    dict(region="me", place="RAS AL KHAIMAH, UAE", field="ACCIDENT", tag="CONFIRMED",
         lon=55.94, lat=25.79, pic="bus", big="13 DEAD", small="14 INJURED",
         head="Bus hits a parked truck in the UAE, killing 13",
         dek="Police say 14 more are in hospital.",
         brief=("UAE", "bus crash kills 13"), src="Gulf News · The National"),
    # drawn only when a variant shows 10 cards; otherwise these two fall back to the short list
    dict(region="me", place="KIRKUK, IRAQ", field="ENERGY", tag="OFFICIAL",
         lon=44.39, lat=35.47, pic="derrick", big="OIL", small="4 PROVINCES",
         head="Baghdad orders takeover of Kurdish-run oilfields",
         dek="PM al-Zaidi also seizes border posts.",
         brief=("Iraq", "Baghdad seizes Kurdish oilfields"), src="Reuters"),
    dict(region="ea", place="HANOI, VIETNAM", field="DISASTER", tag="CONFIRMED",
         lon=105.85, lat=21.03, pic="blast", big="7 DEAD", small="GAS BLAST",
         head="Gas blast wrecks a busy Hanoi restaurant",
         dek="It went off at about 8am local time.",
         brief=("Hanoi", "restaurant gas blast kills 7"), src="VnExpress · Al Jazeera"),
]

# The short list: (region, place, line, tag, source).
BRIEFS = [
    ("eu", "Russia", "Putin vows to retaliate", "OFFICIAL", "Reuters"),
    ("eu", "EU", "to cap Chinese hybrid car imports", "OFFICIAL", "The Guardian"),
    ("eu", "Chess", "world title game 1 drawn", "CONFIRMED", "The Guardian"),
    ("eu", "Tennis", "Sinner has knee surgery", "OFFICIAL", "The Guardian"),
    ("eu", "UK", "2 held after royal home break-in", "OFFICIAL", "Norfolk Police"),
    ("eu", "Football", "Real Madrid beat PSV 5–1", "CONFIRMED", "AFP · The Guardian"),
    ("me", "Turkey", "army helicopter crash kills 5", "CONFIRMED", "AP · Al Jazeera"),
    ("me", "Ankara", "Libya's Haftar meets Erdogan", "CONFIRMED", "Al Jazeera"),
    ("af", "DR Congo", "rebels halt their advance", "OFFICIAL", "Al Jazeera · Anadolu"),
    ("af", "Cameroon", "rebel chief on trial in Oslo", "CONFIRMED", "AFP · EPA"),
    ("af", "Mali", "leak: 349 Russian fighters killed", "REPORTED", "The Guardian"),
    ("sa", "Bangladesh", "Hasina to return 16 Dec", "OFFICIAL", "Reuters · Al Jazeera"),
    ("sa", "Bangladesh", "481 factories halted", "CONFIRMED", "TBS · Daily Star"),
    ("sa", "Cricket", "teen hits 204 off 53 balls", "CONFIRMED", "The Guardian · Al Jazeera"),
    ("sa", "Pakistan", "1st astronaut set to fly", "OFFICIAL", "CMSA · Al Jazeera"),
    ("ea", "Malaysia", "to deport 6,800 to Myanmar", "OFFICIAL", "Al Jazeera · Reuters"),
    ("ea", "China", "orders 50 Boeing 737 jets", "OFFICIAL", "Reuters"),
    ("oc", "Australia", "5% fines for tech giants", "OFFICIAL", "Al Jazeera · AAP"),
    ("oc", "Cricket", "England crush Australia in T20", "CONFIRMED", "The Guardian"),
    ("na", "US", "Giuliani gets Medal of Freedom", "CONFIRMED", "The Guardian"),
    ("na", "US", "Abrego Garcia leaves for Spain", "CONFIRMED", "The Guardian · DHS"),
    ("na", "US", "Meghan's father indicted", "OFFICIAL", "The Guardian"),
    ("na", "Iowa", "Army to blow up 4t of explosive", "OFFICIAL", "Al Jazeera"),
    ("na", "Canada", "rebuffs Pentagon memo", "OFFICIAL", "The Guardian"),
    ("la", "Colombia", "car bomb hurts 23 in Meta", "CONFIRMED", "Al Jazeera"),
    ("la", "Cartagena", "20 freed in hostage-taking", "CONFIRMED", "Al Jazeera"),
    ("la", "Cuba", "life expectancy falls, WHO says", "OFFICIAL", "WHO · The Guardian"),
    ("la", "Football", "Copa América 2028 to US", "OFFICIAL", "Conmebol · Concacaf"),
    ("gl", "UN", "5 women killed by kin every hour", "OFFICIAL", "UN Women"),
    ("gl", "Landmines", "casualties at 5-year high", "OFFICIAL", "Landmine Monitor"),
]

# "In numbers": short-list stories lifted into big type. A variant that shows the strip takes them out of the
# short list, so each story still appears once. (number, what it counts, region, the brief it replaces)
NUMBERS = [
    ("204", "runs off 53 balls by India's Sooryavanshi, 15", "sa", "teen hits 204 off 53 balls"),
    ("481", "garment factories halted in Bangladesh", "sa", "481 factories halted"),
    ("6,800", "people Malaysia will send back to Myanmar", "ea", "to deport 6,800 to Myanmar"),
    ("50", "Boeing 737s ordered by China's Xiamen Airlines", "ea", "orders 50 Boeing 737 jets"),
    ("5%", "of global revenue: Australia's new tech fines", "oc", "5% fines for tech giants"),
    ("349", "Russian fighters killed in Mali, leak shows", "af", "leak: 349 Russian fighters killed"),
]

# The fields the stories cover (each one has at least one story on the page).
FIELDS = ["politics", "courts", "war", "tech", "business", "sport", "security", "health", "disasters", "energy",
          "trade", "aviation", "space", "migration", "crime", "labour", "rights"]

# The day as it moved round the world, east to west (places, not clock times).
TIMELINE = [
    ("Seoul", "alert"),
    ("Hanoi", "blast"),
    ("Riyadh", "drone"),
    ("Zaporizhzhia", "raid"),
    ("Paris", "$41bn deal"),
    ("Brooklyn", "Huawei guilty"),
]

# Reported before Tuesday, so left off (shown in the date check).
LEFT_OUT = [
    ("Mon 23 Nov", "Huang reinstated as Nvidia CEO, Guterres's AI call, Trump's hush-money appeal"),
    ("Sun 22 Nov", "COP31 ends without a deal"),
    ("Fri 20 Nov", "Mexico captures “El Chapo Isidro”"),
]
