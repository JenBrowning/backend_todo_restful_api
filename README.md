Objective

For this assignment, you will create a RESTful API using Flask, that implements a TODO list.   The API methods will support CRUD (Create, Read, Update and Delete) for TODO Items.

Goal

The goal is to create the RESTful API as a backend application, not the front end web application.  A TODO item should contain the following information:

Title
Creation date
Last updated date
Due date
Completed (true/false)
Completion date

Your backend Flask application should implement API endpoints for the following:

List all TODO items
Retrieve a TODO item by Id
Update TODO information: title, due date, and completed
Delete a TODO item.

Notes

We don't need to store the information in a database in this assignment. We can define a simple data structure (e.g. dict) to store the TODO items and perform updates on that structure.

The title is a required field.

The creation date will be auto-generated by the back end.

Success Criteria:

Provide endpoints to get, create, update, delete Todo items.
Handle custom exception when a TODO item is not found.
Perform data validation on API inputs.

Use all coding and project layout idioms that you have learned so far:

PEP8
docstrings on methods
clean repo: No virtual environments or log files!
Discoverable unit tests for all api methods and responses

Curl commands:

delete - curl http://localhost:5000/todos/todo2 -X DELETE -v

get - curl http://localhost:5000/todos/todo3

get the list - 


add a new todo - curl http://localhost:5000/todos -d "task=something new" -X POST -v

update a todo - curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v
