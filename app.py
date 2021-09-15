from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request

import pandas as pd
import requests
from urllib.request import urlopen, Request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
  if request.method == 'POST':
    return "soup"
  else:
    site = 'https://www.vea.com.ar/bife-de-chorizo-2/p'
    r = requests.get(site)
    #soup = BeautifulSoup(r.content, 'html.parser')
    return "get 2"


if __name__ == "__main__":
    app.run(port=8000, debug=True)