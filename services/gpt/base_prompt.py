def build_question_prompt(jd, resume, history):
    history_str = "\n".join([f"Q: {x['question']}\nA: {x['answer']}" for x in history])

    prompt = f"""
You are an AI interviewer conducting a job interview based on the following information.

Job Description:
{jd}

Candidate Resume:
{resume}

Interview so far:
{history_str if history else "None yet"}

Your task:
- Analyze the job description and determine the role and responsibilities.
- Based on the candidate’s resume and previous responses, ask the next most relevant interview question.
- Keep your tone conversational, professional, and neutral.
- Ask only one question at a time.
- If all major topics have been covered, respond with: "Thank you, that’s all from my side."

Generate the next interview question now:
"""

    return prompt.strip()
