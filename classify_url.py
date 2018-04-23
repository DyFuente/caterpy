#!/usr/bin/ena python3
# -*- coding: utf-8 -*-
"""Classify an url by category."""


from __future__ import division
from caterpy.learn_category import cat_words
from caterpy.get_models import return_models


def classify_url(url, limit=-1):
    """Retrun categories and the propability of url pertences each one"""
    _url_words = cat_words(url)
    _models = return_models()
    _data = []
    for model in _models:
        _data.append([model, sum([1 for u in _url_words
                                 if u in _models[model]])/len(_url_words)])
    print("\nCategories for {}\n".format(url))
    for model, prob in list(sorted(_data, key=lambda i: i[1],
                                   reverse=True))[:limit]:
        print("  Categoria {}: {}".format(model, prob))


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(("Usage: classify_url.py <url> <number of classes>\n"
               "  Number of classes is optional, url must contain scheme.\n"))
    elif len(sys.argv) == 3:
        classify_url(sys.argv[1], int(sys.argv[2]))
    else:
        classify_url(sys.argv[1])
