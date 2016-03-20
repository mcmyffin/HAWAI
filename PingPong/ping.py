from flask import Flask, request, redirect, url_for
import requests
import time


app = Flask(__name__)
rem_adr = "http://127.0.0.1"




@app.route('/service/sendPing', methods=['GET'])
def sendPing():
    print("send ping to "+rem_adr)
    requests.get(url=rem_adr+"/service/sendPing")
    return "OK SENDED"



@app.route('/service/sendPong', methods=['GET'])
def recievePong():
    time.sleep(2)
    adr = request.remote_addr
    print("RECIEVE PONG")
    time.sleep(0.5)
    return sendPing()


app.run(host="127.0.0.1", port=8080, debug=True)
