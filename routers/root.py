from flask_restful import Resource

class Root(Resource):
    def get(self):
        return {'hello': 'world'}

def set_route(api):
    api.add_resource(Root, '/')