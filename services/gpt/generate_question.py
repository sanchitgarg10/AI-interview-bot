from services.gpt.base_prompt import build_question_prompt
from config.model_config import MODELS, PROVIDER
import openai

openai.api_key = MODELS[PROVIDER]["api_key"]

def generate_next_question(jd, resume, history):
    prompt = build_question_prompt(jd, resume, history)

    if PROVIDER == "openai":
        response = openai.ChatCompletion.create(
            model=MODELS["openai"]["model"],
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message["content"].strip()

    # Add logic for claude, deepseek, etc. here later
