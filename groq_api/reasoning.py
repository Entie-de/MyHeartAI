import os
from groq import Groq

def generate_reasoning_caption(memory_prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY1"))
    completion = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "user", "content": memory_prompt}
        ],
        temperature=0.6,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=False
    )
    return completion.choices[0].message.content.strip()
