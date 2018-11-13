import requests
import logging


class OMDB():
    def __init__(self):
        self.params = {'apikey': 'f4af6d88'}

    def get_shows(self):
        params = self.params.copy()
        params['i'] = 'tt3896198'
        response = requests.get('http://www.omdbapi.com/', params)
        return response.json()


def main():
    print('Hello World')
    ntflx = OMDB()
    print(ntflx.get_shows())


if __name__ == '__main__':
    main()