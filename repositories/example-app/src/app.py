from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! v2.0.0.2"