import api

if __name__ == "__main__":

    main_api = api.api
    main_app = api.app 

    main_api.add_resource(api.TodoList, '/todos')
    main_api.add_resource(api.Todo, '/todos/<todo_id>')

    main_app.run(debug = True)
