from contextlib import nullcontext
from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import time
import supabase

# Blueprints enable python code to be organized in multiple files and directories https://flask.palletsprojects.com/en/2.2.x/blueprints/
review_api = Blueprint('review_api', __name__,
                   url_prefix='/api/reviews')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(review_api)

"""Time Keeper
Returns:
    Boolean: is it time to update?
"""
def updateTime():
    global last_run  # the last_run global is preserved between calls to function
    try: last_run
    except: last_run = None
    
    # initialize last_run data
    if last_run is None:
        last_run = time.time()
        return True
    
    # calculate time since last update
    elapsed = time.time() - last_run
    if elapsed > 240:  # update every 2 minutes
        last_run = time.time()
        return True
    
    return False

"""API Handler
Returns:
    String: API response
"""   
def getReviewAPI():
    global review_data  # the review_data global is preserved between calls to function
    try: review_data
    except: review_data = None

    """
    Preserve Service usage / speed time with a Reasonable refresh delay
    """
    if updateTime():
        
        #ADD CODE TO FETCH DATA!
        

        review_data = response
    else:  # Request Covid Data
        response = review_data

    return response


"""API with Country Filter
Returns:
    String: Filter of API response
"""   
def getCountry(filter):
    # Request Covid Data
    response = getReviewAPI()
    # Look for Country    
    countries = response.json().get('countries_stat')
    for country in countries:  # countries is a list
        if country["country_name"].lower() == filter.lower():  # this filters for country
            return country
    
    return {"message": filter + " not found"}


"""Defines API Resources 
  URLs are defined with api.add_resource
"""   
class CovidAPI:
    """API Method to GET all Covid Data"""
    class _Read(Resource):
        def get(self):
            return getReviewAPI().json()
        
    """API Method to GET Covid Data for a Specific Country"""
    class _ReadCountry(Resource):
        def get(self, filter):
            return jsonify(getCountry(filter))
    
    # resource is called an endpoint: base usr + prefix + endpoint
    api.add_resource(_Read, '/')
    api.add_resource(_ReadCountry, '/<string:filter>')


"""Main or Tester Condition 
  This code only runs when this file is "played" directly
"""        
if __name__ == "__main__": 
    """
    Using this test code is how I built the backend logic around this API.  
    There were at least 10 debugging session, on handling updateTime.
    """
    
    print("-"*30) # cosmetic separator

    # This code looks for "world data"
    response = getReviewAPI()
    print("World Totals")
    world = response.json().get('world_total')  # turn response to json() so we can extract "world_total"
    for key, value in world.items():  # this finds key, value pairs in country
        print(key, value)

    print("-"*30)

    # This code looks for USA in "countries_stats"
    country = getCountry("USA")
    print("USA Totals")
    for key, value in country.items():
        print(key, value)
        
    print("-"*30)
