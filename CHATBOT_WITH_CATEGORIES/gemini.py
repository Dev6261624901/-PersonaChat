import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables!")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")

def chat_with_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("models/gemini-1.5-pro")
    response = model.generate_content(prompt)
    return response.text