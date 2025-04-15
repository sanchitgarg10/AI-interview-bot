from services.gpt.base_prompt import build_question_prompt
from config.model_config import MODELS, PROVIDER

# Import and initialize the OpenAI v1.0+ client
from openai import OpenAI
client = OpenAI(api_key=MODELS["openai"]["api_key"])  # pulls from your model config

def generate_next_question(jd, resume, history):
    prompt = build_question_prompt(jd, resume, history)

    if PROVIDER == "openai":
        response = client.chat.completions.create(
            model=MODELS["openai"]["model"],
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()

    # 🔁 Add support for other providers like Claude, DeepSeek, etc. here later
