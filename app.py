import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import db_drop_and_create_all, setup_db, Movie, Actor, Scene
from auth import AuthError, requires_auth

from datetime import datetime


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    """ uncomment at the first time running the app """
    # db_drop_and_create_all()

    @app.route('/', methods=['GET'])
    def hi():
        return jsonify({
            'greeting': 'Welcome to my API. Thank your for using it',
            'Heroku_live_link': 'https://casting-fsnd.herokuapp.com',
        })

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors_query = Actor.query.all()
            formatted_actors = [actor.details() for actor in actors_query]
            return jsonify({
                'success': True,
                'actors': formatted_actors
            }), 200
        except Exception:
            abort(500)

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies_query = Movie.query.all()
            formatted_movies = [movie.details() for movie in movies_query]
            return jsonify({
                'success': True,
                'movies': formatted_movies
            }), 200
        except Exception:
            abort(500)

    @app.route('/actors/<int:id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_specific_actor(payload, id):
        try:
            actor_query = Actor.query.filter_by(id=id).first()
            formatted_actor = actor_query.details()
            actor_query.delete()
            return jsonify({
                'success': True,
                'deleted_actor': formatted_actor
            }), 200
        except Exception:
            abort(404)

    @app.route('/movies/<int:id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_specific_movie(payload, id):
        try:
            movie_query = Movie.query.filter_by(id=id).first()
            formatted_movie = movie_query.details()
            movie_query.delete()
            return jsonify({
                'success': True,
                'deleted_movie': formatted_movie
            }), 200
        except Exception:
            abort(404)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def add_new_actor(payload):
        req_data = request.get_json()

        print(req_data)

        name = req_data.get('name')
        age = req_data.get('age')
        gender = req_data.get('gender')

        try:
            new_actor = Actor(name=name, age=age, gender=gender)
            new_actor.insert()

            formatted_actor = new_actor.details()

            return jsonify({
                'success': True,
                'new_actor': formatted_actor
            }), 200
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def add_new_movie(payload):
        req_data = request.get_json()

        print(req_data)

        title = req_data.get('title')
        year = req_data.get('year')
        month = req_data.get('month')
        day = req_data.get('day')

        try:
            release_date = datetime(year=year, month=month, day=day)
            movie = Movie(title=title, release_date=release_date)
            movie.insert()

            formatted_movie = movie.details()

            return jsonify({
                'success': True,
                'new_movie': formatted_movie
            }), 200
        except Exception:
            abort(422)

    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def modify_specific_actor(payload, id):
        req_data = request.get_json()

        print(req_data)

        name = req_data.get('name', None)
        age = req_data.get('age', None)
        gender = req_data.get('gender', None)

        actor_query = Actor.query.filter_by(id=id).first()

        if name:
            actor_query.name = name
        if age:
            actor_query.age = age
        if gender:
            actor_query.gender = gender

        try:
            actor_query.update()

            formatted_actor = actor_query.details()

            return jsonify({
                'success': True,
                'modified_actor': formatted_actor
            }), 200
        except Exception:
            abort(422)

    @app.route('/movies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def modify_specific_movie(payload, id):
        req_data = request.get_json()

        print(req_data)

        title = req_data.get('title', None)
        year = req_data.get('year', None)
        month = req_data.get('month', None)
        day = req_data.get('day', None)

        movie_query = Movie.query.filter_by(id=id).first()
        release_date = movie_query.release_date
        print("release_date:", release_date)

        if title:
            movie_query.title = title
        if year:
            movie_query.release_date = release_date.replace(year=year)
        if month:
            movie_query.release_date = release_date.replace(month=month)
        if day:
            movie_query.release_date = release_date.replace(day=day)

        try:
            movie_query.update()

            formatted_movie = movie_query.details()

            return jsonify({
                'success': True,
                'modified_movie': formatted_movie
            }), 200
        except Exception:
            abort(422)

    # ...................... Error handling .........................

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "server error"
        }), 500

    @app.errorhandler(AuthError)
    def Auth_Error(e):
        return jsonify({
            "success": False,
            "error": e.status_code,
            "message": e.error['description']
        }), e.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
