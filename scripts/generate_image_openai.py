import os
import argparse
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_image(prompt, output_file, model="dall-e-3", size="1024x1024"):
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        return

    print(f"Initializing OpenAI client with base_url: {base_url if base_url else 'default'}")
    
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    print(f"Generating image for prompt: '{prompt}'...")
    print(f"Using model: {model}")
    
    try:
        response = client.images.generate(
            model=model,
            prompt=prompt,
            size=size,  # Use variable size
            quality="standard",
            n=1,
        )
        
        # Debug: Print the first item in data to check structure if needed
        if not response.data:
            print("Error: No data in response.")
            print(response)
            return

        image_url = response.data[0].url
        print(f"Image generated at URL: {image_url}")
        
        if not image_url:
             print("Error: Image URL is None.")
             # Some providers return b64_json instead of url
             if hasattr(response.data[0], 'b64_json') and response.data[0].b64_json:
                 print("Found b64_json, decoding...")
                 import base64
                 img_data = base64.b64decode(response.data[0].b64_json)
                 with open(output_file, 'wb') as handler:
                    handler.write(img_data)
                 print(f"Success! Image saved to {output_file} (from base64)")
                 return
             print(response)
             return

        # Download the image
        img_data = requests.get(image_url).content
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        with open(output_file, 'wb') as handler:
            handler.write(img_data)
            
        print(f"Success! Image saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image using OpenAI DALL-E")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("--output", "-o", default="generated_image.png", help="Output filename")
    parser.add_argument("--model", "-m", default="dall-e-3", help="Model name to use")
    parser.add_argument("--size", "-s", default="1024x1024", help="Image size (e.g. 1024x1024, 1024x1792)")
    
    args = parser.parse_args()
    generate_image(args.prompt, args.output, args.model, args.size)
