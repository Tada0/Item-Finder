from src.Requests.RequestHandler import RequestHandler
import requests
from unittest import TestCase


class TestRequestHandler(TestCase):

    def test_url_wrong(self):
        #  When url is wrong
        self.assertRaises(requests.exceptions.MissingSchema, RequestHandler.request, '2', 'GET')
        self.assertRaises(requests.exceptions.MissingSchema, RequestHandler.request, True, 'GET')
        self.assertEqual(requests.exceptions.ConnectionError, type(RequestHandler.request('http://gogo.gogo', 'GET')))
        self.assertEqual(requests.exceptions.ConnectionError, type(RequestHandler.request('http://de56.957', 'GET')))

    def test_url_correct(self):
        #  When url is correct
        self.assertEqual(requests.models.Response, type(RequestHandler.request('https://www.google.com', 'GET')))
        self.assertEqual(requests.models.Response, type(RequestHandler.request('https://www.fb.com', 'GET')))

    def test_request_type_wrong(self):
        self.assertRaises(KeyError, RequestHandler.request, 'https://www.google.com', 'd')
        self.assertRaises(KeyError, RequestHandler.request, 'https://www.google.com', 12)
        self.assertRaises(KeyError, RequestHandler.request, 'https://www.google.com', 5+3j)
        self.assertRaises(KeyError, RequestHandler.request, 'https://www.google.com', True)

    def test_request_type_correct(self):
        self.assertEqual(requests.models.Response, type(RequestHandler.request('https://www.google.com', 'GET')))
        self.assertEqual(requests.models.Response, type(RequestHandler.request('https://www.google.com', 'POST')))

