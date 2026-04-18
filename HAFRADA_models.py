import uuid
from bson import ObjectId
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity, HTTPException, MethodNotAllowed
from database import todos


# tasks = [
#     {
#         "id": "1",
#         "title": "Learn Flask",
#         "completed": False
#     },
#         {
#         "id": "2",
#         "title": "Build API",
#         "completed": False
#     },
#             {
#         "id": "3",
#         "title": "Test with postman",
#         "completed": True
#     }
#     ]

def get_all_tasks():
    all_todos = list(todos.find())
    for task in all_todos:
        task["_id"] = str(task["_id"])
        
    return all_todos


def get_task_by_id(task_id):
    try:
        # MongoDB uses objectId - we convert the string from "Routes" to this object.
        needed_task = todos.find_one({"_id": ObjectId(task_id)})
    except Exception:
        # if the ID is in the incorrect MongoDB format. 
        raise NotFound(f"Invalid ID format: {task_id}")
    
    needed_task = todos.find_one({"_id": ObjectId(task_id)})
    if needed_task:
        # conversion of _id to string to we can return in it JSON.
        needed_task["_id"] = str(needed_task["_id"])
        return jsonify(needed_task)
    else:
        raise NotFound(f"Task with ID {task_id} not found")
        
        
def create_task(task_data):
    
    if not task_data or "title" not in task_data:
        raise BadRequest("Missing required field: 'title'")

    new_task = {
        "title" : task_data["title"],
        "completed" : False
    }

    todos.insert_one(new_task) # here the "_id" becomes objectId and we need to convert it to string.
    
    new_task["_id"] = str(new_task["_id"]) # here _id becomes a string 
    
    return jsonify({
        "success": True,
        "new_task": new_task
    })
    
def update_task_with_put(task_id):
    new_data = request.json
    
    # validating the input
    if not new_data or "title" not in new_data or not new_data["title"].strip():
        raise UnprocessableEntity("Title must contain text and cannot be empty and cannot have spaces")
    
    # הכנת האובייקט לעדכון
    update_fields = {
        "title": new_data["title"]
    }
    
    # add 'completed' only if it was sent
    if "completed" in new_data:
        update_fields["completed"] = new_data["completed"]

    try:
        # edit the specific task with the data the user entered.
        # $set מעדכן רק את השדות ששלחנו ושומר על שאר השדות הקיימים
        result = todos.update_one(
            {"_id": ObjectId(task_id)}, 
            {"$set": update_fields}
        )
    except Exception:
        raise NotFound(f"Invalid ID format: {task_id}")

    if result.matched_count == 0:
        raise NotFound(f"Task with ID {task_id} not found")

    return f"Task {task_id} updated successfully"
        
        
def delete_a_task_by_id(task_id):
    try:
        # delete the specific task by the id (in the objectId format)
        result = todos.delete_one({"_id": ObjectId(task_id)})
    except Exception:
        # if the id is not in the correct mongoDB format.
        raise NotFound(f"Invalid ID format: {task_id}")

    # if deleted_count (mongoDB method) is 1 after the delete request it worked, if it is 0 it did not work.
    if result.deleted_count == 0:
        raise NotFound(f"Task with ID {task_id} not found")

    return f"Task with ID {task_id} has been successfully deleted"
