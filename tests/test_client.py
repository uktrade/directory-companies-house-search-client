from unittest import TestCase

from directory_ch_client.client import DirectoryCHClient
from directory_ch_client.company import CompanyCHClient

from tests import stub_request


class DirectoryCHClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://example.com'
        self.key = 'test'
        self.client = DirectoryCHClient(self.base_url, self.key)

    def test_company(self):
        assert isinstance(self.client.company, CompanyCHClient)
        assert self.client.company.base_url == self.base_url
        assert self.client.company.request_signer.secret == self.key

    @stub_request('https://example.com/healthcheck/ping/', 'get')
    def test_ping(self, stub):
        self.client.ping()

        request = stub.request_history[0]
        assert request
