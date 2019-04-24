#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from flask import Flask, render_template, jsonify, request
# app = Flask(__name__)

# todos = {}
# # app.debug = True

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/todo/")
# def get_todos():
#     return jsonify(todo=todos)

# @app.route("/todo/", methods=['POST'])
# def create_todo():
#     todo = request.get_json()
#     if len(todos) == 0:
#         todos[0] = todo['name']
#     else:
#         todos[max(todos.keys()) + 1] = todo['name']
#     return jsonify(todo=todos)

# @app.route("/todo/<int:id>")
# def read_todo(id):
#     todo = todos[id]
#     return jsonify(todo=todos)

# @app.route("/todo/<int:id>", methods=['PUT'])
# def update_todo(id):
#     todo = request.get_json()
#     todos[id] = todo['name']
#     return jsonify(todo=todos)

# @app.route("/todo/<int:id>", methods=['DELETE'])
# def delete_todo(id):
#     todos.pop(id, None)
#     return jsonify(todo=todos)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)

todos = {}
todo_id = 0
current_datetime = datetime.datetime.now()


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, default="Please enter a title")
parser.add_argument('due_date', type=str, default="When do you need this done?")
parser.add_argument('completed', type=bool, default=False)


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

class Update_todo(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        

##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')


if __name__ == '__main__':
    app.run(debug=True)