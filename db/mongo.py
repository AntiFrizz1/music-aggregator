from flask_mongoengine import MongoEngine

mongo = MongoEngine()


def initialize_mongo_db(app):
    mongo.init_app(app)

