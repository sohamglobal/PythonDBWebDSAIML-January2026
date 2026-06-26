from openai import OpenAI
import base64

client=OpenAI(api_key="sk-proj-")

def encode_image(image_path):
    with open(image_path,"rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")


image_path="forest.jpg"
base64_image=encode_image(image_path)

response=client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role":"user",
            "content": [
                {"type":"text","text":"Describe this image in simple language"},
                {
                    "type":"image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)