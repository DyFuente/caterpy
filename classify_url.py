#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classify an url by category."""


import argparse
from caterpy.learn_category import cat_words
from caterpy.get_models import return_models


def classify_url(_opts):
    """Retrun categories and the propability of url pertences each one"""
    try:
        _url_words = cat_words(_opts.url, _opts.expand_urls)
        _models = return_models(limit=_opts.limit_words)
        _data = []
        for model in _models:
            _data.append([model, sum([1 for u in _url_words
                                     if u in _models[model]])/len(_url_words)])
        print("\nCategories for {}\n".format(_opts.url))
        for model, prob in list(sorted(_data, key=lambda i: i[1],
                                       reverse=True))[:_opts.limit_class]:
            print("  Categoria {}: {}".format(model, prob))
    except Exception as error:
        print("Error: {}\nType -h to get help.".format(error))


def return_args():
    """Parse options to classify url."""
    _parser = argparse.ArgumentParser(add_help=True, description=(
        "Return some classes for url classified."))
    _parser.add_argument("-u", "--url", action="store", required=True,
                         help="Url to classify with scheme.")
    _parser.add_argument("-c", "--limit_class", action="store", default=-1,
                         type=int, help="Limit number of classes to show.")
    _parser.add_argument("-w", "--limit_words", action="store", default=-1,
                         type=int, help=(
                             "Limit number of words used to classify."))
    _parser.add_argument("-e", "--expand_urls", action="store_true",
                         default=False, help=(
                             "Limit number of words used to classify."))
    return _parser.parse_args()


if __name__ == "__main__":
    opts = return_args()
    classify_url(opts)
