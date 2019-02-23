from src.Requests.RequestHandler import RequestHandler
import requests
import unittest


class TestRequestHandler(unittest.TestCase):

    def test_url_wrong(self):
        #  When url is wrong
        self.assertRaises(requests.exceptions.MissingSchema, RequestHandler.request, '2', 'GET')
        r = RequestHandler.request('http://gogo.gogo', 'GET')
        self.assertEqual(type(r), requests.exceptions.ConnectionError)

    def test_url_correct(self):
        #  When url is correct
        r = RequestHandler.request('https://www.google.com', 'GET')
        self.assertEqual(type(r), requests.models.Response)