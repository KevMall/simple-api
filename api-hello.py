from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello from Azure!"

if __name__ == "__main__":
    app.run()
