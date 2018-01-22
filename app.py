from flask import Flask
from flask_restful import Resource, Api
from lib.add_routers import add_routers

app = Flask(__name__)
api = Api(app)
add_routers(api)

if __name__ == '__main__':
    app.run(debug=True)