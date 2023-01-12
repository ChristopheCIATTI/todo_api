import sqlConnector as mysql
import json

class TaskDao():
    def __init__(self):
        self.sql = mysql.mydb
        self.sql_cursor = self.sql.cursor()

    def getAllTask(self):
        self.sql_cursor
        self.sql_cursor.execute("SELECT * FROM todo_list")
        result = self.sql_cursor.fetchall()
        return json.dumps(result)

    def getTask(self, id):
        self.sql_cursor
        self.sql_cursor.execute(""" SELECT * FROM todo_list WHERE id = %s """, (id, ))
        result = self.sql_cursor.fetchall()
        return json.dumps(result)

    def updateTask(self, id, value):
        id = id
        value = value

        self.sql_cursor
        self.sql_cursor.execute(""" UPDATE todo_list SET task = %s WHERE id = %s """, (value, id))
        self.sql.commit()

    def addTask(self, value):
        new_task = value
        self.sql_cursor
        self.sql_cursor.execute(""" INSERT INTO todo_list (task) VALUES (%s) """, (new_task,))
        self.sql.commit()

    def deleteTask(self, id):
        self.sql_cursor
        self.sql_cursor.execute(""" DELETE FROM todo_list WHERE id = %s """, (id, ))
        self.sql.commit()

