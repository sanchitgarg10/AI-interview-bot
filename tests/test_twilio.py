from twilio.rest import Client
from env_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, TO_PHONE_NUMBER

# Replace this with your ngrok or Codespace tunnel URL
NGROK_URL = "https://your-ngrok-url.ngrok.io/voice"

def make_call():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    call = client.calls.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        url=NGROK_URL
    )
    print(f"Call initiated: SID={call.sid}")

if __name__ == "__main__":
    make_call()
