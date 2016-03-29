from bottle import Bottle
from threading import Thread
from getpass import _raw_input
import requests,time, sys




app = Bottle()


@app.get('/service/sendPing')
def sendPing():
    time.sleep(2)
    print("send ping to "+rem_adr)

    def postPing():
        requests.post(url=rem_adr)

    t = Thread(target = postPing, args=())
    t.start()
    return "SEND"


@app.post('/service/sendPong')
def receivePong():
    print("RECEIVE PONG")
    # time.sleep(0.5)
    return sendPing()




if(__name__ == "__main__"):
    host = _raw_input(">> Local Machine adress? ")
    port = _raw_input(">> Local Machine port? ")
    remHost = _raw_input(">> Remote Machine adress? ")
    remPort = _raw_input(">> Remote Machine port? ")
    rem_adr = "http://"+remHost+":"+remPort+"/service/sendPing"

    app.run(host=host,port=port)


