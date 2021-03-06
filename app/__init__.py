from flask import Flask, request
from flask_cors import CORS # For testing
from dotenv import load_dotenv
import os
import wolframalpha

load_dotenv()

app = Flask(__name__)
CORS(app) # For testing

WOLFRAM_APP_ID = os.environ["WOLFRAM_APP_ID"]
wolfram = wolframalpha.Client(WOLFRAM_APP_ID)

@app.route('/')
def default():
    return 'Hello, World!'

@app.route('/api/solve/text', methods=['POST', 'GET'])
def text():
    print(request)
    error = 'Invalid request. Make sure you are making POST requests.'
    content = request.get_json(silent=True, force=True)
    text = ""
    if content != None: 
        text = content["text"]
    if request.method == 'POST':
        if text != None:
            return wolframRequest(text)
        else:
            error = 'Invalid request body. Format it as JSON, like {“text”: “texthere”}'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return error

@app.route('/api/solve/image')
def image():
    error = 'Invalid request. Make sure you are making POST requests.'
    content = request.get_json(silent=True, force=True)
    text = content["text"]
    if request.method == 'POST':
        if text != None:
            return imgRequest(text)
        else:
            error = 'Invalid request body. Format it as JSON, like {“img”: “texthere”}'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return error

def imgRequest(data):
   if data.img==None:
       return "Error: Couldn't find an image"
   else:

def wolframRequest(text):
    # this will make the request to wolfram with whatever text is passsed in, then return the response
    res = wolfram.query(text)
    return res
