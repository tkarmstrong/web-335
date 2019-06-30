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

db.users.update_one(

    {"employee_id": "6825491"},

    {
        "$set": {
            "email": "tkarmstrong@my365.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "6825491"}))