# pip install openai

from openai import OpenAI

client=OpenAI(api_key="sk-proj-")

response= client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":"you are a history teacher"},
        {"role":"user","content":"give me 5 lines of information about world war 2"}
    ],
)

#print(response)
print(response.choices[0].message.content)