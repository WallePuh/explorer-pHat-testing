from flask import Flask
app = Flask(__name__)

import explorerhat
import time, threading ## Import 'time' library. Allows us to use 'sleep'

blinker = 0
@app.route('/')
def hello_world():
    start_blink()
    return 'Hello to the World!'

def start_blink():
    blinker++
    threading.Timer(1, blink).start()

def blink():
    print "blink"
    explorerhat.output[0].blink()
    threading.Timer(5, stop_blink).start()

def stop_blink():
    print "stop_blink" + blinker
    if blinker == 1:
        explorerhat.output[0].stop()
    blinker--

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
