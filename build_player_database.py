import openpyxl
import os
import json
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

excel_path = r'C:\Users\Kevin Gandhi\Downloads\Auction Names.xlsx'
wb = openpyxl.load_workbook(excel_path)
sheet = wb.active

base_dir = Path("D:/Case/informals")
no_bg_dir = base_dir / "no_bg"

informals_files = [f for f in os.listdir(base_dir) if os.path.isfile(base_dir / f)]
no_bg_files = [f for f in os.listdir(no_bg_dir) if os.path.isfile(no_bg_dir / f)] if no_bg_dir.exists() else []

def clean_str(s):
    return re.sub(r'[^a-z0-9]', '', str(s).lower())

jpeg_stems = {clean_str(Path(f).stem): f for f in informals_files if f.lower().endswith(('.jpeg', '.jpg', '.png')) and not f.startswith('Flag') and not f.startswith('LaLiga') and not f.startswith('Premier') and not f.endswith('logo.svg')}
nobg_stems = {clean_str(Path(f).stem): f for f in no_bg_files if f.lower().endswith(('.jpeg', '.jpg', '.png'))}

ALIASES = {
    'alisson': 'alison',
    'mohamed salah': 'mohammed salah',
    'mohamad salah': 'mohammed salah',
    'frenkie de jong': 'frankie de jong',
    'federico valverde': 'frederico valverde',
    'martin odegaard': 'martin odegard',
    'khvicha kvaratskhelia': 'kvicha kvaratskhelia',
    'dayot upamecano': 'dayot upamecano',
    'jonathan tah': 'jonnathan tah',
    'youri tielemans': 'youri tielmans',
    'trent alexander-arnold': 'trent alexander arnorld',
    'alessandro bastoni': 'bastoni',
    'antonio rudiger': 'rudiger',
    'declan rice': 'rice',
    'sandro tonali': 'tonali',
    'julian alvarez': 'alvarez',
    'rodrygo': 'rodrygo goes',
    'ibrahima konate': 'ibrahim konate',
    'heung-min son': 'heung min son',
    'bryan mbeumo': 'bryan mbuemo',
    'kimmich': 'joshua kimmich',
    'nico schlotterbeck': 'schlotterbeck',
    'jules kounde': 'kounde',
    'josko gvardiol': 'gvardiol',
    'moises caicedo': 'caicedo',
    'ryan gravenberch': 'gravenberch',
    'tijjani reijnders': 'reijnders'
}

def find_best_image(excel_name):
    name_l = excel_name.strip().lower()
    target = ALIASES.get(name_l, name_l)
    target_clean = clean_str(target)
    
    j_file = jpeg_stems.get(target_clean)
    n_file = nobg_stems.get(target_clean)
    
    if not j_file or not n_file:
        words = name_l.split()
        if len(words) > 1:
            last_word_clean = clean_str(words[-1])
            j_file = j_file or jpeg_stems.get(last_word_clean)
            n_file = n_file or nobg_stems.get(last_word_clean)
            
    if not j_file:
        j_file = f"{excel_name}.jpeg"
    if not n_file:
        n_file = f"{excel_name}.png"
        
    return j_file, n_file

FLAG_MAP = {
    'ARGENTINA': 'Flag_of_Argentina.svg',
    'BELGIUM': 'Flag_of_Belgium.svg',
    'BRAZIL': 'Flag_of_Brazil.svg',
    'CAMEROON': 'Flag_of_Cameroon.svg',
    'CANADA': 'Flag_of_Canada_(Pantone).svg',
    'COLOMBIA': 'Flag_of_Colombia.svg',
    'CROATIA': 'Flag_of_Croatia.svg',
    'ECUADOR': 'Flag_of_Ecuador.svg',
    'EGYPT': 'Flag_of_Egypt.svg',
    'ENGLAND': 'Flag_of_England.svg',
    'FRANCE': 'Flag_of_France.svg',
    'GEORGIA': 'Flag_of_Georgia.svg',
    'GERMANY': 'Flag_of_Germany.svg',
    'ITALY': 'Flag_of_Italy.svg',
    'MOROCCO': 'Flag_of_Morocco.svg',
    'NETHERLANDS': 'Flag_of_the_Netherlands.svg',
    'NIGERIA': 'Flag_of_Nigeria.svg',
    'NORWAY': 'Flag_of_Norway.svg',
    'POLAND': 'Flag_of_Poland.svg',
    'PORTUGAL': 'Flag_of_Portugal_(official).svg',
    'SCOTLAND': 'Flag_of_Scotland.svg',
    'SENEGAL': 'Flag_of_Senegal.svg',
    'SLOVENIA': 'Flag_of_Slovenia.svg',
    'SOUTH KOREA': 'Flag_of_South_Korea.svg',
    'SPAIN': 'Flag_of_the_Kingdom_of_Spain.svg',
    'SWEDEN': 'Flag_of_Sweden.svg',
    'USA': 'Flag_of_the_United_States_(DDD-F-416E_specifications).svg',
    'URUGUAY': 'Flag_of_Uruguay.svg'
}

