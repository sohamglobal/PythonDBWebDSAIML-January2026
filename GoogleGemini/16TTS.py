import os
from google import genai
from google.genai import types

client = genai.Client()

# Ask for the output to be strictly audio instead of text
config = types.GenerateContentConfig(
    response_modalities=["AUDIO"]
)

print("Generating audio story...")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents="Tell a 3-sentence scary story about a ghost.",
    config=config
)

# Extract the raw audio bytes from the response parts
audio_bytes = None
for part in response.candidates[0].content.parts:
    if part.inline_data:
        audio_bytes = part.inline_data.data

if audio_bytes:
    # Save the binary audio data to a file
    with open("scary_story.mp3", "wb") as f:
        f.write(audio_bytes)
    print("Success! 'scary_story.mp3' has been created.")
else:
    print("Could not extract audio data.")