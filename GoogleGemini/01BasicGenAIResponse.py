# pip install google-genai

from google import genai

client = genai.Client()
# it automatically picks the api key from the system variable

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in 3 lines",
)

print(response.text)