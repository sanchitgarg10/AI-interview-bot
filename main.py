from services.gpt.generate_question import generate_next_question
from services.gpt.evaluate_answer import evaluate_and_followup
from user.resume_data import resume_text
from user.jd import job_description
from config.constants import MAX_QUESTIONS, FOLLOWUP_ENABLED

## Test which model is being used
from config.model_config import OPENAI_MODEL
print(f"🤖 Using model: {OPENAI_MODEL}")
#################################

interview_history = []
print("🎙️ Smart AI Interview Started...\n")

for i in range(MAX_QUESTIONS):
    question = generate_next_question(job_description, resume_text, interview_history)
    print(f"\n🤖 AI: {question}")
    if "thank you" in question.lower():
        break

    answer = input("🎙️ Your answer: ").strip()
    interview_history.append({"question": question, "answer": answer})

    if FOLLOWUP_ENABLED:
        followup = evaluate_and_followup(question, answer, job_description, resume_text)
        if followup:
            print(f"🔁 AI Follow-up: {followup}")
            followup_answer = input("🎙️ Your follow-up answer: ").strip()
            interview_history.append({"question": followup, "answer": followup_answer})
