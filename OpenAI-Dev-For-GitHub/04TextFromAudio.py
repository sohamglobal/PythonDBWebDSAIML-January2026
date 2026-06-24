from openai import OpenAI

client=OpenAI(api_key="sk-proj-")

with open("granth.mp3","rb") as f:
    transcript=client.audio.transcriptions.create(
        file=f,
        model="gpt-4o-transcribe"
    )

print("text extracted :",transcript.text)