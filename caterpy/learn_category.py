#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Learn category based on a count of words."""


import threading
from requests_html import HTMLSession
from caterpy.url_lists import url_lists
from caterpy.get_url_info import url_info, sum_words


global words
words = sum_words()


def expand_urls(cat_lists, unknow=False):
    session = HTMLSession()
    if cat_lists.startswith('http'):
        urls_to_expand = [cat_lists]
    else:
        urls_to_expand = url_lists[cat_lists]
    expanded_urls = set(urls_to_expand)
    for url in urls_to_expand:
        try:
            req = session.get(url)
            for x in [u.attrs['href'] for u in req.html.find('a')
                      if 'href' in u.attrs]:
                if x.startswith("/"):
                    expanded_urls.add(url+x)
                if unknow:
                    if x.startswith("http") or x.startswith("www"):
                        expanded_urls.add(x)
        except Exception:
            pass
    return expanded_urls


def thread_url_info(_url, log=False):
    global words
    try:
        _url_info = url_info(_url)
        if _url_info:
            for word, value in _url_info.words.items():
                words[word] = value
        if log:
            print(len(words))
    except Exception as error:
        if log:
            print(error)
        pass


def cat_words(cat, unknow=False):
    """Count words of a category based on an url list."""
    global words
    for url in expand_urls(cat, unknow):
        if threading.activeCount() < 5:
            start_thread = threading.Thread(target=thread_url_info, args=[url])
            start_thread.start()
            start_thread.join()
    return words
