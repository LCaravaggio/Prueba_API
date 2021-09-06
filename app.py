from flask import Flask, request, jsonify

app = Flask(__name__)

print('model loaded hola')

@app.route('/')
def health_check():
    return 'OK'

@app.route('/', methods=['POST'])

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
