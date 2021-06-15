#Config
import serial
from flask import Flask
app = Flask(__name__)
bitRate = 9600

#Serial
ser = serial.Serial()
portlist = []
for i in range(10):
    portlist.append('COM'+str(i))
def openport():
    global ser
    if ser.is_open:
        ret =1
        pass
    else:
        for i in portlist:
            try:
                ser = serial.Serial(i, bitRate, timeout=0.1)
                ret= 1
                break
            except:
                ret = 0
    return ret
#Web App
@app.route('/')
def status():
    return str(openport())

@app.route('/open')
def dopen():
    return 'opend'

@app.route('/lock')
def dlock():
    return 'locked'

if __name__ == '__main__':
    app.run()
