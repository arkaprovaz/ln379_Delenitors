## API Codes
### JSON files are not included as it is having the API credentials and tokens.
JSON format:

db_config.json
```
{
    "server" : "",
    "database" : "",
    "user" : "",
    "pass" : "",

    "table" : "[sih].[dbo].[device_logs]"
    
}
```

mqtt_config.json
```
{
  "mqtt_host": "",
  "mqtt_port": 1883,
  "mqtt_uid": "",
  "mqtt_password": "",
  "topic": ""
}
```

tweet_config.json
```
{
  "consumer_key": "",
  "consumer_secret": "",
  "access_token": "",
  "access_token_secret": "",
  "tweet_body": "Attention! There are high chances of flood in your area. Water level is above Danger Level. Please stay alert. Contact local NGO at +919876543210"
}

```
twilio_config.json
```
{
  "twilio_phone_number": "",
  "account_sid": "",
  "auth_token": "",
  "twilio_voice_instruction": "https://sihstoragedelenitors.blob.core.windows.net/%24web/flood.xml",
  "sms_body": "Attention! There are high chances of flood in your area. Water level is above Danger Level. Please stay alert. Contact local NGO at +919876543210",

  "sendgridAPIKey": "",
  "email_template": "assets/email_template.html",
  "email_subject": "Flood Alert!",
  "sender_email": "",
  "sender_name": "Delenitors"
}
```






CRUD.py is responsible for all CREATE, READ, UPDATE, DELETE operations with the Database
app.py is a flask server that is hosted on azure vm
email_alert.py is the code to generate and push alert via email
mqtt_subscriber.py is responsible for getting the data from the mqtt broker and pushing it to the database
predict_weather_rise.py is responsible for predicting the water level rise with respect to the weather forecast fetched from the weatherapi.com
predictor.py is a module that is being used by the predict_weather_rise.py
rainfall_model.py is the module that is for forecasting the water level rise
tweet.py is responsible for post tweets
twilio_call_sms.py is the code for generating the call and sms alert
weather_api.py is the code to hit the api provided by the weatherapi.com and convert it to specific format


