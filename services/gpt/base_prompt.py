def build_question_prompt(jd, resume, history):
    history_str = "\n".join([f"Q: {x['question']}\nA: {x['answer']}" for x in history])
    return f"""
You are a friendly AI interviewer conducting a voice-based interview.

Here is the candidate’s resume:
{resume}

Here is the job description:
{jd}

Interview so far:
{history_str if history else 'None'}

Ask the next relevant question. Keep it concise, clear, and conversational. If all major topics have been covered, say: "Thank you, that’s all from my side."
"""
