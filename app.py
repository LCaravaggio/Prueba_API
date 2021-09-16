from bs4 import BeautifulSoup
from flask_cors import cross_origin, CORS
from flask import Flask, render_template, request, send_file, Response

import pandas as pd
import requests
from urllib.request import urlopen, Request
import datetime 

app = Flask(__name__)
CORS(app)

@app.route('/')
@cross_origin()
def index():
    b=""
    for l in lista(): 	
        try:
            b+=scrap(l)
        except:
            b+="/n"
    now = datetime.datetime.now()
    sumar=datetime.timedelta(hours = -3)
    now=now+sumar
    nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
    return Response(b,mimetype="text/csv",headers={"Content-disposition": "attachment; filename="+nw+".csv"})
 



@app.route("/api/search/<query>")
def search_queryA(query=None):
    b=""
    try:
        b+=scrap(query)
        return (b)
    except Exception as e:
        return ("Error API: "+f"{e}" + query)

@app.route("/api/<query>")
def search_query(query=None):
	return(query)

if __name__ == "__main__":
    app.run(port=8000, debug=True)


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


@app.errorhandler(500)
def internal_error(error):
    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404


def lista(): 
    return {"https://www.vea.com.ar/galletitas-lincoln-angry-birds/p",
"https://www.vea.com.ar/galletitas-criollitas-de-agua-x100gr/p"
}