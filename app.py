from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request, send_file

import pandas as pd
import requests
from urllib.request import urlopen, Request
import datetime 

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():
  if request.method == 'POST':
    return "POST"
  else:
    b=""
    for l in lista(): 
        b+=scrap(l)
    
    #now = datetime.datetime.now()
    #nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))

    f = open("scrap.txt", "w")
    f.write(b)

    return send_file(f.name, mimetype="csv", attachment_filename=file.name, as_attachment=True)   
    #return str(b)
    


if __name__ == "__main__":
    app.run(port=8000, debug=True)


def archivo(b):
  File_object = open(r"Archivo.txt","w")
  return File_object.write(b)


def scrap(site):
    r = requests.get(site)
    b=""

    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find("span", {"class": "vtex-breadcrumb-1-x-term vtex-breadcrumb-1-x-term--breadcrumb-style ph2 c-on-base"}).text    
    b+=";"
    b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"}).text
    b+=","
    b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"}).text    
    b+="\n"
    
    return b


def lista(): 
    return {
"https://www.vea.com.ar/galletitas-lincoln-angry-birds/p",
"https://www.vea.com.ar/galletitas-criollitas-de-agua-x100gr/p",
"https://www.vea.com.ar/galletitas-criollitas-x400g/p"
}