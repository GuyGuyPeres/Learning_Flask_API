
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
# todos = db["TodosCollection"]
#! //////////////////////////////////////////////////////////////////////

_client = None
_db = None

def init_db(app):
    global _client, _db
    _client = client
    _db = db
    app.config["DB"] = _db
    
def get_collection(name):
    return _db[name]

