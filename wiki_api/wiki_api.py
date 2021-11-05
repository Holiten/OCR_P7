#!/usr/bin/python3
# coding: utf-8

import requests
from config import WIKI_URL, WIKI_API_URL


class WikiApi:
    """Object allowing the use of Wikipedia API"""

    def __init__(self):
        """Initialization of the WikiApi object"""
        self.wiki_api_url = WIKI_API_URL
        self.wiki_page_id = int
        self.wiki_title = str
        self.wiki_extract = str
        self.wiki_url = str
        self.wiki_error = str

    def wiki_fetch_infos(self, goog_coords):
        wiki_query_params = {
            "action": "query",
            "generator": "geosearch",
            "ggsradius": 400,
            "ggscoord": goog_coords,
            "prop": "extracts",
            "explaintext": True,
            "exsentences": 2,
            "exlimit": 1,
            "redirects": True,
            "format": "json",
            "formatversion": 2,
        }

        wiki_r = requests.get(self.wiki_api_url, params=wiki_query_params)
        wiki_j = wiki_r.json()
        print(wiki_j)

        try:
            self.wiki_page_id = wiki_j['query']['pages'][0]['pageid']
            self.wiki_title = wiki_j['query']['pages'][0]['title']
            self.wiki_extract = wiki_j['query']['pages'][0]['extract']
            self.wiki_url = WIKI_URL + str(self.wiki_page_id)

            return self.wiki_page_id, self.wiki_title, self.wiki_extract, self.wiki_url

        except KeyError:
            print("La recherche n'a pas pu aboutir")
            self.wiki_error = "ZERO_RESULTS"
            return self.wiki_error
            # Faire parler le bot --PHRASE D'ERREUR--
