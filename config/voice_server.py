from flask import Flask, request, Response
from services.telephony.twilio_adapter import handle_twilio_request

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    return handle_twilio_request(request)

if __name__ == "__main__":
    app.run(port=5000)
