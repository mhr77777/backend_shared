from flask import Flask, jsonify
import time
import math
import json


#MONIKA CODED THIS FILE BTW!!
app = Flask(__name__)
uTime = 0.0

#Hopefully this is more secure than the old code lol
sbkey = open(".dbkeys").read().split("=")[1]
def UpdateAPI():
    pass #I'll do this later ffs

apidata = UpdateAPI()

# GET endpoint to retrieve all books
@app.route('/api/books', methods=['GET'])
def get_items():
    return jsonify(apidata)

# GET endpoint to retrieve a specific item by ID
@app.route('/api/books/item_id=<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in apidata if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item)

if __name__ == '__main__':
    app.run(debug=True)