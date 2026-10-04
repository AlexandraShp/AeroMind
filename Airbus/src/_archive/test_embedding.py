import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("EMBEDDING_BINDING_API_KEY"),
    base_url=os.getenv("EMBEDDING_BINDING_HOST")
)

response = client.embeddings.create(
    model=os.getenv("EMBEDDING_MODEL"),
    input="The Airbus A320 has several aircraft systems."
)

vector = response.data[0].embedding

print("Embedding model:", os.getenv("EMBEDDING_MODEL"))
print("Vector length:", len(vector))
print("First 5 values:", vector[:5])