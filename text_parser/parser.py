#!/usr/bin/python3
# coding: utf-8

import os
import json
from text_parser.remove_chars import list_chars

actual_folder = os.path.dirname(__file__)
stopwords_folder = "\\remove_chars"
full_path = actual_folder + stopwords_folder

with open(full_path + '\\stopwords_fr.json', 'rb') as f:
    stopwords = json.load(f)


class Parser:
    """Object allowing to parse a sentence from a user text"""

    def __init__(self, user_text):
        """Initialization of the text_pars with the user text"""
        self.user_text = user_text

    def remove_uppercase(self):
        """Parser method to remove uppercase chars"""
        self.user_text = self.user_text.lower()

    def remove_special_char(self):
        """Parser method to remove special characters"""
        for char in self.user_text:
            if char in list_chars.list_a:
                self.user_text = self.user_text.replace(char, 'a')

            elif char in list_chars.list_ae:
                self.user_text = self.user_text.replace(char, 'ae')

            elif char in list_chars.list_oe:
                self.user_text = self.user_text.replace(char, 'oe')

            elif char in list_chars.list_c:
                self.user_text = self.user_text.replace(char, 'c')

            elif char in list_chars.list_e:
                self.user_text = self.user_text.replace(char, 'e')

            elif char in list_chars.list_i:
                self.user_text = self.user_text.replace(char, 'i')

            elif char in list_chars.list_d:
                self.user_text = self.user_text.replace(char, 'd')

            elif char in list_chars.list_n:
                self.user_text = self.user_text.replace(char, 'n')

            elif char in list_chars.list_o:
                self.user_text = self.user_text.replace(char, 'o')

            elif char in list_chars.list_s:
                self.user_text = self.user_text.replace(char, 's')

            elif char in list_chars.list_u:
                self.user_text = self.user_text.replace(char, 'u')

            elif char in list_chars.list_y:
                self.user_text = self.user_text.replace(char, 'y')

            elif char in list_chars.list_other:
                self.user_text = self.user_text.replace(char, '')

            else:
                pass

    def remove_double_space(self):
        """Parser method to remove double spaces"""
        self.user_text = self.user_text.replace('  ', ' ')

    def remove_stopwords(self):
        """Parser method allowing to remove stopwords from a given list via a json file"""
        self.user_text = self.user_text.split(' ')
        i = 0
        while i < 10:
            for word in stopwords:
                try:
                    self.user_text.remove(word)
                except ValueError:
                    pass
            i = i + 1
        self.user_text = ' '.join(self.user_text)

    def call_all_methods(self):
        """Parser method allowing to launch all the methods at once"""
        self.remove_uppercase()
        self.remove_special_char()
        self.remove_double_space()
        self.remove_stopwords()
        print(self.user_text)
        return self.user_text
