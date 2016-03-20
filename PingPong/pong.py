from flask import Flask
import requests
import time

app = Flask(__name__)



@app.route('/service/sendPing', methods=['GET'])
def receivePingSendPong():
    adr = "http://127.0.0.1:8080/service/sendPong"
    print("RECEIVE PING")
    time.sleep(1.5)
    print("SEND PONG to : "+adr)
    requests.get(url=adr)
    return ""




app.run(port=5000, debug=True)
