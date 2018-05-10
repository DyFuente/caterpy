#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Start workers to create model for all categories."""


import time
import argparse
import threading
from subprocess import call
from unidecode import unidecode
from caterpy.url_lists import return_url_lists


def return_args():
    """Get some args to start update classifiers."""
    _parser = argparse.ArgumentParser(add_help=True, description=(
        "Get some args to pass to update_classifiers script."))
    _parser.add_argument("-c", "--category", action="store", default="all",
                         help="Pass category, url or all categories.")
    _parser.add_argument("-u", "--unknow", action="store_true", default=False,
                         help="Get word from unknow urls into url parsed.")
    _parser.add_argument("-e", "--english", action="store_true",
                         default=False, help="Save only words in english.")
    return _parser.parse_args()


def worker_cat(cat, en, unknow):
    call(["/usr/bin/python3 update_classifiers.py -c {} {} {}".format(
        cat, en, unknow)], shell=True)


if __name__ == "__main__":
    opts = return_args()
    url_lists = return_url_lists()

    if opts.category == "all":
        cats = set([c for c in url_lists])
    elif opts.category.startswith('http'):
        cats = set([opts.category])
    else:
        cats = set([c for c in url_lists if unidecode(c) == unidecode(
            opts.category)])

    if opts.english:
        en = "-e"
    else:
        en = ""
    if opts.unknow:
        unknow = "-u"
    else:
        unknow = ""

    while len(cats) != 0:
        if threading.active_count() > 10:
            time.sleep(30)
        else:
            cat = cats.pop()
            start_worker = threading.Thread(
                target=worker_cat, args=[cat, en, unknow])
            start_worker.start()
