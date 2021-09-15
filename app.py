from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request, send_file, Response

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
        try: 	
          b+=scrap(l)
        except: 
          _		

    
    now = datetime.datetime.now()
    sumar=datetime.timedelta(hours = -3)
    now=now+sumar
    nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
    return Response(b,mimetype="text/csv",headers={"Content-disposition": "attachment; filename="+nw+".csv"})
 


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
"https://www.vea.com.ar/leche-en-polvo-nido-3-prebio-1-leche-800g/p",
"https://www.vea.com.ar/queso-pategras-la-serenisima-paq-x-kg-2/p",
"https://www.vea.com.ar/queso-pategras-sancor-tradicional-ca-pintado-1-kg/p"
}