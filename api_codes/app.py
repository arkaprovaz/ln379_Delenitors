from flask import Flask, request, jsonify
from waitress import serve
import json
import twilio_call_sms as tg
from email_alert import sendEmail
from tweet import tweet
from CRUD import device_logs
from predict_water_rise import get_pred_water_level
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello World this is the flask app! <br><br> Call API: /api/v1.0/triggerCall <br> SMS API: /api/v1.0/triggerSMS <br> Email API: /api/v1.0/triggerEmail <br> Tweet API: /api/v1.0/triggerTweet <br><br> GetData API: /api/v1.0/getData?datapoints=1"


@app.route('/api/v1.0/triggerCall', methods=['GET'])
def call():
    st = tg.sendTwilio()
    st.triggerAlertCall("+918944992236")
    response = {"status": "OK"}
    return (jsonify(response))


@app.route('/api/v1.0/triggerSMS', methods=['GET'])
def SMS():
    st = tg.sendTwilio()
    st.triggerAlertSMS("+918944992236")
    response = {"status": "OK"}
    return (jsonify(response))


@app.route('/api/v1.0/triggerEmail', methods=['GET'])
def Email():
    res = sendEmail()
    response = {"status": res}
    return (jsonify(response))


@app.route('/api/v1.0/triggerTweet', methods=['GET'])
def TweetAlert():
    res = tweet()
    response = {"status": res}
    return (jsonify(response))


@app.route("/api/v1.0/getData", methods=['GET'])
def getData():
    try:
        return(jsonify(device_logs(request.args.get("datapoints"))))
    except:
        response = {"status": "Error"}
        return (response)


@app.route("/api/v1.0/getPredData", methods=["GET"])
def getPredData():
    try:
        return jsonify(get_pred_water_level(request.args.get("city")))
    except:
        response = {"status": "Error"}
        return (response)


if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000)
    serve(app, host='0.0.0.0', port=5000)
