from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    greet = "Hello, This is Samiksha's experiment 4 for cloud computing~ >.<"
    return greet

@app.route("/about")
def about():
    return "This is a simple Flask application running on Microsoft Azure."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
