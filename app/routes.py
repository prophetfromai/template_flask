# app/routes.py

from flask_restx import Namespace, Resource, fields

api = Namespace('todos', description='TODO operations')

# Define a model for Swagger documentation
todo_model = api.model('Todo', {
    'id': fields.String(required=True, description='The task identifier'),
    'task': fields.String(required=True, description='The task details')
})

TODOS = {
    'todo1': {'task': 'Build an API'},
    'todo2': {'task': 'Write docs'},
    'todo3': {'task': 'Test the app'},
}


@api.route('/<string:id>')
@api.doc(params={'id': 'The task ID'})
class TodoResource(Resource):
    @api.doc(description='Get a task by its ID')
    @api.marshal_with(todo_model)
    def get(self, id):
        """Fetch a given resource"""
        if id not in TODOS:
            api.abort(404, "Todo {} doesn't exist".format(id))
        return {'id': id, 'task': TODOS[id]['task']}

    @api.doc(description='Delete a task by its ID')
    def delete(self, id):
        """Delete a task given its identifier"""
        if id not in TODOS:
            api.abort(404, "Todo {} doesn't exist".format(id))
        del TODOS[id]
        return '', 204
