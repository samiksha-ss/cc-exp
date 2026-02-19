from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    greet = "Hello, This is Samiksha's experiment 4 for cloud computing~ >.<"
    edit = "This is an edit to test the deployment process. Hope it works!!"
    return greet + " " + edit

@app.route("/about")
def about():
    return "This is a simple Flask application running on Microsoft Azure."


