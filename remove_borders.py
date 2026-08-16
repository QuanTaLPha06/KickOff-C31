import os
import sys
from pathlib import Path
from PIL import Image

try:
    from rembg import new_session, remove
    HAS_REMBG = True
except ImportError:
    HAS_REMBG = False

def crop_and_transparentize_black_borders(src_path, dst_path):
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    pix = img.load()
    
    # Simple threshold to find non-black bounding box & make outer black transparent
    min_x, min_y, max_x, max_y = w, h, 0, 0
    
    # We can check pixels
    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            # Dark threshold: max(r,g,b) < 30
            if r < 28 and g < 28 and b < 28:
                pix[x, y] = (0, 0, 0, 0)
            else:
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x < max_x and min_y < max_y:
        # Crop to bounding box with 2px margin
        crop_box = (max(0, min_x - 2), max(0, min_y - 2), min(w, max_x + 3), min(h, max_y + 3))
        cropped = img.crop(crop_box)
        cropped.save(dst_path, format="PNG", compress_level=6)
    else:
        img.save(dst_path, format="PNG", compress_level=6)

def main():
    folder = Path("D:/Case/informals")
    out_dir = folder / "no_bg"
    out_dir.mkdir(parents=True, exist_ok=True)
    
    jpeg_files = sorted(list(folder.glob("*.jpeg")) + list(folder.glob("*.jpg")))
    print(f"Found {len(jpeg_files)} image files.")
    
    session = None
    if HAS_REMBG:
        print("rembg is installed! Loading model...")
        try:
            session = new_session("birefnet-general")
        except Exception as e:
            try:
                session = new_session("u2net")
            except Exception as e2:
                session = None

    for f in jpeg_files:
        if f.name.lower() in ["background.jpeg", "tunnel_bg.jpeg"]:
            continue
            
        dst = out_dir / f"{f.stem}.png"
        
        processed = False
        if session is not None:
            try:
                img = Image.open(f).convert("RGBA")
                res = remove(img, session=session)
                res.save(dst, format="PNG", compress_level=6)
                processed = True
                print(f" [rembg] {f.name} -> {dst.name}")
            except Exception as e:
                print(f" [rembg error on {f.name}]: {e}")
        
        if not processed:
            try:
                crop_and_transparentize_black_borders(f, dst)
                print(f" [PIL crop] {f.name} -> {dst.name}")
            except Exception as e:
                print(f" [Error on {f.name}]: {e}")

    print("Finished processing all player cards!")

if __name__ == "__main__":
    main()
