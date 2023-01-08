import time
from flask import Flask
import os
import subprocess

app = Flask(__name__)

@app.route('/hi', methods=['POST'])
def hi():
    return 'Hello Slack!'

@app.route('/duffy', methods=['POST'])
def duffy():
    return 'test!'

@app.route('/chrome', methods=['POST'])
def chrome():
    subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe')
    return 'chrome is open now'

@app.route('/restart', methods=['POST'])
def restart():
    os.system("shutdown /r /t 10")
    return "system is restarting in 10 sce"

@app.route('/shutdown', methods=['POST'])
def shutdown():
    os.system("shutdown /s /t 10")
    return "system is shutting down in 10 sce"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)