from unittest import TestCase

from directory_ch_client.company import CompanyCHClient
from tests import stub_request


class CompanyCHClientTest(TestCase):

    def setUp(self):
        self.base_url = 'https://example.com'
        self.api_key = 'test'
        self.client = CompanyCHClient(
            base_url=self.base_url,
            api_key=self.api_key,
            sender_id='test',
            timeout=5,
        )

    @stub_request('https://example.com/api/search/companies/', 'get')
    def test_search_companies(self, stub):
        self.client.search_companies(query='acme')

        request = stub.request_history[0]

        assert 'q=acme' in request.url

    @stub_request(
        'https://example.com/api/company/1/registered-office-address/',
        'get'
    )
    def test_get_company_registered_address(self, stub):
        self.client.get_company_registered_address(company_number=1)

        request = stub.request_history[0]

        assert request.url == \
            'https://example.com/api/company/1/registered-office-address/'

    @stub_request('https://example.com/api/company/1/', 'get')
    def test_get_company_profile(self, stub):
        self.client.get_company_profile(company_number=1)

        request = stub.request_history[0]

        assert request.url == 'https://example.com/api/company/1/'

    @stub_request('/api/company/1/officers/', 'get')
    def test_list_officers(self, stub):
        self.client.list_officers(company_number=1)

        request = stub.request_history[0]

        assert request.url == 'https://example.com/api/company/1/officers/'
