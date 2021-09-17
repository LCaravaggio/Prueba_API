from bs4 import BeautifulSoup
from flask_cors import cross_origin, CORS
from flask import Flask, render_template, request, send_file, Response

import pandas as pd
import requests
from urllib.request import urlopen, Request
import datetime 

app = Flask(__name__)
CORS(app)

@app.route("/")
@cross_origin()
def welcome():
    return (
        f"Bienvenido a la API!<br/>")
 

@app.route("/vea/search/<query>")
def search_queryA(query=None):
    b=""
    l="https://www.vea.com.ar/"+query+"/p"
    try:
        b+=scrapvea(l)
        return (b)
    except Exception as e:
        return ("no se pudo acceder")

@app.route("/coto/search/<query>")
def search_queryA(query=None):
    b=""
    l="https://www.coto.com.ar/"+query+"/p"
    try:
        b+=scrapcoto(l)
        return (b)
    except Exception as e:
        b+="/n"
        return (b)



if __name__ == "__main__":
    app.run(port=8000, debug=True)


def scrapvea(site):
    r = requests.get(site)
    b=""
    
    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find("span", {"class": "vtex-breadcrumb-1-x-term vtex-breadcrumb-1-x-term--breadcrumb-style ph2 c-on-base"}).text    
    b+=";"
    b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price"}).text
    b+=","
    b+=soup.find("span", {"class": "vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price"}).text    

    return b



def scrapcoto(site):
    r = requests.get(site)
    b=""
    
    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find("h1", {"class": "product_page"}).text.replace(" ","").replace("\n","").replace("\r","").replace(";","").replace("\t","") + ";"     
    b+=soup.find("span", {"class": "atg_store_newPrice"}).text.replace("$","").replace(" ","").replace("\n","").replace("\r","").replace("\t","").replace("PRECIOCONTADO","").replace("PRECIOREGULAR","") + "\n" 
    b+="\n"

    return b

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404
