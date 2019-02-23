import requests


class RequestHandler:

    requests_dict = {
        'POST': requests.post,
        'GET': requests.get
    }

    @staticmethod
    def request(url: str, request_type: str, headers: dict = None, data: dict = None, cookies: dict = None,
                allow_redirects: bool = False):

        try:
            response = RequestHandler.requests_dict[request_type](url, headers=headers, data=data, cookies=cookies,
                                                                  allow_redirects=allow_redirects)
        except requests.ConnectionError as e:
            print('Connection Error', e)
            return e
        except requests.HTTPError as e:
            print('Abnormal HTTP Response', e)
            return e
        except requests.Timeout as e:
            print('Timeout', e)
            return e
        except requests.TooManyRedirects as e:
            print('Too many redirects', e)
            return e

        return response
