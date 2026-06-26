from openai import OpenAI

client=OpenAI(api_key="sk-proj-")
file=open("meeting.txt")
meeting_text=file.read()

print(meeting_text)

