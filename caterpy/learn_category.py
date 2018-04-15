#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Learn category based on a count of words."""


from requests_html import HTMLSession
from caterpy.url_lists import url_lists
from caterpy.get_url_info import url_info, sum_words


def expand_urls(cat_lists, unknow=False):
    session = HTMLSession()
    expanded_urls = set([])
    for url in url_lists[cat_lists]:
        req = session.get(url)
        for x in [u.attrs['href'] for u in req.html.find('a')
                  if 'href' in u.attrs]:
            if x.startswith("/"):
                expanded_urls.add(url+x)
            if unknow:
                if x.startswith("http") or x.startswith("www"):
                    expanded_urls.add(x)
    return expanded_urls


def cat_words(cat):
    """Count words of a category based on an url list."""
    words = sum_words()
    for url in expand_urls(cat):
        try:
            _url_info = url_info(url)
            if _url_info:
                for word, value in _url_info.words.items():
                    words[word] = value
        except Exception as error:
            print(error)
    return words
