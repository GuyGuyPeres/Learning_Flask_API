
from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
from HAFRADA_routes import tasks_bp
from HAFRADA_errors import errors_bp
from database import init_db
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

init_db(app)
app.register_blueprint(tasks_bp)
app.register_blueprint(errors_bp)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)