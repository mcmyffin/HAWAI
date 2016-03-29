from bottle import Bottle, HTTPResponse
import requests
import time

app = Bottle()
adr = "http://127.0.0.1:8888/service/sendPong"

@app.post('/service/sendPing')
def receivePingSendPong():
    print("RECEIVE PING")
    time.sleep(1.5)
    sendPong()
    return "RECEIVED PING AND SEND PONG"

def sendPong():
    print("SEND PONG to : "+adr)
    requests.post(adr)

app.run(host="localhost", port="8881")