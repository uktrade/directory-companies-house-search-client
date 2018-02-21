from unittest import TestCase

from directory_ch_client.company import CompanyCHClient
from directory_ch_client.dummy_client import DummyDirectoryCHClient


class DirectoryCHExternalClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://ch.com'
        self.api_key = 'test'
        self.client = DummyDirectoryCHClient(
            self.base_url, self.api_key
        )

    def test_company(self):
        company = self.client.company
        assert isinstance(company, CompanyCHClient)
        assert company.base_url == self.base_url
        assert company.request_signer.secret == self.api_key
