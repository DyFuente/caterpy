#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Subdivide list of urls into domains."""


import re
import requests
from tldextract import extract
from caterpy.tags import return_tags
from unidecode import unidecode
from nltk import pos_tag, download, word_tokenize, corpus
from collections import defaultdict, namedtuple, UserDict


TOKEN_IDS = return_tags('token_ids')
RESERVED_WORDS = return_tags('reserved_words')

download('punkt', quiet=True)
download('averaged_perceptron_tagger', quiet=True)
download('words', quiet=True)

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
    _read_translated = []

    for line in list(filter(
            None, open("/usr/local/etc/translated").readlines())):
        untranslated, translated, _ = list(filter(None, line.split('|')))
        _read_translated.append((unidecode(untranslated.lower().strip()),
                                 unidecode(translated.lower().strip())))

    _trans_dict = trans_words_dict()
    for untranslated, translated in _read_translated:
        _trans_dict[untranslated] = translated

    return _trans_dict


def return_valid_words(url_text, en, devel=False):
    """Return a list of words valid to the model."""
    _to_translate = set([])
    _valid_words = sum_words()
    trans_words = return_trans_dict()
    english_words = set(w.lower() for w in corpus.words.words())

    for word in WORDS.findall(NO_TAGS.sub(" ", url_text)):
        if len(word) > 3:
            _word = unidecode(word.lower().strip())
            _check_numbers = bool(NUMBERS.match(_word))
            if _word not in RESERVED_WORDS.split() and not _check_numbers:
                if en:
                    token = pos_tag(word_tokenize(trans_words[_word]))[0]
                    if token[1] in TOKEN_IDS and token[0] in english_words:
                        _valid_words[token[0]] = 1
                    elif token[0] not in english_words:
                        _to_translate.add(token[0])
                else:
                    if _word not in english_words:
                        _valid_words[_word] = 1

    if devel:
        if len(_to_translate) != 0:
            words_to_translate = [w for w in _to_translate
                                  if w not in trans_words.keys()]
            with open('/usr/local/etc/words_to_translate', 'a') as wtt:
                wtt.write("\n".join(words_to_translate))

    return _valid_words


def url_info(url, en=False):
    """Return info of an url."""
    _url = namedtuple('url', 'status domain subdomain words')
    _url.status = False
    try:
        get_url = requests.get(url)
        if get_url.status_code == 200:
            _url.status = True
            tld = extract(url)
            if tld.registered_domain != '':
                _url.domain = tld.registered_domain
            else:
                _url.domain = tld.domain
            _url.subdomain = tld.subdomain
            _url.words = return_valid_words(get_url.text, en)
    except Exception as error:
        print(error)

    return _url
