from flask import Flask, jsonify, Blueprint
import time
import math
import json
import requests
import asyncio
import threading
import sbkeys

sbkey = sbkeys.sbkey
apigenres = Blueprint("genres",__name__,url_prefix='/api/genres')

app = Flask(__name__)
uTime = float(time.time() + 30.0)
apidata = {}
#Hopefully this is more secure than the old code lol
def UpdateAPI():
    genresdat = requests.get("https://jcvfukpccvibxumakqdh.supabase.co/rest/v1/genres?select=*",headers={"apikey":sbkey,"Authorization":"Bearer "+sbkey})
    genresdat = genresdat.json()
    return genresdat
@apigenres.route('/', methods=['GET'])
def get_items():
    apidata = UpdateAPI()
    return jsonify(apidata)

# GET endpoint to retrieve a specific item by ID
@apigenres.route('/item_id=<int:item_id>', methods=['GET'])
def get_item(item_id):
    apidata = UpdateAPI()
    item = next((item for item in apidata if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)