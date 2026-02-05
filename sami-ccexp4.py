from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Python Web App Successfully Deployed on Azure 🚀"

@app.route("/about")
def about():
    return "This is a simple Flask application running on Microsoft Azure."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
