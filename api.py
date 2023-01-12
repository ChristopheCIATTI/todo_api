from flask import Flask
from flask import request
from flask_restful import reqparse, abort, Api, Resource
import json

import sqlConnector as mysql
from taskDao import TaskDao

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

class Todo(Resource):
    def __init__(self):
        self.sql = mysql.mydb
        self.sql_cursor = self.sql.cursor()

    def get(self, todo_id):
        task = TaskDao.getTask(self, todo_id)
        return task

    def delete(self, todo_id):
        TaskDao.deleteTask(self, todo_id)
        return 204

    def put(self, todo_id):
        data = request.get_json(force=True)
        task = data["task"]
        TaskDao.updateTask(self, todo_id, task)
        return 201

class TodoList(Resource):
    def __init__(self):
        self.sql = mysql.mydb
        self.sql_cursor = self.sql.cursor()

    def get(self):
        tasks = TaskDao.getAllTask(self)
        return tasks

    def post(self):
        data = request.get_json(force=True)
        new_task = data["task"]
        TaskDao.addTask(self, new_task)
        return 200
