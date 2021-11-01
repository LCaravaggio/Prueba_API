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
    l="https://www.vea.com.ar/"+query+"/p"
    try:
        return (scrapvea(l))
    except Exception as e:
        r = requests.get(l)
        soup = BeautifulSoup(r.content, 'html.parser')
        return ("no se pudo acceder a VEA")


@app.route("/carrefour/search/<query>")
def search_query_carr(query=None):
    l="https://www.carrefour.com.ar/"+query+"/p"
    try:
        return (scrapcarrefour(l))
    except Exception as e:
        return ("no se pudo acceder a Carrefour")

@app.route("/dia/search/<query>")
def search_query_dia(query=None):
    l="https://diaonline.supermercadosdia.com.ar/"+query+"/p"
    try:
        return (scrapdia(l))
    except Exception as e:
        return ("no se pudo acceder a Dia")

@app.route("/coto/search/<querycoto>")
def search_query_coto(querycoto=None):
    med="/_/"
    last=querycoto[-23:]
    ini=querycoto.replace(last,"")
    newquery="https://www.cotodigital3.com.ar/sitios/cdigi/producto/"+ini+med+last
    try:
        return (scrapcoto(newquery))
    except Exception as e:
        return ("no se pudo acceder a Coto")

if __name__ == "__main__":
    app.run(port=8000, debug=True)


def scrapvea(sitevea):
    r = requests.get(sitevea)
    b="" 
    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find('span', {'class':'vtex-store-components-3-x-productBrand'}).text.replace(" ","").replace("\n","").replace("\r","") + ";"
    ini=str(soup).find('"teasers":[],"Price":')
    fin=str(soup).find(',"ListPrice":')
    b+=str(soup)[ini+21:fin]
    return b


def scrapcoto(sitecoto):
    r = requests.get(sitecoto)
    b=""
    soup = BeautifulSoup(r.content, 'html.parser')
    b+=soup.find("h1", {"class": "product_page"}).text.replace(" ","").replace("\n","").replace("\r","").replace(";","").replace("\t","") + ";"     
    b+=soup.find("span", {"class": "atg_store_newPrice"}).text.replace("$","").replace(" ","").replace("\n","").replace("\r","").replace("\t","").replace("PRECIOCONTADO","").replace("PRECIOREGULAR","") 
    return b

def scrapcarrefour(sitecarrefour):
    r = requests.get(sitecarrefour)
    b=""
    
    soup = BeautifulSoup(r.content, 'html.parser')
    ini=str(soup).find('="og:type"/><meta content="')
    fin=str(soup).find('" data-react-helmet="true" property="og:title"/><meta ')
    b+=str(soup)[ini+27:fin]
    
    b+=";"
    ini=str(soup).find('":"Precio x unidad","values":{"type":"json","json":["($')
    b+=str(soup)[ini+55:ini+61]

    return b

def scrapdia(sitedia):
    r = requests.get(sitedia)
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
