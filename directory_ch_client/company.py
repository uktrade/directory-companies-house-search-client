from directory_ch_client.base import BaseCHClient


class CompanyCHClient(BaseCHClient):

    endpoints = {
        'search-companies': '/api/search/companies/',
    }

    def search_companies(self, query):
        return self.get(
            self.endpoints['search-companies'],
            params={'q': query}
        )
