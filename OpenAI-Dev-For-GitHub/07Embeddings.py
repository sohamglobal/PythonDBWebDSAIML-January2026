from openai import OpenAI

client=OpenAI(api_key="sk-proj-")

sentences=[
    "I love Python programming",
    "Python is the best for AI",
    "I don't enjoy cooking food"
]

embeddings=[
    client.embeddings.create(
        model="text-embedding-3-small",
        input=s
    ).data[0].embedding
    for s in sentences
]

print("Embeddings : ",embeddings)
print("Embedding size :",len(embeddings[0]))