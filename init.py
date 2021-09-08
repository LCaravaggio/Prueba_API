from flask import Flask
from flask_cors import CORS


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hello World API!<br/>")


if __name__ == '__main__':
    app.run()