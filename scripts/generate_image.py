import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

def generate_image(prompt, output_file, model_name="gemini-3-pro-image-preview"):
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        return

    client = genai.Client(api_key=api_key)
    
    print(f"Generating image for prompt: '{prompt}'...")
    print(f"Using model: {model_name}")
    
    try:
        response = client.models.generate_content(
            model=model_name,
            contents=[prompt],
        )
        
        image_saved = False
        
        if response.parts:
            for part in response.parts:
                if part.inline_data:
                    # Try using as_image() if available, otherwise handle bytes manually
                    if hasattr(part, 'as_image'):
                        try:
                            img = part.as_image()
                            img.save(output_file)
                            print(f"Success! Image saved to {output_file}")
                            image_saved = True
                            break
                        except Exception as e:
                            print(f"Error using as_image(): {e}")
                    
                    # Fallback to direct bytes handling
                    if not image_saved:
                        try:
                            img_data = part.inline_data.data
                            # img_data might be bytes or base64 string depending on SDK version
                            # usually it's bytes in the new SDK
                            img = Image.open(io.BytesIO(img_data))
                            img.save(output_file)
                            print(f"Success! Image saved to {output_file}")
                            image_saved = True
                            break
                        except Exception as e:
                            print(f"Error processing inline data bytes: {e}")
                            
        if not image_saved:
            print("No image found in response.")
            # print(response) # Debugging

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Tip: Verify your API key and model availability.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image using Google Gemini 2.5 Flash Image")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("--output", "-o", default="generated_image.png", help="Output filename")
    parser.add_argument("--model", "-m", default="gemini-3-pro-image-preview", help="Model name to use")
    
    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.model)
