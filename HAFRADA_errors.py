
from flask import Flask, jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed

errors_bp = Blueprint("errors", __name__)

app = Flask(__name__)

@errors_bp.app_errorhandler(NotFound)
def handle_not_found(e):
    return jsonify({
        "status": 404,
        "message": e.description,
        "error": "NotFound"
    }), 404

@errors_bp.app_errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({
        "status": 400,
        "message": e.description,
        "error": "BadRequest"
    }), 400

@errors_bp.app_errorhandler(MethodNotAllowed)
def handle_method_allowed(e):
    return jsonify({
        "status": 405,
        "message": "This method is not allowed on this endpoint",
        "error": "MethodNotAllowed"
    }), 405
    
@errors_bp.app_errorhandler(UnprocessableEntity)
def handle_method_allowed(e):
    return jsonify({
        "status": 403,
        "error": e.description,
        "message": "UnprocessableEntity"
    }), 403
















# @errors_bp.app_errorhandler(TypeError)
# def handle_type_error(e):
#     return jsonify({
#         "status": 400,
#         "message": str(e),
#         "error": "TypeError"
#     }), 400
    
    
# @errors_bp.app_errorhandler(UnprocessableEntity)
# def handle_type_error(e):
#     return jsonify({
#         "status": 400,
#         "message": str(e),
#         "error": "UnprocessableEntity"
#     }), 400
    

