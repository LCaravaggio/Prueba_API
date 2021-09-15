from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request

import pandas as pd
from urllib.request import urlopen, Request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
    if request.method == 'POST':
	site = 'https://www.vea.com.ar/bife-de-chorizo-2/p'
		r = requests.get(site)
		soup = BeautifulSoup(r.content, 'html.parser')	
		return soup
    else:
        return "get"


if __name__ == "__main__":
    app.run(port=8000, debug=True)