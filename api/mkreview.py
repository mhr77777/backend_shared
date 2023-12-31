from flask import Flask, jsonify, Blueprint, request
import time
import math
import json
import requests
import asyncio
import threading
import sbkeys

sbkey = sbkeys.sbkey
sbwritekey = sbkeys.sbwritekey

apireview = Blueprint("review",__name__,url_prefix='/api/review')

def get_largest_integer(array):
  largest_integer = array[0]
  for integer in array:
    if integer > largest_integer:
      largest_integer = integer
  return largest_integer
def getLatestID():
    reviewsdat = requests.get("https://jcvfukpccvibxumakqdh.supabase.co/rest/v1/reviews?select=id",headers={"apikey":sbkey,"Authorization":"Bearer "+sbkey})
    revs = reviewsdat.json()
    arr_ids = []
    for i in revs:
        arr_ids.append(i.get('id'))
    lid = get_largest_integer(arr_ids)
    return str(lid)

@apireview.route('/', methods=['POST'])
def post_review():
    reqdat = request.get_json()
    try:
        rvat = requests.post("https://jcvfukpccvibxumakqdh.supabase.co/rest/v1/reviews",
                  headers={
                     "apikey":sbkey,
                     "Authorization":"Bearer "+sbwritekey,
                     "Content-Type": "application/json",
                     "Prefer": "return=minimal"
                  },
                  data=json.dumps({
                     "id":int(getLatestID())+1,
                     "reviewer_name": str("Jane D."),
                     "stars":int(reqdat.get("stars")),
                     "commentary":str("Lorem ipsum dolor sit amet"),
                     "book_id":int(reqdat.get("book_id"))
                  }))
        return str(rvat.status_code)
    except Exception as e:
       return str("418: "+str(e))