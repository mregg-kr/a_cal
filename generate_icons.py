import os
from PIL import Image, ImageDraw

source_image_path = r"C:\Users\cityt\.gemini\antigravity-ide\brain\68080832-dbae-435a-9016-04d54cf3481c\calculator_app_icon_1780816329449.png"
output_res_dir = r"c:\Vibe Coding\acalcu\app\src\main\res"

# Standard sizes for Android mipmaps
sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192
}

def create_circular_icon(img):
    # Create mask for circular icon
    width, height = img.size
    mask = Image.new('L', (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    
    # Put transparency inside circle bounds
    circular_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    circular_img.paste(img, (0, 0), mask=mask)
    return circular_img

def main():
    if not os.path.exists(source_image_path):
        print(f"Error: Source image not found at {source_image_path}")
        return

    # Load source image
    img = Image.open(source_image_path).convert("RGBA")
    
    # Generate circular version of the full-res image
    circular_img = create_circular_icon(img)
    
    for folder, size in sizes.items():
        folder_path = os.path.join(output_res_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        
        # Resize standard icon
        resized_img = img.resize((size, size), Image.Resampling.LANCZOS)
        resized_img.save(os.path.join(folder_path, "ic_launcher.png"), "PNG")
        
        # Resize circular icon
        resized_circular_img = circular_img.resize((size, size), Image.Resampling.LANCZOS)
        resized_circular_img.save(os.path.join(folder_path, "ic_launcher_round.png"), "PNG")
        
        print(f"Generated icons in {folder} (Size: {size}x{size})")

if __name__ == "__main__":
    main()
