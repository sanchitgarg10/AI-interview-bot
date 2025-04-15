from flask import Response
from twilio.twiml.voice_response import VoiceResponse
from services.gpt.generate_question import generate_next_question
from services.user.resume_data import resume_text
from services.user.jd import job_description
from config.constants import MAX_QUESTIONS

interview_history = []
question_count = 0

def handle_twilio_request(req):
    global interview_history, question_count

    response = VoiceResponse()
    speech_result = req.form.get("SpeechResult")

    if speech_result:
        interview_history[-1]["answer"] = speech_result

    if question_count >= MAX_QUESTIONS:
        response.say("Thank you. This concludes the interview. Have a nice day.")
        return Response(str(response), mimetype="text/xml")

    question = generate_next_question(job_description, resume_text, interview_history)
    interview_history.append({"question": question, "answer": ""})
    response.say(question)
    response.gather(input="speech", timeout=5, speechTimeout="auto", action="/voice", method="POST")

    question_count += 1
    return Response(str(response), mimetype="text/xml")
