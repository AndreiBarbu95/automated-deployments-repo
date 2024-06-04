import time
import os
import logging
from flask import Flask, jsonify, request
import subprocess as sp

app = Flask(__name__)

hostName = sp.getoutput("hostname")

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    url = request.url
    logging.info(f"{request.remote_addr} - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"{request.method} {url} {request.environ.get('SERVER_PROTOCOL')}\" {user_agent}")
    return f"<h1><center>{hostName} {request.remote_addr}</center></h1>"

@app.route("/images")
def images():
    user_agent = request.headers.get('User-Agent')
    url = request.url
    logging.info(f"{request.remote_addr} - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"{request.method} {url} {request.environ.get('SERVER_PROTOCOL')}\" {user_agent}")
    return "<h1><center>Images</center></h1>"

@app.route("/videos")
def videos():
    user_agent = request.headers.get('User-Agent')
    url = request.url
    logging.info(f"{request.remote_addr} - - [{time.strftime('%d/%b/%Y %H:%M:%S')}] \"{request.method} {url} {request.environ.get('SERVER_PROTOCOL')}\" {user_agent}")
    return "<h1><center>Videos</center></h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
