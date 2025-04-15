import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.gpt.generate_question import generate_next_question
from services.gpt.evaluate_answer import evaluate_and_followup
from services.user.resume_data import resume_text
from services.user.jd import job_description
from config.model_config import OPENAI_MODEL
from config.constants import MAX_QUESTIONS

def run_full_interview():
    print(f"\n🤖 Smart Interview Started using model: {OPENAI_MODEL}\n")

    interview_history = []
    main_question_count = 0

    while main_question_count < MAX_QUESTIONS:
        question = generate_next_question(job_description, resume_text, interview_history)

        if "thank you" in question.lower():
            print(f"\n✅ AI: {question}")
            break

        print(f"\n🤖 AI asks: {question}")
        user_answer = input("🎙️ Your answer: ").strip()

        interview_history.append({
            "question": question,
            "answer": user_answer
        })

        followup = evaluate_and_followup(question, user_answer, job_description, resume_text)

        if followup:
            print(f"\n🔁 AI Follow-up: {followup}")
            followup_answer = input("🎙️ Your follow-up answer: ").strip()

            interview_history.append({
                "question": followup,
                "answer": followup_answer
            })

        main_question_count += 1

    print("\n📝 Interview complete. Responses stored in memory.\n")

if __name__ == "__main__":
    run_full_interview()
