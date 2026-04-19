from flask import jsonify, request, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
import uuid
from models.task import get_all_tasks, get_task_by_id, create_task, update_task_with_put, delete_a_task_by_id
from models.list import get_list_by_id
from config.database import get_collection

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
def tasks1():
    if request.method == "GET":
        list_id = request.args.get("list_id")
        return jsonify(get_all_tasks(list_id=list_id))

    if request.method == "POST":
        new_data = request.json or {}
        list_id = new_data.get("list_id")
        if list_id:
            if not get_list_by_id(list_id):
                raise NotFound(f"List {list_id} not found")
        return create_task(new_data)


@tasks_bp.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def user(id):

    if request.method == "GET":
        return get_task_by_id(id)
            
            
    if request.method == "PUT":
        return jsonify(update_task_with_put(id))
                
                
    if request.method == 'DELETE':  
        return jsonify(delete_a_task_by_id(id))
    
        
        