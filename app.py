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
def search_query_vea(query=None):
    b=""
    l="https://www.vea.com.ar/"+query+"/p"
    try:
        b+=scrapvea(l)
        return (b)
    except Exception as e:
        return ("no se pudo acceder")


@app.route("/carrefour/search/<query>")
def search_query_carr(query=None):
    b=""
    l="https://www.carrefour.com.ar/"+query+"/p"
    try:
        b+=scrapcarrefour(l)
        return (b)
    except Exception as e:
        return ("no se pudo acceder")


@app.route("/dia/search/<query>")
def search_query_dia(query=None):
    b=""
    l="https://diaonline.supermercadosdia.com.ar/"+query+"/p"
    try:
        b+=scrapdia(l)
        return (b)
    except Exception as e:
        return ("no se pudo acceder")



@app.route("/coto/search/<querycoto>")
def search_query_coto(querycoto=None):
    b=""
    med="/_/"
    last=querycoto[-23:]
    ini=querycoto.replace(last,"")
    newquery="https://www.cotodigital3.com.ar/sitios/cdigi/producto/"+ini+med+last
    try:
        b+=scrapcoto(newquery)
        return (b)
    except Exception as e:
        return ("no se pudo acceder")



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


def scrapcoto(sitecoto):
    r = requests.get(sitecoto)
    b=""
    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find("h1", {"class": "product_page"}).text.replace(" ","").replace("\n","").replace("\r","").replace(";","").replace("\t","") + ";"     
    b+=soup.find("span", {"class": "atg_store_newPrice"}).text.replace("$","").replace(" ","").replace("\n","").replace("\r","").replace("\t","").replace("PRECIOCONTADO","").replace("PRECIOREGULAR","") 
    return b

def scrapcarrefour(site):
    r = requests.get(site)
    b=""
    
    soup = BeautifulSoup(r.content, 'html.parser')
    ini=str(soup).find('name="robots"/><meta content="')
    fin=str(soup).find('" data-react-helmet="true" name="description"/>')
    b+=str(soup)[ini+30:fin]
    
    b+=";"
    ini=str(soup).find('":"Precio x unidad","values":{"type":"json","json":["($')
    b+=str(soup)[ini+55:ini+61]

    return b

def scrapdia(site):
    r = requests.get(site)
    b=""
    
    soup = BeautifulSoup(r.content, 'html.parser')
    ini=str(soup).find('},"productName":"')
    fin=str(soup).find('","productBrandId":')
    b+=str(soup)[ini+17:fin]
    b+=";"
    ini=str(soup).find('fullSellingPrice":"')
    b+=str(soup)[ini+19:ini+26]
    
    return b

@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404
