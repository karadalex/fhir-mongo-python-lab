import os
import json
from pymongo import MongoClient
from flask import Flask, Response
from bson import json_util


app = Flask(__name__)

client = MongoClient('mongodb://root:example@localhost:27017/')
db = client.fhir
fhir = db.fhir

@app.route("/")
def index():
    return Response(
        json_util.dumps(fhir.find().limit(1)[0]),
        mimetype='application/json'
    )