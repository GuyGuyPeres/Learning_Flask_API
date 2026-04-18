from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)


task_id_counter = 4

tasks = [
    {
        "id": 1,
        "title": "Learn Flask",
        "completed": False
    },
        {
        "id": 2,
        "title": "Build API",
        "completed": False
    },
            {
        "id": 3,
        "title": "Tesy with postman",
        "completed": True
    }
    ]


@app.route('/tasks', methods=['GET', 'POST'])
def tasks1():
    if request.method == "POST":
        global task_id_counter
        title = request.json
        if not bool(title):
            return f"ERROR" , 400

        new_todo = {
            "id" : task_id_counter,
            "title" : title["title"],
            "completed" : False
        }

        task_id_counter += 1
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



@app.route('/tasks/<id>', methods=["GET", "PUT", "DELETE"])
def user(id):

    if request.method == "GET":
        success = False
        
        for task in tasks:
            if task["id"] == int(id):
                success = True
                return jsonify({
                    "success" : success,
                    "task" : task 
                })
        if success == False:
            return jsonify({
                "error" : "id not found",
                "id to search" : id
            })
            
            
    if request.method == "PUT":
        new_data = request.json
        for task in tasks:
            if task["id"] == int(id):
                task["completed"] = new_data["completed"]
                task["title"] = new_data["title"] 
                return f"{task} updated"
        
        return f"ERROR", 400
                
                
    if request.method == 'DELETE':
        for taskID, task in enumerate(tasks):
            if task["id"] == int(id):
                tasks.pop(taskID)
                return f"{id} has been deleted"
        return tasks
        
        
        



if __name__ == "__main__":
    app.run(debug=True)