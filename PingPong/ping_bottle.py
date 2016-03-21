from bottle import Bottle, redirect, request, run,HTTPResponse ,response;# or route
from threading import Thread
import requests
import time

rem_adr = "http://141.22.86.37:8080/service/sendPing"
app = Bottle()



class Message():
    message = ""

    def getMessage(self):
        self.message = self.message + "<b>Ping sent</b><br>"
        return self.message


message = Message()

@app.get('/service/sendPing')
def sendPing():
    time.sleep(2)
    print("send ping to "+rem_adr)

    def postPing():
        requests.post(url=rem_adr)

    t = Thread(target = postPing, args=())
    t.start()
    return message.getMessage()


@app.post('/service/sendPong')
def receivePong():

    print("RECEIVE PONG")
    # time.sleep(0.5)
    return sendPing()


app.run(host="141.22.89.39", port="8081")


