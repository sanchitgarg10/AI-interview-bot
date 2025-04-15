from config.model_config import MODELS, PROVIDER
import openai

openai.api_key = MODELS[PROVIDER]["api_key"]

def evaluate_and_followup(question, answer, jd, resume):
    prompt = f"""
You are evaluating a candidate’s response.

Q: {question}
A: {answer}

If the answer is strong, say: Proceed to next.
If weak, suggest ONE follow-up.
"""

    if PROVIDER == "openai":
        response = openai.ChatCompletion.create(
            model=MODELS["openai"]["model"],
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message["content"]
        return None if "Proceed to next" in result else result.strip()
