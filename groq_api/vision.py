import os
from groq import Groq

def generate_vision_caption(description):
    client = Groq(api_key=os.getenv("GROQ_API_KEY2"))
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {"role": "user", "content": description}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return completion.choices[0].message.content.strip()
