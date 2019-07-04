import pkg_resources

from django.conf import settings

from directory_client_core.base import AbstractAPIClient
from directory_ch_client.company import CompanyCHClient


class DirectoryCHClient(AbstractAPIClient):

    endpoints = {
        'ping': 'healthcheck/ping/',
    }

    version = pkg_resources.get_distribution(__package__).version

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = CompanyCHClient(*args, **kwargs)

    def ping(self):
        return self.get(url=self.endpoints['ping'])


ch_search_api_client = DirectoryCHClient(
    base_url=settings.DIRECTORY_CH_SEARCH_CLIENT_BASE_URL,
    api_key=settings.DIRECTORY_CH_SEARCH_CLIENT_API_KEY,
    sender_id=settings.DIRECTORY_CH_SEARCH_CLIENT_SENDER_ID,
    timeout=settings.DIRECTORY_CH_SEARCH_CLIENT_DEFAULT_TIMEOUT,
)
