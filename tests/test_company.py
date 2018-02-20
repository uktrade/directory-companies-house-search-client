from unittest import TestCase

from directory_ch_client.company import CompanyCHClient
from tests import stub_request


class CompanyCHClientTest(TestCase):

    def setUp(self):
        self.client = CompanyCHClient(
            base_url='https://example.com', api_key='test'
        )

    @stub_request('https://example.com/api/search/companies/', 'get')
    def test_search_companies(self, stub):
        self.client.search_companies(query='acme')

        request = stub.request_history[0]

        assert 'q=acme' in request.url
