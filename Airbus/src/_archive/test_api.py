import os
from dotenv import load_dotenv
from openai import OpenAI

# Load variables from .env
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("LLM_BINDING_API_KEY"),
    base_url=os.getenv("LLM_BINDING_HOST")
)

# Send a very small test request
response = client.chat.completions.create(
    model=os.getenv("LLM_MODEL"),
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Say exactly: LightRAG connection works!"
        }
    ]
)

print("MODEL:", os.getenv("LLM_MODEL"))
print("RESPONSE:", response.choices[0].message.content)