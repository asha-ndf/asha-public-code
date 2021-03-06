##実用版です
##
#Config====================================
import datetime
import serial
from flask import *

app = Flask(__name__)
bitRate = 9600

#Serial====================================
ser = serial.Serial()
portlist = []
for i in range(10):
    portlist.append('COM'+str(i))
def openport():
    global ser
    if ser.is_open:
        ret =1
    else:
        for i in portlist:
            try:
                ser = serial.Serial(i, bitRate, timeout=0.1)
                ret= 1
                break
            except:
                ret = 0
    return ret

#Web App====================================
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
        ser.write('a'.encode('utf-8'))
        message = '放出コマンドが送信されました'
    else:
        message = '放出コマンドエラー：送信端末が接続されていません'
    return render_template("main.html", msg=message)

@app.route('/lock')
def dlock():
    if openport()==1:
        ser.write('b'.encode('utf-8'))
        message = 'ロックコマンドが送信されました'
    else:
        message = 'ロックコマンドエラー：送信端末が接続されていません'
    return render_template("main.html", msg=message)

@app.route('/quit')
def quit():
    if openport()==1:
        ser.close()
    message = 'シリアル通信が切断されました。'
    return  render_template("main.html", msg=message)

@app.route('/hight') #ajax用のjson送信
def jsonhight():
    #現在のサーボモーターの状態を表示する
    hight = ser.readline().decode('utf-8')
    return jsonify({'result': hight})

#run====================================
if __name__ == '__main__':
    app.run(host='localhost', port=5000, threaded=False)
