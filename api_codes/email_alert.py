import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


twilio_config = "jsons/twilio_config.json"
with open(twilio_config) as json_data_file:
    config = json.load(json_data_file)

with open(config["email_template"], 'r') as f:
    html_string = f.read()

to_emails = [
    ('arkaprova.deb97@gmail.com', 'Arkaprova Deb'),
    #('bappadityashome@gmail.com', 'Bappaditya Shome'),
    #('haimantikamitra@gmail.com', 'Haimantika Mitra')
]
message = Mail(
    from_email=(config["sender_email"], config["sender_name"]),
    to_emails=to_emails,
    subject=config["email_subject"],
    html_content=html_string)

def sendEmail():
    try:
        sendgrid_client = SendGridAPIClient(config["sendgridAPIKey"])
        response = sendgrid_client.send(message)
        #print(response.status_code)
        #print(response.body)
        #print(response.headers)
        return (str(response.status_code))
    except Exception as e:
        #print(e)
        return (str(e))

if __name__=="__main__":
    sendEmail()