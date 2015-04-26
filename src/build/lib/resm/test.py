# -*- coding: utf-8 -*-

import unittest
import json
from view import app

class TestService(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()        
       
    def test_resm_service(self):
        self._test_list()
        self._test_allocate()
        self._test_deallocate()
        self._test_reset()
        self._test_bad_request()

    def _test_list(self):
        resp = self.app.get('/list')     
        self.assertEqual({"allocated": {}, "deallocated": ["r1", "r2", "r3"]}, json.loads(resp.data))
        self.assertEqual("200 OK", resp.status)
        
    def _test_allocate(self):
        resp = self.app.get('/allocate/alice') 
        self.assertEqual("r1", resp.data)
        self.assertEqual("201 CREATED", resp.status)
        
        resp = self.app.get('/list')     
        self.assertEqual({"allocated": {"r1": "alice"}, "deallocated": ["r2", "r3"]}, json.loads(resp.data))
        
        self.app.get('/allocate/bob') 
        self.app.get('/allocate/alice') 
        
        resp = self.app.get('/allocate/bob') 
        self.assertEqual("Out of resources.", resp.data)
        self.assertEqual("503 SERVICE UNAVAILABLE", resp.status)
        
    def _test_deallocate(self):
        resp = self.app.get('/deallocate/r2') 
        self.assertEqual("204 NO CONTENT", resp.status)
        
        resp = self.app.get('/deallocate/r2') 
        self.assertEqual("Not allocated.", resp.data)
        self.assertEqual("404 NOT FOUND", resp.status)
        
    def _test_reset(self):
        resp = self.app.get('/reset') 
        self.assertEqual("204 NO CONTENT", resp.status)
        self._test_list()
        
    def _test_bad_request(self):
        resp = self.app.get('/get_me_all_resources') 
        self.assertEqual("Bad request.", resp.data)
        self.assertEqual("400 BAD REQUEST", resp.status)


def run():
    unittest.main()