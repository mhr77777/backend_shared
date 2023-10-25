from flask import Flask, jsonify, Blueprint
import time
import math
import json
import requests
import asyncio
import threading

apibooks = Blueprint("books",__name__,url_prefix='/api/books')

#MONIKA CODED THIS FILE BTW!!

app = Flask(__name__)
uTime = float(time.time() + 30.0)
apidata = {}
#Hopefully this is more secure than the old code lol
sbkey = open(".dbkeys").read().split("=")[1]
def UpdateAPI():
    booksdat = requests.get("https://jcvfukpccvibxumakqdh.supabase.co/rest/v1/books?select=*",headers={"apikey":sbkey,"Authorization":"Bearer "+sbkey})
    booksdat = booksdat.json()
    return booksdat
@apibooks.route('/', methods=['GET'])
def get_items():
    apidata = UpdateAPI()
    return jsonify(apidata)

# GET endpoint to retrieve a specific item by ID
@apibooks.route('/item_id=<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in apidata if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)