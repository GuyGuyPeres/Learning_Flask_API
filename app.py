
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
from HAFRADA_routes import tasks_bp
from HAFRADA_errors import errors_bp
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv
load_dotenv()

# #! ////////////////////////////////////////////////////////////////////////
# #! DATABASE:
# cr = certifi.where()
# mongoconnectionstring = os.getenv("MONDGO_DB_CON_STRING")
# client = MongoClient(mongoconnectionstring, tlsCAFile=cr)
# db = client["FlaskAPI_Testing"]
# todos = db["TodosCollection"]
# #! //////////////////////////////////////////////////////////////////////



app = Flask(__name__)

app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)


if __name__ == '__main__':
    app.run(debug=True)