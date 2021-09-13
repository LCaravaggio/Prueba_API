# app.py
from flask import Flask, request, jsonify

from bs4 import BeautifulSoup
import requests
import time
import datetime 



app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    #return "<h1>Welcome to our server !!</h1>"
	return fun()

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)


def fun():
  a=""
  listacorta={"https://www.vea.com.ar/milanesa-nalga-5/p",
"https://www.vea.com.ar/bife-de-chorizo-2/p",}
    
  for l in listacorta: 
    try:
	    r = requests.get(l.replace("\n",""))
	    soup = BeautifulSoup(r.content, 'html.parser')
	    #print(l.replace("\n",""))
	    a += l.replace("\n","") + ";"
	    a += soup.find_all('span', {'class':'vtex-store-components-3-x-productBrand '})[0].text.replace(" ","").replace("\n","").replace("\r","") + ";"
	    a += soup.find_all('span', {'class':'vtex-product-price-1-x-currencyInteger vtex-product-price-1-x-currencyInteger--shelf-main-selling-price'})[0].text.replace(" ","").replace("\n","").replace("\r","") + ";" 
	    a += soup.find_all('span', {'class':'vtex-product-price-1-x-currencyFraction vtex-product-price-1-x-currencyFraction--shelf-main-selling-price'})[0].text.replace("$","").replace(" ","").replace("\n","").replace("\r","").replace("PRECIOCONTADO","") + "\n" 

    except:
      a+="ERROR+\n"

  return a