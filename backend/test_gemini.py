import os
from dotenv import load_dotenv, find_dotenv
from google import genai
from google.genai import types

load_dotenv(find_dotenv())

key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")
print("Key loaded:", bool(key), "| Model:", model)

client = genai.Client(
    api_key=key,
    http_options=types.HttpOptions(timeout=30000),  # 30 seconds
)

try:
    response = client.models.generate_content(
        model=model,
        contents="Reply with one word: working",
    )
    print("Response:", response.text)
except Exception as e:
    print("FAILED:", type(e).__name__, "-", str(e)[:200])