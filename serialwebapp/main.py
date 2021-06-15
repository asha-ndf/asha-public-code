from flask import Flask
app = Flask(__name__)

@app.route('/')
def status():
    return 'This is status page'

@app.route('/open')
def dopen():
    return 'opend'

@app.route('/lock')
def dlock():
    return 'locked'

if __name__ == '__main__':
    app.run()
