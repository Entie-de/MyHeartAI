# groq_api/tools.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Load the Groq API key from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in the environment.")

client = Groq(api_key=groq_api_key)

# Model 1: Vision-based Caption Generator
def generate_caption(image_description):
    messages = [
        {"role": "user", "content": f"Describe this image in an emotionally poetic style: {image_description}"}
    ]
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False
    )
    return response.choices[0].message.content.strip()

# Model 2: Poetic Love Story Generator (Fixed prompt to remove internal thinking)
def generate_poetic_story(memory):
    prompt = f"""You are a poetic writer.

Turn this memory into a deeply romantic, emotional, and cinematic love story. 
Write the story in flowing, poetic prose — like a scene from a beautiful movie. 
Use vivid language and metaphors. 
Only return the final story — no titles, no explanation, no reasoning, no thinking steps, and no inner thoughts. 
Do not include any phrases like "I will now" or "Let's think".

Memory: "{memory}"
"""
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=1024,
        top_p=0.95,
        stream=False
    )
    return response.choices[0].message.content.strip()
