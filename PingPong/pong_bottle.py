from bottle import Bottle, HTTPResponse
import requests
import time

app = Bottle()
adr = "http://127.0.0.1:8080/service/sendPong"

@app.post('/service/sendPing')
def receivePingSendPong():
    print("RECEIVE PING")

    time.sleep(1.5)
    print("SEND PONG to : "+adr)
    # requests.post(url=adr)
    return "RECEIVED PING AND SEND PONG"

app.run(host="127.0.0.1", port="5000")