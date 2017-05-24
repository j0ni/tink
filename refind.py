import requests

class Error(Exception):
    pass

class FeedFailure(Error):
    def __init__(self, url, resp):
        self.url = url
        self.response = resp


def get_feed(url='https://refind.com/j0ni.json'):
    resp = requests.get(url)
    if resp.status_code != 200:
        raise FeedFailure(url, resp)
    else:
        return resp.json()

        


