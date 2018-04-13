#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Subdivide list of urls into domains."""


import re
import requests
from tldextract import extract
from collections import defaultdict, namedtuple, UserDict


urls = defaultdict(lambda: False)
WORDS = re.compile(r"\w+")
NO_TAGS = re.compile(r"<[^>]+>")


class sum_words(UserDict):
    """Create a dict that sum a key value."""
    def __setitem__(self, key, item):
        if key in self.keys():
            self.data[key] = self.data[key] + item
        else:
            self.data[key] = item


def url_info(url):
    """Return info of an url."""
    _url = namedtuple('url', 'domain subdomain words')
    get_url = requests.get(url)
    if get_url.status_code == 200:
        tld = extract(url)
        _url.domain = tld.registered_domain
        _url.subdomain = tld.subdomain
        _url.words = sum_words()
        for word in [x for x in WORDS.findall(NO_TAGS.sub(" ", get_url.text))]:
            _url.words[word] = 1
    return _url
