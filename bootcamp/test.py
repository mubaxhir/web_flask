import unittest
import app

from flask import testing

class TodoAppTestCase(unittest.TestCase):
    def test_tasks(self):
        client = app.retrieve_list()
        rsp = client.get('/todo/api/v1.0/tasks')
        assert rsp.status == '200 OK'
