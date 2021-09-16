from bs4 import BeautifulSoup
from flask_cors import cross_origin
from flask import Flask, render_template, request, send_file, Response

import pandas as pd
import requests
from urllib.request import urlopen, Request
import datetime 

from rq import Queue
from worker import conn
from utils import scrap

q = Queue(connection=conn)

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
            b+=q.enqueue(scrap, l)
          except:
            b+="/n"
       


    now = datetime.datetime.now()
    sumar=datetime.timedelta(hours = -3)
    now=now+sumar
    nw=str(now.strftime("%Y-%m-%d %H-%M-%S"))
    return Response(b,mimetype="text/csv",headers={"Content-disposition": "attachment; filename="+nw+".csv"})
 


if __name__ == "__main__":
    app.run(port=8000, debug=True)



def lista(): 
    return {"https://www.vea.com.ar/galletitas-lincoln-angry-birds/p",
"https://www.vea.com.ar/vacio-de-novillito-ca/p",
"https://www.vea.com.ar/galletitas-criollitas-de-agua-x100gr/p"
}