
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv
load_dotenv()


#! ////////////////////////////////////////////////////////////////////////
#! DATABASE:
cr = certifi.where()
mongoconnectionstring = os.getenv("MONDGO_DB_CON_STRING")
client = MongoClient(mongoconnectionstring, tlsCAFile=cr)
db = client["FlaskAPI_Testing"]
todos = db["TodosCollection"]
#! //////////////////////////////////////////////////////////////////////

