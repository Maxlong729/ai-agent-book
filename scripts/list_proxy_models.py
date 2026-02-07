import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def list_models():
    api_key = os.environ.get("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL")
    
    if not api_key:
        print("Error: OPENAI_API_KEY not found.")
        return

    print(f"Connecting to: {base_url}")
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    try:
        models = client.models.list()
        # Sort models by id
        sorted_models = sorted(models.data, key=lambda x: x.id)
        
        print(f"\nSuccessfully retrieved {len(sorted_models)} models.")
        print("-" * 50)
        
        # Categorize for better display
        categories = {
            "GPT (OpenAI)": ["gpt", "dall-e", "o1"],
            "Claude (Anthropic)": ["claude"],
            "Gemini (Google)": ["gemini"],
            "DeepSeek": ["deepseek"],
            "Midjourney/Flux": ["mj", "flux", "midjourney"],
            "Other": []
        }
        
        categorized = {k: [] for k in categories}
        
        for model in sorted_models:
            found = False
            for cat, keywords in categories.items():
                if any(k in model.id.lower() for k in keywords):
                    categorized[cat].append(model.id)
                    found = True
                    break
            if not found:
                categorized["Other"].append(model.id)
        
        for cat, model_ids in categorized.items():
            if model_ids:
                print(f"\n[{cat}]")
                for mid in model_ids:
                    print(f"  - {mid}")
                    
    except Exception as e:
        print(f"Error listing models: {e}")

if __name__ == "__main__":
    list_models()
