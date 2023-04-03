import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, setup_db, db_drop_and_create_all, Movies, Actors
from auth.auth import requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  db_drop_and_create_all(app)
  CORS(app)


  # @app.route('/', methods = ['GET'])
  # def index():

  #     return jsonify({
  #         'success': True,
  #         'message':'Backend of Capstone casting project is  Successfully connected.'})


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
  
    return jsonify({"resp":resp})


  @app.route('/movies',methods=['POST'])
  @requires_auth('post:movies')
  def postmovie(payload):
    # actors = Actors.query.all()
    req = request.get_json()
    title= req.get('title','')
    date= req.get('date','')

    movie = Movies(title,date)
    # movie.title = req['title']
    # movie.data= req['date']
    movie.insert()
    
    # resp=[]
    # for actor in actors:
    #   movie = Movies.query.get(actor.movie_id)

    #   act = {

      
    #     'id' :  actor.id,
    #     'name' : actor.name,
    #     'age' : actor.age,
    #     'gender' : actor.gender,
    #     'movie': movie.title
        

    #   }
      # resp.append(act)
      
    return jsonify({"status":200, "resp":movie.id})

  @app.route('/movies',methods=['PATCH'])
  @requires_auth('patch:movies')
  def patchmovie(payload):
    # actors = Actors.query.all()

    try:
      req = request.get_json()
      title= req.get('title','')
      date= req.get('date','')

      movie = Movies.query.get(id)
      
      # movie.title = req['title']
      # movie.data= req['date']
      movie.insert()
      
      # resp=[]
      # for actor in actors:
      #   movie = Movies.query.get(actor.movie_id)

      #   act = {

        
      #     'id' :  actor.id,
      #     'name' : actor.name,
      #     'age' : actor.age,
      #     'gender' : actor.gender,
      #     'movie': movie.title
          

      #   }
        # resp.append(act)
    except Exception as e:
        abort(422,{'message': {'message': str(e)}})

    return jsonify({"status":200, "resp":movie.id})



  @app.route('/actors',methods=['GET'])
  @requires_auth('get:actors')
  def actors(payload):
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
      
    return jsonify({"resp":resp})


  @app.route('/actors',methods=['POST'])
  @requires_auth('post:actors')
  def postactor(payload):

    req = request.get_json()
    name= req.get('name','')
    age= req.get('age','')
    gender= req.get('gender','')

    actor = Actors(name,age,gender, None)
    
    actor.insert()
    


      
    return jsonify({"status":200, "resp":actor.id})



  return app


app = create_app()

if __name__ == '__main__':

  app.run(host='0.0.0.0', port=8080, debug=True)