from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder(text, output_file):
    width, height = 1024, 1024
    image = Image.new('RGB', (width, height), color=(240, 240, 240))
    draw = ImageDraw.Draw(image)
    
    # Try to load a font, otherwise use default
    try:
        font = ImageFont.truetype("Arial", 40)
    except IOError:
        font = ImageFont.load_default()

    # Calculate text position (approximate centering)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    
    draw.text((x, y), text, fill=(255, 0, 0), font=font)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    image.save(output_file)
    print(f"Created placeholder image at {output_file}")

if __name__ == "__main__":
    create_placeholder("Image Generation Failed:\nQuota Exceeded for API Key", "manuscript/images/chapter1_workflow_factory.png")
