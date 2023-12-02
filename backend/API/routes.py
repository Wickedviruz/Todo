from flask import Blueprint, request, jsonify
from API.models import TodoList, db
from sqlalchemy import asc

api = Blueprint('api', __name__)

# Laddar in alla todo listor
@api.route('/', methods=['GET'])
def home():
    todo_lists = TodoList.query.order_by(asc(TodoList.id)).all()
    lists = []
    for list in todo_lists:
        lists.append({'status': list.done,'name': list.name, 'information': list.information, 'id': list.id})
    return jsonify({'lists': lists})

# Lägger till en todo lista
@api.route('/add_todo', methods=['POST'])
def add_todo():
    if request.method == 'POST':
        todo_list = TodoList(name=request.json['name'], information=request.json['information'])
        db.session.add(todo_list)
        db.session.commit()
        return jsonify({'message': 'Todo list added successfully!'})
    else:
        return jsonify({'message': 'NOt correct data'})
    
@api.route('/get_todo/<int:id>', methods=['GET'])
def get_todo_list(id):
    todo = TodoList.query.get(id)
    if todo:
        return jsonify({'lists': [{'name': todo.name, 'information': todo.information, 'id': todo.id}]})
    else:
        return jsonify({'message': 'Todo not found'}), 404
    
# Uppdaterar en todo lista    
@api.route('/update_todo/<int:id>', methods=['PUT'])
def update_todo_list(id):
    todo_list = TodoList.query.get(id)
    todo_list.name = request.json['name']
    todo_list.information = request.json['information']
    db.session.commit()
    return jsonify({'message': 'Todo list updated successfully!'})

# Assuming you have a route like this to handle the PUT request
@api.route('/update_status/<int:id>', methods=['PUT'])
def update_status(id):
    todo_list = TodoList.query.get(id)
    todo_list.done = request.json['status']
    db.session.commit()
    return jsonify({'message': 'Todo status updated successfully'}), 200

# Tar bort en todo lista
@api.route('/delete_todo/<int:id>', methods=['DELETE'])
def delete_todo_list(id):
    todo_list = TodoList.query.get(id)
    db.session.delete(todo_list)
    db.session.commit()
    return jsonify({'message': 'Todo list deleted successfully!'})