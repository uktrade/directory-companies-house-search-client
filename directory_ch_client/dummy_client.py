import http
from unittest.mock import patch, MagicMock

from requests import Response

from directory_ch_client.client import DirectoryCHClient


class DummyDirectoryCHClient(DirectoryCHClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        patch.object(self.company, 'send', self.send).start()

    @patch('requests.Session.send')
    def send(self, mock_send, *args, **kwargs):
        response = Response()
        response.status_code = http.client.BAD_REQUEST
        response.json = lambda: MagicMock()
        mock_send.return_value = response
        return super().send(*args, **kwargs)
