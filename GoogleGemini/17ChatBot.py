import os
from google import genai
from google.genai import types

client = genai.Client()

# System instructions completely alter how the model behaves
config = types.GenerateContentConfig(
    system_instruction="You are a core python trainer."
)

print("🏴‍☠️ Talk to the trainer! (Type 'quit' to exit)\n")

while True:
    user_message = input("You: ")
    if user_message.lower() == 'quit':
        break
        
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_message,
        config=config
    )
    
    print(f"\nTrainer: {response.text}\n")