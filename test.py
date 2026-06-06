from src.config import client

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain transformers in one paragraph."
)

print(response.text)