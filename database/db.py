from flask_pymongo import PyMongo


def getDb(app):
    mongo = PyMongo(app)
    return mongo.db