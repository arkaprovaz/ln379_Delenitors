from twilio.rest import Client
import json

twilio_config = "jsons/twilio_config.json"

class sendTwilio():
    def __init__(self):
        with open(twilio_config) as json_data_file:
            config = json.load(json_data_file)

        self.TWILIO_PHONE_NUMBER=config["twilio_phone_number"]
        self.client = Client(config["account_sid"],config["auth_token"])
        self.TWIML_INSTRUCTIONS_URL=config["twilio_voice_instruction"]
        self.sms_body = config["sms_body"]

    def triggerAlertCall(self,number):
        self.client.calls.create(to=number,from_=self.TWILIO_PHONE_NUMBER,url=self.TWIML_INSTRUCTIONS_URL,method="GET")

    def triggerAlertSMS(self,number):
        self.client.messages.create(to=number,from_=self.TWILIO_PHONE_NUMBER,body=self.sms_body)

def main():
    st=sendTwilio()
    #st.triggerAlertSMS("+918944992236")
    st.triggerAlertCall("+918944992236")

if __name__ == "__main__":
    main()
