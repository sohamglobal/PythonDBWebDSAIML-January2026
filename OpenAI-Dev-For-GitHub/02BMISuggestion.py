from openai import OpenAI
from datetime import date

client=OpenAI(api_key="sk-proj-")

def call_chatgpt(prompt):
    response=client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content.strip()


nm=input('Enter your name : ')
wt=input('Enter weight in kg : ')
ht=input('Enter height in meters : ')
today=date.today()

prompt=f'''
you are a fitness consultant.
take data from the customer.
you received an enquiry on date {today} of a customer 
whose name is {nm}, weight is {wt} in kg and height is {ht} in meters. 
calculate bmi of the customer. generate diet and workout suggestions in 
one sentence to improve bmi and maintain fitness.
return information like name, date, weight, height, bmi, bmi status, diet suggestion and 
workout suggestion in JSON format.
'''

response=call_chatgpt(prompt)
print(response)