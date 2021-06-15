#Config
import serial
from flask import *
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
    if openport() ==1:
        message = str(ser.name) + 'で接続しています。'
    else:
        message = '接続されていません'
    return render_template("main.html", msg=message)

@app.route('/open')
def dopen():
    if openport()==1:
        ser.write(1)
    return '放出コマンドを送信しました'

@app.route('/lock')
def dlock():
    if openport()==1:
        ser.write(0)
    return 'ロックコマンドを送信しました'

@app.route('/quit')
def quit():
    if openport()==1:
        ser.close()

if __name__ == '__main__':
    app.run()
