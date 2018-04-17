#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Subdivide list of urls into domains."""


import re
import requests
from tldextract import extract
from caterpy.tags import TOKEN_IDS
from nltk import pos_tag, download, word_tokenize
from collections import defaultdict, namedtuple, UserDict


download('punkt')
download('averaged_perceptron_tagger')

urls = defaultdict(lambda: False)
WORDS = re.compile(r"\w+")
NUMBERS = re.compile(r"\d+")
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
        token_words = [pos_tag(word_tokenize(x))[0] for x in WORDS.findall(
            NO_TAGS.sub(" ", get_url.text)) if not NUMBERS.match(x)]
        for word in [word for word, t_id in token_words
                     if t_id in TOKEN_IDS]:
            _url.words[word] = 1
    return _url
