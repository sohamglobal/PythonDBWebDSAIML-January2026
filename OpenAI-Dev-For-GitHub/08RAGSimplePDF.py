# pip install pymupdf
from openai import OpenAI
import fitz

client=OpenAI(api_key="sk-proj-")

def read_pdf(file_path):
    pdf=fitz.open(file_path)
    text=""
    for page in pdf:
        text+=page.get_text()
    
    return text

context=read_pdf("SohamGlobal-KB.pdf")
print(context)
print("PDF loaded successfully")

question=input("Ask Question : ")

prompt=f"""
You are an assistant.
Answer ONLY using the information given below.
If the answer is not prosent, say -
"I don't know"

Find answer of the question {question} in {context} and return
"""

response=client.responses.create(
    model="gpt-4o",
    input=prompt
)

print("Answer : \n")
print(response.output_text)