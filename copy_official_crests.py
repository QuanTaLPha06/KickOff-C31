import shutil
import os
from pathlib import Path

base_dir = Path("D:/Case/informals")

# Copy Bayern Munich official logo to clean name
bayern_files = [f for f in os.listdir(base_dir) if "Bayern" in f]
print("Found Bayern files:", [f.encode('ascii', 'ignore').decode('ascii') for f in bayern_files])

for f in bayern_files:
    src = base_dir / f
    dst = base_dir / "FC_Bayern_Munchen_official.svg"
    shutil.copy(src, dst)
    print(f"Copied {f.encode('ascii', 'ignore').decode('ascii')} -> FC_Bayern_Munchen_official.svg")

# Verify real_madrid.jpeg
rm_file = base_dir / "real_madrid.jpeg"
print("real_madrid.jpeg exists:", rm_file.exists())
