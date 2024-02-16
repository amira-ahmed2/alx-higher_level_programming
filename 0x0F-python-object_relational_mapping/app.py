from flask import Flask
# import flask_mysqldb import SqlAlchemy

import sqlalchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///:db.sqlite3:'
