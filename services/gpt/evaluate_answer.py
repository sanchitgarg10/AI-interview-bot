from config.model_config import MODELS, PROVIDER
from openai import OpenAI

client = OpenAI(api_key=MODELS["openai"]["api_key"])

def evaluate_and_followup(question, answer, jd, resume):
    prompt = f"""
You are an intelligent AI interviewer evaluating a candidate’s response.

Job Description:
{jd}

Candidate Resume:
{resume}

Question:
{question}

Answer:
{answer}

Instructions:
- Evaluate the answer based on relevance, depth, clarity, and alignment with the job description.
- If the answer is strong and needs no probing: respond with "Proceed to next."
- If the answer is weak or incomplete, ask ONE follow-up question to dig deeper.
"""

    if PROVIDER == "openai":
        response = client.chat.completions.create(
            model=MODELS["openai"]["model"],
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.choices[0].message.content
        return None if "Proceed to next" in result else result.strip()
