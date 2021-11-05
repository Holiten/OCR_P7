##############################################
################# GEO WIKI ###################
##############################################

from wiki_api.wiki_api import WikiApi
from unittest.mock import patch


class MockResponse:
    def json(self):
        return {
            "continue": {
                "excontinue": 1,
                "continue": "||"
            },
            "query": {
                "pages": [
                    {
                        "pageid": 271433,
                        "ns": 0,
                        "title": "Avenue Corentin-Cariou",
                        "index": -1,
                        "extract": "L'avenue Corentin-Cariou est une avenue du 19e arrondissement de Paris.\n\n\n== "
                                   "Situation et accès ==\nCette avenue prolonge l'avenue de Flandre jusqu'à l'avenue "
                                   "de la Porte-de-la-Villette et la porte de la Villette historique. "
                    },
                    {
                        "pageid": 512073,
                        "ns": 0,
                        "title": "Porte de la Villette (métro de Paris)",
                        "index": 0
                    },
                    {
                        "pageid": 2960707,
                        "ns": 0,
                        "title": "Porte de la Villette",
                        "index": 1
                    },
                    {
                        "pageid": 3120618,
                        "ns": 0,
                        "title": "Quai de la Charente",
                        "index": 2
                    },
                    {
                        "pageid": 3120649,
                        "ns": 0,
                        "title": "Quai de la Gironde",
                        "index": 3
                    },
                    {
                        "pageid": 3120923,
                        "ns": 0,
                        "title": "Quai du Lot",
                        "index": 4
                    },
                    {
                        "pageid": 3124793,
                        "ns": 0,
                        "title": "Square du Quai-de-la-Gironde",
                        "index": 5
                    },
                    {
                        "pageid": 5422631,
                        "ns": 0,
                        "title": "Rue Benjamin-Constant",
                        "index": 6
                    },
                    {
                        "pageid": 7065484,
                        "ns": 0,
                        "title": "Gare du pont de Flandre",
                        "index": 7
                    },
                    {
                        "pageid": 11988883,
                        "ns": 0,
                        "title": "Parc du Pont de Flandre",
                        "index": 8
                    }
                ]
            }
        }


@patch('requests.get', return_value=MockResponse())
def test_wiki_geo_search(mock_requests):
    w = WikiApi()
    w.wiki_fetch_infos("48.8975156|2.3833993")
    assert w.wiki_page_id == 271433
    assert w.wiki_title == "Avenue Corentin-Cariou"
    assert w.wiki_url == "https://fr.wikipedia.org/?curid=271433"
