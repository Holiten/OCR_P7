##############################################
################## GOOG API ##################
##############################################

from goog_api.goog_api import GoogleApi
from unittest.mock import patch


class MockResponse:
    def json(self):
        return {
            "candidates": [
                {
                    "formatted_address": "10 Quai de la Charente, 75019 Paris, France",
                    "geometry": {
                        "location": {
                            "lat": 48.8975156,
                            "lng": 2.3833993
                        },
                        "viewport": {
                            "northeast": {
                                "lat": 48.89886702989273,
                                "lng": 2.384756379892722
                            },
                            "southwest": {
                                "lat": 48.89616737010729,
                                "lng": 2.382056720107278
                            }
                        }
                    }
                }
            ],
            "status": "OK"
        }


@patch('requests.get', return_value=MockResponse())
def test_goog_fetch_infos_ok(mock_requests):
    g = GoogleApi()
    g.goog_fetch_infos("OpenClassRoom")
    assert g.google_coords == "48.8975156|2.3833993"
    assert g.google_adress == "10 Quai de la Charente, 75019 Paris, France"
    assert g.google_status == "OK"
