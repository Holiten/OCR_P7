##############################################
################## GOOG API ##################
##############################################

from goog_api.goog_api import GoogleApi
from unittest.mock import patch


class MockResponse:
    def json(self):
        return {'candidates': [], 'status': 'ZERO_RESULTS'}


@patch('requests.get', return_value=MockResponse())
def test_fetch_infos_zero(mock_request):
    g = GoogleApi()
    g.fetch_infos("fvazveda")
    assert g.google_status == "ZERO_RESULTS"
