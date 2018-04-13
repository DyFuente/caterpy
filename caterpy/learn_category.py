#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Learn category based on a count of words."""


from caterpy.url_lists import url_lists
from caterpy.get_url_info import url_info, sum_words


def cat_words(cat):
    """Count words of a category based on an url list."""
    words = sum_words()
    for url in url_lists[cat]:
        try:
            _url_info = url_info(url)
            if _url_info:
                for word, value in _url_info.words.items():
                    words[word] = value
        except Exception as error:
            print(error)
    return words
