from bottle import Bottle, redirect, request, run # or route
import requests
import time

rem_adr = "http://127.0.0.1:5000/service/sendPing"
app = Bottle()



@app.get('/service/sendPing')
def sendPing():
    time.sleep(1)
    print("send ping to "+rem_adr)
    requests.post(url=rem_adr)
    return "OK SENDED"



@app.post('/service/sendPong')
def recievePong():
    time.sleep(2)
    print("RECIEVE PONG")
    time.sleep(0.5)
    return sendPing()


app.run(host="127.0.0.1", port="8080")


