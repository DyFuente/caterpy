#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Subdivide list of urls into domains."""


import re
import requests
from tldextract import extract
from caterpy.tags import TOKEN_IDS, RESERVED_WORDS
from unidecode import unidecode
from nltk import pos_tag, download, word_tokenize
from collections import defaultdict, namedtuple, UserDict


download('punkt')
download('averaged_perceptron_tagger')

urls = defaultdict(lambda: False)
WORDS = re.compile(r"\w+")
NUMBERS = re.compile(r".*\d[.*]?")
NO_TAGS = re.compile(r"<[^>]+>")


class trans_words_dict(UserDict):
    """Create a dict to return own key if it don't exists."""
    def __getitem__(self, key):
        if key in self.data.keys():
            return self.data[key]
        elif key.endswith('s') and key[:-1] in self.data.keys():
            return self.data[key[:-1]]
        else:
            return key


class sum_words(UserDict):
    """Create a dict that sum a key value."""
    def __setitem__(self, key, item):
        if key in self.keys():
            self.data[key] = self.data[key] + item
        else:
            self.data[key] = item


def return_trans_dict():
    """Return a dict with translated words"""
    read_translated = [(x.split('|')[0].lower(), x.split('|')[1].lower())
                       for x in list(filter(None, open(
                               "files/translated", "r").read().split('\n')))]
    _trans_dict = trans_words_dict()
    for word, trans in read_translated:
        _trans_dict[unidecode(word)] = unidecode(trans)
    return _trans_dict


def url_info(url):
    """Return info of an url."""
    trans_words = return_trans_dict()
    _url = namedtuple('url', 'domain subdomain words')
    get_url = requests.get(url)
    if get_url.status_code == 200:
        tld = extract(url)
        _url.domain = tld.registered_domain
        _url.subdomain = tld.subdomain
        _url.words = sum_words()
        token_words = [pos_tag(word_tokenize(trans_words[unidecode(
            x.lower())]))[0] for x in WORDS.findall(NO_TAGS.sub(
                " ", get_url.text)) if not NUMBERS.match(x)
                       if x.lower() not in RESERVED_WORDS.split()
                       if len(x) >= 3]
        for word in [word for word, t_id in token_words
                     if t_id in TOKEN_IDS]:
            _url.words[word.lower()] = 1
    return _url
