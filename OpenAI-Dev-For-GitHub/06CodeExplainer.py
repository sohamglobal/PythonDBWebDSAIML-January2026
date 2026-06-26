from openai import OpenAI

client=OpenAI(api_key="sk-proj-")

code_snippet="""
List<String> lst=new ArrayList<>();
lst.add("Praffull");
lst.add("Sharayu");
lst.stream().forEach(System.out::println);
"""

response=client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role":"system","content":"You are an experienced Java trainer"},
        {"role":"user","content":f"Explain this code line by line :\n {code_snippet} "}
    ]
)

print(response.choices[0].message.content)