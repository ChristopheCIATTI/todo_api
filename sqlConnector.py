import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        database="python_todo_list_api"
    )