LEAGUE_MAP = {
    'BUNDESLIGA': 'Bundesliga_logo_(2017).svg',
    'LALIGA': 'LaLiga_EA_Sports_2023_Vertical_Logo.svg',
    'LIGUE 1': 'Logo_Ligue_1_McDonald_s_2024.svg',
    'MLS': 'Major_League_Soccer_logo.svg',
    'PREMIER LEAGUE': 'Premier_League_Logo.svg',
    'SAUDI PRO LEAGUE': 'Roshn_Saudi_League_Logo.svg',
    'SERIE A': 'Serie_A_ENILIVE_logo.svg',
    'SÜPER LIG': 'Turkish_Süper_Lig_logo_(2024).svg',
    'TURKISH SÜPER LIG': 'Turkish_Süper_Lig_logo_(2024).svg',
    'SUPER LIG': 'Turkish_Süper_Lig_logo_(2024).svg',
    'TURKISH SUPER LIG': 'Turkish_Süper_Lig_logo_(2024).svg'
}

CLUB_MAP = {
    'AC MILAN': 'AC_Milan_logo.svg',
    'AL ITIHAD': 'Al-Ittihad_Club_(Jeddah)_logo.svg',
    'AL-ITTIHAD': 'Al-Ittihad_Club_(Jeddah)_logo.svg',
    'AL ITTIHAD': 'Al-Ittihad_Club_(Jeddah)_logo.svg',
    'AL NASSER': 'Al_Nassr_FC_logo.svg',
    'AL NASSR': 'Al_Nassr_FC_logo.svg',
    'AL HILAL': 'Al_Hilal_SFC_Logo.svg',
    'ARSENAL': 'Arsenal_FC.svg',
    'ASTON VILLA': 'Aston_Villa_FC_logo.svg',
    'ATHLETIC BILBAO': 'Club_Athletic_Bilbao_logo.svg',
    'ATLETICO MADRID': 'Atletico_Madrid_Logo_2024.svg',
    'BARCELONA': 'FC_Barcelona_(crest).svg',
    'BAYERN': 'FC_Bayern_Munchen_logo.svg',
    'BAYERN MUNICH': 'FC_Bayern_Munchen_logo.svg',
    'CHELSEA': 'Chelsea_FC.svg',
    'DORTMUND': 'Borussia_Dortmund_logo.svg',
    'GALATASARAY': 'Galatasaray_SK_logo.svg',
    'INTER MIAMI': 'Inter_Miami_CF_logo.svg',
    'INTER MILAN': 'FC_Internazionale_Milano_2021.svg',
    'JUVENTUS': 'Juventus_FC_logo.svg',
    'LAFC': 'LAFC_logo.svg',
    'LIVERPOOL': 'Liverpool_FC.svg',
    'MANCHESTER CITY': 'Manchester_City_FC.svg',
    'MANCHESTER UNITED': 'Manchester_United_FC.svg',
    'NAPOLI': 'SSC_Napoli_logo.svg',
    'NEWCASTLE': 'Newcastle_United_logo.svg',
    'PSG': 'PSG_logo.svg',
    'REAL MADRID': 'Real_Madrid_logo.svg',
    'ROMA': 'AS_Roma_logo_(2017).svg'
}

rows = [list(r) for r in sheet.iter_rows(values_only=True) if any(r)]
data_rows = rows[1:]

players = []
for idx, r in enumerate(data_rows, 1):
    while len(r) < 8:
        r.append('')
        
    category, name, base_price, nation, pos2, rating, league, club = r[:8]
    category = str(category).strip()
    name = str(name).strip()
    base_price = str(base_price).strip()
    nation = str(nation).strip()
    pos2 = str(pos2).strip()
    try:
        rating = int(rating) if str(rating).isdigit() else int(float(rating))
    except Exception:
        rating = 85
        
    league = str(league).strip()
    club = str(club).strip()
    
    jpeg_file, nobg_file = find_best_image(name)
    flag_file = FLAG_MAP.get(nation.upper(), 'Flag_of_England.svg')
    league_file = LEAGUE_MAP.get(league.upper(), 'Premier_League_Logo.svg')
    club_file = CLUB_MAP.get(club.upper(), 'Premier_League_Logo.svg')
    
    players.append({
        "id": f"p_{idx}",
        "name": name,
        "category": category,
        "basePrice": base_price,
        "nation": nation.upper(),
        "flagImg": flag_file,
        "pos": pos2.upper(),
        "rating": rating,
        "club": club.upper(),
        "clubImg": club_file,
        "league": league.upper(),
        "leagueImg": league_file,
        "cardImg": f"no_bg/{nobg_file}",
        "image": jpeg_file,
        "noBgImage": f"no_bg/{nobg_file}",
        "flag": flag_file,
        "clubLogo": club_file,
        "leagueLogo": league_file
    })

print(f"Generated {len(players)} player records.")

js_content = f"// Comprehensive EA FC Player Database generated from spreadsheet\nconst PLAYERS_DATABASE = {json.dumps(players, indent=4)};\nconst playersData = PLAYERS_DATABASE;\n\nif (typeof module !== 'undefined' && module.exports) {{\n    module.exports = PLAYERS_DATABASE;\n}}\n"

js_path = base_dir / "players_data.js"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Saved {len(players)} players to {js_path}")
