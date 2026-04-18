from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
import uuid
from HAFRADA_models import get_all_tasks, get_task_by_id, create_task, update_task_with_put, delete_a_task_by_id
from database import todos

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
def tasks1():
    

    if request.method == "GET":
        return jsonify(get_all_tasks())
    
        
    if request.method == "POST":
        new_data = request.json
        return create_task(new_data)


@tasks_bp.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def user(id):

    if request.method == "GET":
        return get_task_by_id(id)
            
            
    if request.method == "PUT":
        return jsonify(update_task_with_put(id))
                
                
    if request.method == 'DELETE':  
        return jsonify(delete_a_task_by_id(id))
    
        
        