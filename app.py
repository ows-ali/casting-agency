import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, setup_db

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)


  # @app.route('/', methods = ['GET'])
  # def index():

  #     return jsonify({
  #         'success': True,
  #         'message':'Backend of Capstone casting project is  Successfully connected.'})


  @app.route('/', methods=['GET'])
  def index():
    return jsonify({"Hello":'World'})

  return app

APP = create_app()

if __name__ == '__main__':

  APP.run(host='0.0.0.0', PORT=8080, debug=True)