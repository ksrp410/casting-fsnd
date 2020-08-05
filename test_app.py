import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from app import create_app
from models import setup_db, Movie, Actor


load_dotenv()


class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        database_name = "casting_agency_test"
        project_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.getenv("postgresql://{}:{}@{}/{}".format(
            'postgres','postgres410','localhost:5432',database_name))

        setup_db(self.app)

        self.producer_headers = os.environ.get('PRODUCER_TOKEN')
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create/drop all tables

    def tearDown(self):
        """Executed after reach test"""
        pass


# ................................................ POST: /actors endpoint test ................................................

    def test_01_post_actors(self):
        result = self.client().post('/actors',
                                 json={"name": "mayar", "age": 15,
                                       "gender": "female"},
                                 headers={'Authorization':
                                          'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])

    def test_02_401_sent_requesting_post_actors_without_auth_header(self):
        result = self.client().post('/actors',
                                 json={"name": "Halaaaa", "age": 15, "gender": "female"})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ POST: /movies endpoint test ................................................
    def test_03_post_movies(self):
        result = self.client().post('/movies',
                                 json={"title": "myshs movie",
                                       "year": 2024, "month": 12, "day": 10},
                                 headers={'Authorization':
                                          'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])

    def test_04_401_sent_requesting_post_movies_without_auth_header(self):
        result = self.client().post('/movies',
                                 json={"title": "ss movie", "year": 2024, "month": 12, "day": 10})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ GET: /actors endpoint test ................................................
    def test_05_get_actors(self):
        result = self.client().get('/actors', headers={'Authorization':
                                                    'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_06_401_sent_requesting_actors_without_auth_header(self):
        result = self.client().get('/actors')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ GET: /movies endpoint test ................................................
    def test_07_get_movies(self):
        result = self.client().get('/movies', headers={'Authorization':
                                                    'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_08_401_sent_requesting_movies_without_auth_header(self):
        result = self.client().get('/movies')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ PATCH: /actors endpoint test ................................................
    def test_09_patch_actors(self):
        result = self.client().patch('/actors/10',
                                  json={"age": 20}, headers={'Authorization':
                                                             'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['modified_actor'])

    def test_010_401_sent_requesting_patch_actors_without_auth_header(self):
        result = self.client().patch('/actors/9',
                                  json={"age": 22})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ PATCH: /movies endpoint test ................................................
    def test_011_patch_movies(self):
        result = self.client().patch('/movies/1',
                                  json={"title": "wow"}, headers={'Authorization':
                                                                  'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['modified_movie'])

    def test_012_401_sent_requesting_patch_movies_without_auth_header(self):
        result = self.client().patch('/movies/1',
                                  json={"title": "woow"})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ DELETE: /actors endpoint test ................................................

    def test_013_delete_actors(self):
        result = self.client().delete('/actors/11', headers={'Authorization':
                                                          'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_actor'])

    def test_014_401_sent_requesting_delete_actors_without_auth_header(self):
        result = self.client().delete('/actors/1')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')

    # ................................................ DELETE: /movies endpoint test ................................................
    def test_015_delete_movies(self):
        result = self.client().delete('/movies/3', headers={'Authorization':
                                                         'Bearer ' + self.producer_headers})
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted_movie'])

    def test_016_401_sent_requesting_delete_movies_without_auth_header(self):
        result = self.client().delete('/movies/1')
        data = json.loads(result.data)

        self.assertEqual(result.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
