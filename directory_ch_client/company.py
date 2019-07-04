import pkg_resources

from directory_client_core.base import AbstractAPIClient


class CompanyCHClient(AbstractAPIClient):

    endpoints = {
        'search-companies': '/api/search/companies/',
        'registered-address':
            '/api/company/{company_number}/registered-office-address/',
        'profile': '/api/company/{company_number}/',
        'officers': '/api/company/{company_number}/officers/',
    }
    version = pkg_resources.get_distribution(__package__).version

    def search_companies(self, query):
        return self.get(
            self.endpoints['search-companies'],
            params={'q': query}
        )

    def get_company_registered_address(self, company_number):
        url = self.endpoints['registered-address'].format(
            company_number=company_number
        )
        return self.get(url)

    def get_company_profile(self, company_number):
        url = self.endpoints['profile'].format(company_number=company_number)
        return self.get(url)

    def list_officers(self, company_number):
        url = self.endpoints['officers'].format(company_number=company_number)
        return self.get(url)
