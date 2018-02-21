from directory_ch_client.base import BaseCHClient
from directory_ch_client.company import CompanyCHClient


class DirectoryCHClient(BaseCHClient):

    endpoints = {
        'ping': 'healthcheck/ping/',
    }

    def __init__(self, base_url=None, api_key=None):
        super(DirectoryCHClient, self).__init__(base_url, api_key)

        self.company = CompanyCHClient(base_url, api_key)

    def ping(self):
        return self.get(url=self.endpoints['ping'])
