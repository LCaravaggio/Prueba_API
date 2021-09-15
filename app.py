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
    site = 'https://www.vea.com.ar/queso-sardo-la-paulina/p'
    r = requests.get(site)
    a="hola 5"
    b=""


    soup = BeautifulSoup(r.content, 'html.parser')
    b += soup.find_all('span', {'class':'vtex-store-components-3-x-productBrand '})[0].text + ";"
    b += soup.find_all('span', {'class':'vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price'})[0].text + "," 
    b += soup.find_all('span', {'class':'vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price'})[0].text 
    return str(a)


if __name__ == "__main__":
    app.run(port=8000, debug=True)