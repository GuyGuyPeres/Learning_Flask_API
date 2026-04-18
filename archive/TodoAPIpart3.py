from flask import Flask, jsonify, request
from datetime import datetime, timezone
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
import uuid

#! THIS IS PART 3   <-------------

app = Flask(__name__)


# task_id_counter = 4

tasks = [
    {
        "id": "1",
        "title": "Learn Flask",
        "completed": False
    },
        {
        "id": "2",
        "title": "Build API",
        "completed": False
    },
            {
        "id": "3",
        "title": "Tesy with postman",
        "completed": True
    }
    ]


@app.errorhandler(TypeError)
def handle_type_error(e):
    return jsonify({
        "status": 400,
        "message": str(e),
        "error": "TypeError"
    }), 400
    
@app.errorhandler(NotFound)
def handle_type_error(e):
    return jsonify({
        "status": 404,
        "message": str(e),
        "error": "NotFound"
    }), 404
    
@app.errorhandler(BadRequest)
def handle_type_error(e):
    return jsonify({
        "status": 405,
        "message": str(e),
        "error": "BadRequest"
    }), 405
    
@app.errorhandler(UnprocessableEntity)
def handle_type_error(e):
    return jsonify({
        "status": 400,
        "message": str(e),
        "error": "UnprocessableEntity"
    }), 400



@app.route('/tasks', methods=['GET', 'POST'])
def tasks1():
    
    
    if request.method == "POST":
        # global task_id_counter
        data = request.json
        title = data["title"]
        
        if not title.strip():
            raise BadRequest("The title can not be empty or with spaces only")

        new_todo = {
            "id" : str(uuid.uuid4()),
            "title" : title,
            "completed" : False
        }


        tasks.append(new_todo)
        return jsonify({
            "success" : True,
            "the new todo we created: ": new_todo
        }), 200


    if request.method == "GET":
        all = []
        for task in tasks:
            all.append(task)
        return all


    # raise BadRequest("METHOD NOT ALLOWED") #TODO need to understand how do it. 


@app.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def user(id):

    if request.method == "GET":
        success = False
    
        for task in tasks:
            if task["id"] == id:
                success = True
                return jsonify({
                    "success" : success,
                    "task" : task 
                })
        if success == False:
            raise NotFound("wrong id was given, nothing is found")
            
            
    if request.method == "PUT":
        new_data = request.json
        
        if not bool(new_data):
            raise NotFound("user didnt give anything!")
        
        if "completed" not in new_data or "title" not in new_data:
            raise BadRequest("user didnt give 'completed' or 'title' !!!")
        
        
        for task in tasks:
            if task["id"] == id:
                if "completed" in new_data:
                    task["completed"] = new_data["completed"]
                if "title" in new_data:
                    task["title"] = new_data["title"]
                     
                return f"{task} updated"
                
                
    if request.method == 'DELETE':
        DELETE_success = False
        for taskID, task in enumerate(tasks):
            if task["id"] == id:
                tasks.pop(taskID)
                DELETE_success = True
                return f"{id} has been deleted"
        return tasks
    
    if DELETE_success == False:
        raise NotFound("delete did not work! check the id you gave again.")
        
        
        



if __name__ == "__main__":
    app.run(debug=True)