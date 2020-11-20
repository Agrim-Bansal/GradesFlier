import requests
from flask import Flask
app = Flask(__name__)



@app.route('/')
def default():
    return 'Hello, World!'

@app.route('/api/solve/text')
def login():
    error = 'Invalid request. Make sure you are making POST requests.'
    content = request.get_json(silent=True, force=True)
    text= content["text"]
    if request.method == 'POST':
        if text != None:
            return wolframRequest(text)
        else:
            error = 'Invalid request body. Format it as JSON, like {“text”: “texthere”}'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return error

def wolframRequest(text):
    return text