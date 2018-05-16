#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Update classifier files with words and count."""


import argparse
from caterpy.learn_category import cat_words


def return_args():
    """Get some args to update classifiers."""
    _parser = argparse.ArgumentParser(add_help=True, description=(
        "Update classifiers into directory classifiers."))
    _parser.add_argument("-e", "--english", action="store_true",
                         default=False, help="Save only words in english.")
    _parser.add_argument("-c", "--category", action="store", help=(
        "Chose category to classify, can be a url, with scheme."))
    _parser.add_argument("-u", "--unknow", action="store_true", default=False,
                         help="Get word from unknow urls into url parsed.")
    return _parser.parse_args()


if __name__ == "__main__":
    opts = return_args()
    item = cat_words(opts.category, opts.unknow, opts.english)

    if opts.english:
        en = ""
    else:
        en = "pt_BR/"
    if opts.category.startswith('http'):
        en = "urls/"

    for w, c in item.items():
        with open('classifiers/{}{}.data'.format(
                en, opts.category.split('/')[-1]), 'a') as class_model:
            class_model.write("{}|{}\n".format(w.replace("|", ""), c))
