import requests
from ..app import config

class OMDB():
    def __init__(self):
        self.params = {'apikey': config['DEFAULT']['OMDB_API_KEY']}
        self.URL = 'http://www.omdbapi.com/'

    def get_shows(self):
        params = self.params.copy()
        params['i'] = 'tt3896198'
        response = requests.get(self.URL, params)
        return response.json()

    def search_shows(self, search_string, page=1):
        params = self.params.copy()
        params['s'] = search_string
        response_raw = requests.get(self.URL, params)
        response = response_raw.json()

        return response
