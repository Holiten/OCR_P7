#!/usr/bin/python3
# coding: utf-8

import os
import requests
from config import GOOGLE_URL


class GoogleApi:
    """Object allowing the use of Google API"""

    def __init__(self):
        """Initialization of the GoogleApi object"""
        self.google_url = GOOGLE_URL
        self.google_lat = str
        self.google_long = str
        self.google_coords = str
        self.google_adress = str
        self.google_status = int

    def fetch_infos(self, user_input):
        """GoogleApi method to fetch coords (lat & long) from Google API"""
        google_params = {
            "key": os.environ["GOOGLE_KEY"],
            "input": user_input,
            "inputtype": "textquery",
            "fields": "formatted_address,geometry",
        }

        google_r = requests.get(self.google_url, params=google_params)
        google_j = google_r.json()
        print(google_j)

        self.google_status = google_j['status']

        if self.google_status == 'OK':
            self.google_lat = google_j['candidates'][0]['geometry']['location']['lat']
            self.google_long = google_j['candidates'][0]['geometry']['location']['lng']
            self.google_coords = str(self.google_lat) + "|" + str(self.google_long)
            self.google_adress = google_j['candidates'][0]['formatted_address']

            return self.google_coords, self.google_adress, self.google_status

        else:
            print("Merci de refaire une recherche")
            # Faire parler le bot --PHRASE D'ERREUR--
