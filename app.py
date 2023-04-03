import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, setup_db, db_drop_and_create_all, Movies, Actors
from auth.auth import requires_auth, AuthError

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  db_drop_and_create_all(app)
  CORS(app)
  


  @app.route('/', methods=['GET'])
  def index():
    return jsonify({"Hello":'World'})

  @app.route('/movies',methods=['GET'])
  @requires_auth('get:movies')
  def movies(payload):
    
    try:
      movies = Movies.query.all()
      
      resp=[]
      for movie in movies:
        mov = {

        
          'id' :  movie.id,
          'title' : movie.title,
          'date' : movie.date,
          'actors': []
        }
        actors=movie.actors
        print('movie.actors')
        print(movie.actors)
        movActors = []
        for actor in actors:
          movActors.append({
            'id':actor.id,
            'name':actor.name,
            'age':actor.age,
            'gender': actor.gender

          })
        mov['actors'] = movActors
        resp.append(mov)
    except Exception as e:
      abort(422,{'message': {'message': str(e)}})
  
    return jsonify({"resp":resp, "status":"OK"})


  @app.route('/movies/<id>',methods=['GET'])
  @requires_auth('get:movie')
  def getmovie(payload,id):
    
    try:
      movie = Movies.query.get(id)
      
      resp=[]

      mov = {
        'id' :  movie.id,
        'title' : movie.title,
        'date' : movie.date,
        
      }
      actors=movie.actors
      # print('movie.actors')
      # print(movie.actors)
      movActors = []
      for actor in actors:
        movActors.append({
          'id':actor.id,
          'name':actor.name,
          'age':actor.age,
          'gender': actor.gender

        })
      mov['actors'] = movActors
      resp.append(mov)
    except Exception as e:
      abort(422,{'message': {'message': str(e)}})
  
    return jsonify({"resp":resp,"status":"OK"})

  @app.route('/movies',methods=['POST'])
  @requires_auth('post:movies')
  def postmovie(payload):
    try:
      # actors = Actors.query.all()
      req = request.get_json()
      title= req.get('title','')
      date= req.get('date','')

      movie = Movies(title,date)

      movie.insert()
      

    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

      
    return jsonify({"status":200, "resp":movie.id,"status":"OK"})

  @app.route('/movies/<int:id>',methods=['PATCH'])
  @requires_auth('patch:movies')
  def patchmovie(payload,id):
    # actors = Actors.query.all()

    try:
      req = request.get_json()
      title= req.get('title','')
      date= req.get('date','')

      movie = Movies.query.get(id)
      
      movie.title = title
      movie.date= date
      movie.update()
      
      
    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify({ "resp":movie.id,"status":"OK"})


  @app.route('/movies/<int:id>',methods=['DELETE'])
  @requires_auth('delete:movies')
  def deletemovie(payload,id):
    
    
    try:
      req = request.get_json()

      movie = Movies.query.get(id)

      movie.delete()


    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify({ "resp":movie.id,"status":"OK"})


  @app.route('/actors',methods=['GET'])
  @requires_auth('get:actors')
  def actors(payload):
    try:
      actors = Actors.query.all()
      
      resp=[]
      for actor in actors:
        movie = Movies.query.get(actor.movie_id)
        print('movvvvvvv',movie)
        print('movvvvvvv',actor.movie_id, actor.name)
        movieName = "NA"
        if movie:
          movieName =movie.title

        act = {

        
          'id' :  actor.id,
          'name' : actor.name,
          'age' : actor.age,
          'gender' : actor.gender,
          'movie': movieName
          

        }
        resp.append(act)
    except Exception as e:
        abort(422,{'message': {'message': str(e)}})
      
    return jsonify({"resp":resp,"status":"OK"})

  @app.route('/actors/<id>',methods=['GET'])
  @requires_auth('get:actor')
  def getactor(payload,id):
    
    try:
      actor = Actors.query.get(id)
      
      resp=[]
      movie = Movies.query.get(actor.movie_id)
      print('movvvvvvv',movie)
      print('movvvvvvv',actor.movie_id, actor.name)
      movieName = "NA"
      if movie:
        movieName =movie.title

      act = {
      
        'id' :  actor.id,
        'name' : actor.name,
        'age' : actor.age,
        'gender' : actor.gender,
        'movie': movieName
        

      }
      resp.append(act)
    except Exception as e:
      abort(422,{'message': {'message': str(e)}})
  
    return jsonify({"resp":resp,"status":"OK"})


  @app.route('/actors',methods=['POST'])
  @requires_auth('post:actors')
  def postactor(payload):

    try:
      req = request.get_json()
      name= req.get('name','')
      age= req.get('age','')
      gender= req.get('gender','')

      actor = Actors(name,age,gender, None)
      
      actor.insert()
    except Exception as e:
      abort(422,{'message': {'message': str(e)}})

    


      
    return jsonify({ "resp":actor.id,"status":"OK"})


  @app.route('/actors/<int:id>',methods=['PATCH'])
  @requires_auth('patch:actors')
  def patchactor(payload,id):
    
    try:
      req = request.get_json()
      name= req.get('name','')
      age= req.get('age','')
      gender= req.get('gender','')
      movie_id= req.get('movie_id','')

      actor = Actors.query.get(id)
      
      actor.name = name
      actor.age= age
      actor.gender= gender
      actor.movie_id= movie_id

      actor.update()


    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify({"resp":actor.id,"status":"OK"})


  @app.route('/actors/<int:id>',methods=['DELETE'])
  @requires_auth('delete:actors')
  def deleteactor(payload,id):
    
    try:
      req = request.get_json()

      actor = Actors.query.get(id)

      actor.delete()


    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify({ "resp":actor.id,"status":"OK"})


  @app.errorhandler(400)
  def error401(error):
      return jsonify({
              "success": False,
              "error": 400,
              "message":error.description.get('message', '404-Not found')
              }), 400

  @app.errorhandler(404)
  def error404(error):
      return jsonify({
              "success": False,
              "error": 404,
              "message": error.description.get('message', 'invalid JSON body')
              }), 404





  # Error Handling
  '''
  Example error handling for unprocessable entity
  '''
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": error.description.get('message', 'unprocessable')
    }), 422


  @app.errorhandler(403)
  def error403(error):
      return jsonify({
              "success": False,
              "error": 403,
              "message": error.description.get('message', 'Unauthorized')
              }), 404


  @app.errorhandler(AuthError)
  def permissionFailed(auth_error):
      return jsonify({
          "success": False,
          "error": auth_error.status_code,
          "message": auth_error.error
      }), 401

  return app
  



app = create_app()

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=8080, debug=True)