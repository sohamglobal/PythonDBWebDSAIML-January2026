from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a teacher in a primary school. Help the students to learn in the easiest way",
    ),
    contents="Hello there"
)

print(response.text)

'''
You are a bank manager. Your job is to assist customers with their banking needs.
'''