import random
import unittest
from app import create_app


    


class FlaskTestCase(unittest.TestCase):
    """ Define setUp app test"""
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        #self.app.debug = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()


    """ This is one of potentially many TestCases """  
    def test_route_hello_world(self):
        res = self.client.get("/")
        # print(dir(res), res.status_code)
        assert res.status_code == 200
        assert b"Hello World" in res.data

    def test_route_foo(self):
        res = self.client.get("/foo/12345")
        assert res.status_code == 200
        assert b"12345" in res.data


if __name__ == '__main__':
    unittest.main()
