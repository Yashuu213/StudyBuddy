import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error listing models: {e}")
