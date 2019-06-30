# ============================================
#  Title:  User Service
#  Author: Tyler Armstrong
#  Date:   30 June 2019
#  Description: Updating and deleting documents using Python.
# ===========================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

db = client.web335

user = {

    "first_name": "Jesse",

    "last_name": "Freeman",

    "email": "freeman@me.com",

    "employee_id": "6825491",

    "date_created": datetime.datetime.utcnow()

}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one())