#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import datetime


app = Flask(__name__)
api = Api(app)

todos = {}
todo_id = 0
current_datetime = datetime.datetime.now()


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, message="This To Do Item {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, default="Please enter a title")
parser.add_argument('due_date', type=str, default="When is this due?")
parser.add_argument('completed', type=bool, default=False)


class TodoList(Resource):
    """Create a To Do List for yo'self"""

    def get(self):
        return todos

    def post(self):
        global todo_id
        args = parser.parse_args()
        todo_id = int(todo_id) + 1
        todo_id = str(todo_id)
        todos[todo_id] = {
            "completed_date": str(current_datetime),
            "creation_date": str(current_datetime),
            "last_update": str(current_datetime),
            "title": args["title"],
            "completed": args["completed"],
            "due_date": args["due_date"]
        }
        return todo_id, 201


class TodoItem(Resource):
    """Create some To Do Items for yo'self"""
    def get(self, todo_id):
        return todos[todo_id]

    def put(self):
        """update a todo item"""
        args = parser.parse_args()
        if args['title']:
            todos[todo_id].update({'title': args['title']})
        if args['creation_date']:
            todos[todo_id].update({'created on': str(current_datetime)})
        if args['last_update']:
            todos[todo_id].update({'Updated on': str(current_datetime)})
        if args['completed']:
            todos[todo_id].update({'completed': args['completed']})
            if args['completed']is True:
                todos[todo_id].update({'Completed on': str(current_datetime)})
            if args['completed']is False:
                todos[todo_id].update({'competed_date': 'Seriously??'})
        if args['completed_date']:
            todos[todo_id].update({'completed_date': str(current_datetime)})
        return 201

    def delete_item(self, todo_id):
        """Deletes a to do item on the list"""
        abort_if_todo_doesnt_exist(todo_id)
        del todos[todo_id]

        return 204
api.add_resource(TodoList, '/todos')
api.add_resource(TodoItem, '/todos/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)  