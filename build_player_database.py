import json
from pathlib import Path

# Load parsed excel rows
with open('parsed_excel_rows.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

base_dir = Path("D:/Case/informals")
no_bg_dir = base_dir / "no_bg"

# SVG Flag Mapping for all Nations
FLAG_MAP = {
    "ARGENTINA": "Flag_of_Argentina.svg",
    "BELGIUM": "Flag_of_Belgium.svg",
    "BRAZIL": "Flag_of_Brazil.svg",
    "CAMEROON": "Flag_of_Cameroon.svg",
    "CANADA": "Flag_of_Canada_(Pantone).svg",
    "COLOMBIA": "Flag_of_Colombia.svg",
    "CÔTE D'IVOIRE": "Flag_of_Côte_d_Ivoire.svg",
    "IVORY COAST": "Flag_of_Côte_d_Ivoire.svg",
    "CROATIA": "Flag_of_Croatia.svg",
    "ECUADOR": "Flag_of_Ecuador.svg",
    "EGYPT": "Flag_of_Egypt.svg",
    "ENGLAND": "Flag_of_England.svg",
    "FRANCE": "Flag_of_France.svg",
    "GEORGIA": "Flag_of_Georgia.svg",
    "GERMANY": "Flag_of_Germany.svg",
    "ITALY": "Flag_of_Italy.svg",
    "MOROCCO": "Flag_of_Morocco.svg",
    "NORWAY": "Flag_of_Norway.svg",
    "POLAND": "Flag_of_Poland.svg",
    "PORTUGAL": "Flag_of_Portugal_(official).svg",
    "SCOTLAND": "Flag_of_Scotland.svg",
    "SENEGAL": "Flag_of_Senegal.svg",
    "SLOVENIA": "Flag_of_Slovenia.svg",
    "SOUTH KOREA": "Flag_of_South_Korea.svg",
    "SWEDEN": "Flag_of_Sweden.svg",
    "TURKEY": "Flag_of_Turkey.svg",
    "URUGUAY": "Flag_of_Uruguay.svg",
    "SPAIN": "Flag_of_the_Kingdom_of_Spain.svg",
    "NETHERLANDS": "Flag_of_the_Netherlands.svg",
    "USA": "Flag_of_the_United_States_(DDD-F-416E_specifications).svg"
}

LEAGUE_MAP = {
    "LALIGA": "LaLiga_EA_Sports_2023_Vertical_Logo.svg",
    "PREMIER LEAGUE": "Premier_League_Logo.svg",
    "SERIE A": "Serie_A_ENILIVE_logo.svg",
    "LIGUE 1": "Logo_Ligue_1_McDonald_s_2024.svg",
    "BUNDESLIGA": "Bundesliga_logo_(2017).svg",
    "SAUDI PRO LEAGUE": "Roshn_Saudi_League_Logo.svg",
    "MLS": "Major_League_Soccer_logo.svg",
    "SÜPER LIG": "Turkish_Su%CC%88per_Lig_logo_(2024).svg",
    "EREDIVISIE": "VriendenLoterij_Eredivisie_Logo.png"
}

# Explicit Player -> (Card PNG, Club Name, Club Crest SVG/JPEG)
CARD_EXACT_MAP = {
    # Goalkeepers
    "THIBAUT COURTOIS": ("no_bg/Thibaut Courtois.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "GIANLUIGI DONNARUMMA": ("no_bg/Gianluigi Donnarumma.png", "PSG", "PSG_logo.svg"),
    "ALISSON": ("no_bg/Alison.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "JAN OBLAK": ("no_bg/Jan Oblak.png", "ATLETICO MADRID", "Atletico_Madrid_Logo_2024.svg"),
    "MIKE MAIGNAN": ("no_bg/Mike Maignan.png", "AC MILAN", "AC_Milan_logo.svg"),
    "DAVID RAYA": ("no_bg/David Raya.png", "ARSENAL", "Arsenal_FC.svg"),

    # Centre Backs
    "VIRGIL VAN DIJK": ("no_bg/Virgil Van Dijk.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "WILLIAM SALIBA": ("no_bg/William Saliba.png", "ARSENAL", "Arsenal_FC.svg"),
    "GABRIEL": ("no_bg/Gabriel.png", "ARSENAL", "Arsenal_FC.svg"),
    "ALESSANDRO BASTONI": ("no_bg/Bastoni.png", "INTER MILAN", "FC_Internazionale_Milano_2021.svg"),
    "RUBEN DIAS": ("no_bg/Ruben Dias.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "MARQUINHOS": ("no_bg/Marquinhos .png", "PSG", "PSG_logo.svg"),
    "IBRAHIMA KONATE": ("no_bg/Ibrahim Konate.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "ANTONIO RUDIGER": ("no_bg/Rudiger.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "DAYOT UPAMECANO": ("no_bg/Dayot Upamecano.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "RONALD ARAUJO": ("no_bg/Ronald Araujo.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "JONATHAN TAH": ("no_bg/Jonnathan Tah.png", "BAYER LEVERKUSEN", "Bayer_Leverkusen_logo.svg"),
    "WILLIAM PACHO": ("no_bg/William Pacho.png", "PSG", "PSG_logo.svg"),
    "NICO SCHLOTTERBECK": ("no_bg/Schlotterbeck.png", "BORUSSIA DORTMUND", "Borussia_Dortmund_logo.svg"),
    "BREMER": ("no_bg/Bremer .png", "JUVENTUS", "Serie_A_ENILIVE_logo.svg"),
    "EDER MILITAO": ("no_bg/Eder Militao.png", "REAL MADRID", "Real_Madrid_logo.svg"),

    # Right Backs
    "ACHRAF HAKIMI": ("no_bg/Achraf Hakimi.png", "PSG", "PSG_logo.svg"),
    "TRENT ALEXANDER-ARNOLD": ("no_bg/Trent Alexander Arnorld.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "JULES KOUNDE": ("no_bg/Kounde.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "JEREMIE FRIMPONG": ("no_bg/Jeremie Frimpong.png", "BAYER LEVERKUSEN", "Bayer_Leverkusen_logo.svg"),
    "DENZEL DUMFRIES": ("no_bg/Denzel Dumfries.png", "INTER MILAN", "FC_Internazionale_Milano_2021.svg"),
    "MARCOS LLORENTE": ("no_bg/Marcos Llorente.png", "ATLETICO MADRID", "Atletico_Madrid_Logo_2024.svg"),

    # Left Backs
    "NUNO MENDES": ("no_bg/Nuno Mendes.png", "PSG", "PSG_logo.svg"),
    "JOSKO GVARDIOL": ("no_bg/Gvardiol.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "ALPHONSO DAVIES": ("no_bg/Alphonso Davies.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "THEO HERNANDEZ": ("no_bg/Theo Hernandez.png", "AC MILAN", "AC_Milan_logo.svg"),
    "MARC CUCURELLA": ("no_bg/Marc Cucurella.png", "CHELSEA", "Chelsea_FC.svg"),
    "BALDE": ("no_bg/Balde.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),

    # CDMs
    "RODRI": ("no_bg/Rodri.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "KIMMICH": ("no_bg/Joshua Kimmich.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "DECLAN RICE": ("no_bg/Rice.png", "ARSENAL", "Arsenal_FC.svg"),
    "MOISES CAICEDO": ("no_bg/Caicedo.png", "CHELSEA", "Chelsea_FC.svg"),
    "SANDRO TONALI": ("no_bg/Tonali.png", "NEWCASTLE UNITED", "Newcastle_United_logo.svg"),
    "RYAN GRAVENBERCH": ("no_bg/Gravenberch.png", "LIVERPOOL", "Liverpool_FC.svg"),

    # CMs
    "PEDRI": ("no_bg/Pedri.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "KEVIN DE BRUYNE": ("no_bg/Kevin De Bruyne.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "FEDERICO VALVERDE": ("no_bg/Frederico Valverde.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "MARTIN ODEGAARD": ("no_bg/Martin Odegard.png", "ARSENAL", "Arsenal_FC.svg"),
    "BERNARDO SILVA": ("no_bg/Bernardo Silva.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "VITINHA": ("no_bg/Vitinha.png", "PSG", "PSG_logo.svg"),
    "FRENKIE DE JONG": ("no_bg/Frankie De Jong.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "NICOLO BARELLA": ("no_bg/Nicolo Barella.png", "INTER MILAN", "FC_Internazionale_Milano_2021.svg"),
    "BRUNO GUIMARAES": ("no_bg/Bruno Guimaraes.png", "NEWCASTLE UNITED", "Newcastle_United_logo.svg"),
    "JOAO NEVES": ("no_bg/Joao Neves.png", "PSG", "PSG_logo.svg"),
    "ALEXIS MAC ALLISTER": ("no_bg/Alexis Mac Allister.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "TIJJANI REIJNDERS": ("no_bg/Reijnders.png", "AC MILAN", "AC_Milan_logo.svg"),
    "ENZO FERNANDEZ": ("no_bg/Enzo Fernandez.png", "CHELSEA", "Chelsea_FC.svg"),
    "SCOTT MCTOMINAY": ("no_bg/Scott Mctominay.png", "NAPOLI", "Serie_A_ENILIVE_logo.svg"),
    "YOURI TIELEMANS": ("no_bg/Youri tielmans .png", "ASTON VILLA", "Premier_League_Logo.svg"),

    # CAMs
    "JUDE BELLINGHAM": ("no_bg/Jude Bellingham.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "FLORIAN WIRTZ": ("no_bg/Florian Wirtz.png", "BAYER LEVERKUSEN", "Bayer_Leverkusen_logo.svg"),
    "JAMAL MUSIALA": ("no_bg/Jamal Musiala.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "BRUNO FERNANDES": ("no_bg/Bruno Fernandes.png", "MANCHESTER UNITED", "Manchester_United_FC.svg"),
    "COLE PALMER": ("no_bg/Cole Palmer.png", "CHELSEA", "Chelsea_FC.svg"),
    "PAULO DYBALA": ("no_bg/Paulo Dybala.png", "AS ROMA", "AS_Roma_logo_(2017).svg"),

    # Wingers
    "VINICIUS JR.": ("no_bg/Vinicius Jr.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "KHVICHA KVARATSKHELIA": ("no_bg/Kvicha Kvaratskhelia.png", "PSG", "PSG_logo.svg"),
    "RAPHINHA": ("no_bg/Raphinha.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "NICO WILLIAMS": ("no_bg/Nico Williams.png", "ATHLETIC BILBAO", "Club_Athletic_Bilbao_logo.svg"),
    "LUIS DIAZ": ("no_bg/Luis Diaz.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "HEUNG-MIN SON": ("no_bg/Heung Min Son.png", "TOTTENHAM", "Premier_League_Logo.svg"),
    "RAFAEL LEAO": ("no_bg/Rafael Leao.png", "AC MILAN", "AC_Milan_logo.svg"),
    "BRADLEY BARCOLA": ("no_bg/Bradley Barcola.png", "PSG", "PSG_logo.svg"),
    "CODY GAKPO": ("no_bg/Cody Gakpo.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "KINGSLEY COMAN": ("no_bg/Kingsley Coman.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "GABRIEL MARTINELLI": ("no_bg/Gabriel Martinelli.png", "ARSENAL", "Arsenal_FC.svg"),
    "ANTHONY GORDON": ("no_bg/Anthony Gordon.png", "NEWCASTLE UNITED", "Newcastle_United_logo.svg"),
    "SADIO MANE": ("no_bg/Sadio Mane.png", "AL-NASSR", "Al_Hilal_SFC_Logo.svg"),
    "LEANDRO TROSSARD": ("no_bg/Leandro Trossard.png", "ARSENAL", "Arsenal_FC.svg"),

    "MOHAMED SALAH": ("no_bg/Mohammed Salah.png", "LIVERPOOL", "Liverpool_FC.svg"),
    "LAMINE YAMAL": ("no_bg/Lamine Yamal.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "BUKAYO SAKA": ("no_bg/Bukayo Saka.png", "ARSENAL", "Arsenal_FC.svg"),
    "LIONEL MESSI": ("no_bg/Lionel Messi.png", "INTER MIAMI", "Inter_Miami_CF_logo.svg"),
    "MICHAEL OLISE": ("no_bg/Michael Olise.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "PHIL FODEN": ("no_bg/Phil Foden.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "DESIRE DOUE": ("no_bg/Desire Doue.png", "PSG", "PSG_logo.svg"),
    "RODRYGO": ("no_bg/Rodrygo Goes.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "BRYAN MBEUMO": ("no_bg/Bryan Mbuemo.png", "BRENTFORD", "Premier_League_Logo.svg"),
    "CHRISTIAN PULISIC": ("no_bg/Christian Pulisic.png", "AC MILAN", "AC_Milan_logo.svg"),
    "MOUSSA DIABY": ("no_bg/Moussa Diaby.png", "AL-ITTIHAD", "Al-Ittihad_Club_(Jeddah)_logo.svg"),
    "BRAHIM DIAZ": ("no_bg/Brahim Diaz.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "KARIM ADEYEMI": ("no_bg/Schlotterbeck.png", "BORUSSIA DORTMUND", "Borussia_Dortmund_logo.svg"),
    "LEROY SANE": ("no_bg/Leroy Sane.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "RAYAN CHERKI": ("no_bg/Rayan Cherki.png", "LYON", "Logo_Ligue_1_McDonald_s_2024.svg"),

    # Strikers
    "KYLIAN MBAPPE": ("no_bg/Kylian Mbappe.png", "REAL MADRID", "Real_Madrid_logo.svg"),
    "ERLING HAALAND": ("no_bg/Erling Haaland.png", "MANCHESTER CITY", "Manchester_City_FC.svg"),
    "HARRY KANE": ("no_bg/Harry Kane.png", "BAYERN MUNICH", "FC_Bayern_Munchen_logo.svg"),
    "OUSMANE DEMBELE": ("no_bg/Ousmane Dembele.png", "PSG", "PSG_logo.svg"),
    "LAUTARO MARTINEZ": ("no_bg/Lautaro Martinez.png", "INTER MILAN", "FC_Internazionale_Milano_2021.svg"),
    "ALEXANDER ISAK": ("no_bg/Alexander Isak.png", "NEWCASTLE UNITED", "Newcastle_United_logo.svg"),
    "VIKTOR GYOKERES": ("no_bg/Viktor Gyokeres.png", "SPORTING CP", "Premier_League_Logo.svg"),
    "JULIAN ALVAREZ": ("no_bg/Alvarez.png", "ATLETICO MADRID", "Atletico_Madrid_Logo_2024.svg"),
    "ROBERT LEWANDOWSKI": ("no_bg/Robert Lewandowski.png", "FC BARCELONA", "FC_Barcelona_(crest).svg"),
    "CRISTIANO RONALDO": ("no_bg/Cristiano Ronaldo.png", "AL-NASSR", "Al_Hilal_SFC_Logo.svg")
}

raw_players = []

for idx, r in enumerate(rows[1:], 1):
    if len(r) < 7 or not r[1]:
        continue

    cat = r[0].strip()
    name = r[1].strip()
    price = r[2].strip()
    nation = r[3].strip()
    pos = r[4].strip()
    rating = r[5].strip()
    league = r[6].strip()

    if "/" in name and "Sane" in name:
        raw_players.append({
            "cat": cat, "name": "Leroy Sane", "price": price,
            "nation": "Germany", "pos": "RW", "rating": "84", "league": "Bundesliga"
        })
        raw_players.append({
            "cat": cat, "name": "Rayan Cherki", "price": price,
            "nation": "France", "pos": "CAM", "rating": "85", "league": "Ligue 1"
        })
    else:
        raw_players.append({
            "cat": cat, "name": name, "price": price,
            "nation": nation, "pos": pos, "rating": rating, "league": league
        })

processed_players = []

for idx, p in enumerate(raw_players, 1):
    name_upper = p["name"].upper()
    nation_upper = p["nation"].upper()
    league_upper = p["league"].upper()

    try:
        rating_num = int(float(p["rating"]))
    except:
        rating_num = 85

    flag_file = FLAG_MAP.get(nation_upper, "Flag_of_Germany.svg")
    league_file = LEAGUE_MAP.get(league_upper, "Premier_League_Logo.svg")

    card_info = CARD_EXACT_MAP.get(name_upper)
    if card_info:
        card_img, club_name, club_img = card_info
    else:
        card_img = "assets/courtois_card.jpeg"
        club_name = league_upper
        club_img = league_file

    player_obj = {
        "id": f"p_{idx}",
        "name": p["name"],
        "category": p["cat"],
        "basePrice": p["price"] if p["price"] else "₹5M",
        "nation": nation_upper,
        "flagImg": flag_file,
        "pos": p["pos"],
        "rating": rating_num,
        "club": club_name,
        "clubImg": club_img,
        "league": league_upper,
        "leagueImg": league_file,
        "cardImg": card_img
    }
    processed_players.append(player_obj)

print(f"Total clean players: {len(processed_players)}")

js_content = f"// Comprehensive EA FC Player Database generated from spreadsheet\nconst PLAYERS_DATABASE = {json.dumps(processed_players, indent=4, ensure_ascii=False)};\n"

with open("players_data.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Updated players_data.js successfully!")
