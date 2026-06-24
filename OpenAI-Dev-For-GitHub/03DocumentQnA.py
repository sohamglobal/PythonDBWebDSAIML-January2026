from openai import OpenAI

client=OpenAI(api_key="sk-proj-")

file=open("sohamglobal.txt","r")
document=file.read()
question=input('Enter your query : ')

response= client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":"you are a helpful assistant"},
        {"role":"user","content":f"Answer the question {question} strictly and only from the document {document} in one line. if the information is not found say - sorry i cant answer this"}
    ],
)

print(response.choices[0].message.content)

