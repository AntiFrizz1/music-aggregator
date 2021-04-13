from flask_sqlalchemy import SQLAlchemy

sql_db = SQLAlchemy()


def initialize_sql_db(app):
    sql_db.init_app(app)
