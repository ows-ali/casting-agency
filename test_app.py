
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db,db_drop_and_create_all


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""

        self.bearerToken = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFMZWJENlVXUG52aWY4aUtJZEJ4YiJ9.eyJpc3MiOiJodHRwczovL2Rldi1jNjdhY3NoaW51bjF2dDU1LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NDI4ZGYyZDAwNjZhNmVlZTkzMWI4YjMiLCJhdWQiOiJjYXBzdG9uZS1hcGktaWRlbiIsImlhdCI6MTY4MDUzNDY1MSwiZXhwIjoxNjgwNTQxODUxLCJhenAiOiJoSkNMcmZKYUdCQ0JJTG5VTUFsZ3Q3cndzWkNld2tSTyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3IiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.bY3fheelAU8zPsfjXdzCNrtivJnaACDwWAuERzaM-mK_X-vmvIbgCa86whpDPm_tkDJaIgDz5gHexYviTWahGkaDXhfLNLMaXhm3ZBLX7IiqAuNWrWx_neDVbIsd0oMPnRZhwILkEshjZxj0XPPUL2eEaYO0MkmY9od4tt2sL1vbzbQKSPZN4HMR1tcgZQFcMoQjgswM2liXEN42_f6RnotMu6RXpjfUV_ZtKoGeV4NOmuzAbyHwAhLFxjSS5rk0suizsi5aE_ZrStoDy1AfTjpfZDaIISz9654Vm_mXAFF5Y-3H4fYdCgazfjXsSF-L2mX08GscYnOg8LSwApBF_A'

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency"
        self.database_path = "postgresql://{}/{}".format('postgres:12345@localhost:5433', self.database_name)

        setup_db(self.app, self.database_path)
        db_drop_and_create_all(self.app)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
    
    
    def tearDown(self):
        """Executed after reach test"""
        with self.app.app_context():
            self.db.drop_all()

        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_get_movies(self):
        
        res = self.client().get('/movies', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)
        print('sdf')
        print (res.data)
        data = json.loads(res.data)

        print('...get moveis')
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')




    def test_get_actors(self):
        
        res = self.client().get('/actors', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        data = json.loads(res.data)
        print('...get actors')
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], False)
            self.assertTrue(len(data['resp'])==1)


    def test_get_movie_by_id(self):
        
        res = self.client().get('/movies/1', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        data = json.loads(res.data)
        print('...get movie by  i')
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')


    def test_get_actor_by_id(self):
        
        res = self.client().get('/actors/1', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        data = json.loads(res.data)
        print('...get actor by  i')
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')


    def test_post_movie(self):
        
        
        movie = {
            'title' : 'Zindabhaag',
            'date' : '2022-03-24'
        } 
        res = self.client().post('/movies', json=movie, headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...post movie ')
        # print(res.data)
        data = json.loads(res.data)
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            self.assertEqual(data['resp'],2)

    

    def test_post_actor(self):
        
        
        actor = {
            'title' : 'Ali Zafar',
            'age' : '24',
            'gender': 'Male',
            'movie_id':1
        } 
        res = self.client().post('/actors', json=actor, headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...post actor ')
        # print(res.data)
        data = json.loads(res.data)
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            self.assertEqual(data['resp'],2)

    def test_patch_movie(self):
        
        movie = {
            'title' : 'Movie updated',
            'date' : '2022-03-12'
        } 
        res = self.client().patch('/movies/1', json=movie, headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...patch movie ')
        # print(res.data)
        data = json.loads(res.data)
        # print('ppp')
        # print(data['resp'])
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            
            self.assertEqual(data['resp'],1)


    def test_patch_actor(self):
        
        actor = {
            'name' : 'Mahira',
            'age' : '20',
            'gender': 'Female'
        } 
        res = self.client().patch('/actors/1', json=actor, headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...patch actor ')
        # print(res.data)
        data = json.loads(res.data)
        # print('ppp')
        # print(data['resp'])
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            
            self.assertEqual(data['resp'],1)

    

    def test_delete_movie(self):
        

        res = self.client().delete('/movies/1', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...delete movie')
        # print(res.data)
        data = json.loads(res.data)
        # print('ppp')
        # print(data['resp'])
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            
            self.assertEqual(data['resp'],1)
        else:
            self.assertEqual(data['success'], False)


        

    def test_delete_actor(self):
        

        res = self.client().delete('/actors/1', headers={"Authorization":self.bearerToken})

        # res =  self.client(self).get('/movies', headers=self.bearerTokenExecProd)

        print('...delete actor')
        # print(res.data)
        data = json.loads(res.data)
        # print('ppp')
        # print(data['resp'])
        # print(data)
        if res.status_code ==401:

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data['success'],False)

        elif res.status_code==200:
            self.assertEqual(data['status'], 'OK')
            
            self.assertEqual(data['resp'],1)
        else:
            self.assertEqual(data['success'], False)


        

    def test_error(self):
        

        res = self.client().delete('/actors/1', headers={"Authorization":""})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
    

    

if __name__ == "__main__":
    unittest.main()
