import requests

class BaseClient:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, path, params=None):
        return requests.get(f'{self.base_url}{path}', params=params, headers=self.headers)

    def post(self, path, json=None):
        return requests.post(f'{self.base_url}{path}', json=json, headers=self.headers)

    def put(self, path, json=None):
        return requests.put(f'{self.base_url}{path}', json=json, headers=self.headers)

    def delete(self, path):
        return requests.delete(f'{self.base_url}{path}', headers=self.headers)