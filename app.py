from flask import Flask
from flask_cors import CORS

def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])


app = Flask(__name__)
CORS(app)


@app.route("/")
def welcome():
    return (
        f"Welcome to the RECIPERFECT search API!<br/>")