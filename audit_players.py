import json
from pathlib import Path

# Load parsed excel rows
with open('parsed_excel_rows.json', 'r', encoding='utf-8') as f:
    rows = json.load(f)

base_dir = Path("D:/Case/informals")
no_bg_dir = base_dir / "no_bg"

no_bg_files = {f.name.lower(): f.name for f in no_bg_dir.glob("*.png")}
jpeg_files = {f.name.lower(): f.name for f in base_dir.glob("*.jpeg")}

print(f"Total no_bg png files: {len(no_bg_files)}")
print(f"Total jpeg files: {len(jpeg_files)}")

# Print all player names in Excel
excel_players = []
for r in rows[1:]:
    if len(r) >= 2 and r[1]:
        excel_players.append((r[1], r[3], r[4], r[5], r[6]))

print(f"Total rows in Excel: {len(excel_players)}")

# Check unmatched
for name, nation, pos, rating, league in excel_players:
    clean = name.strip()
    # Check if image exists
    found_png = None
    found_jpg = None
    
    for k, v in no_bg_files.items():
        stem = Path(v).stem.lower().strip()
        if stem == clean.lower() or stem in clean.lower() or clean.lower() in stem:
            found_png = v
            break
            
    for k, v in jpeg_files.items():
        stem = Path(v).stem.lower().strip()
        if stem == clean.lower() or stem in clean.lower() or clean.lower() in stem:
            found_jpg = v
            break
            
    print(f"Player: '{name}' | Nation: '{nation}' | PNG: {found_png} | JPG: {found_jpg}")
