from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()
cr = certifi.where()
mongoconnectionstring = os.getenv("MONDGO_DB_CON_STRING")
client = MongoClient(mongoconnectionstring, tlsCAFile=cr)
db = client["FlaskAPI_Testing"]
chats = db["FlaskCollection1"]