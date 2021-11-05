##############################################
################# GEO WIKI ###################
##############################################

from wiki_api.wiki_api import WikiApi
from unittest.mock import patch


class MockResponse:
    def json(self):
        return {}


@patch('requests.get', return_value=MockResponse())
def test_wiki_geo_search(mock_requests):
    w = WikiApi()
    w.wiki_fetch_infos("x|x")
    assert w.wiki_error == "ZERO_RESULTS"
