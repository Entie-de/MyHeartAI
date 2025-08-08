import os
from groq import Groq

def translate_to_language(text, language="Urdu"):
    prompt = f"Translate this poetic caption to {language}:\n{text}"
    client = Groq(api_key=os.getenv("GROQ_API_KEY1"))
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return completion.choices[0].message.content.strip()
