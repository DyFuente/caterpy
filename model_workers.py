#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Start workers to create model for all categories."""


import time
import threading
from subprocess import call
from caterpy.url_lists import url_lists

cats = set([c for c in url_lists if c != 'porno'])


def worker_cat(cat):
    call(["/usr/bin/python3 update_classifiers.py {}".format(cat)],
         shell=True)


while len(cats) != 0:
    if threading.active_count() > 7:
        print("Threads active: {}".format(threading.active_count()))
        time.sleep(30)
    else:
        cat = cats.pop()
        print("starting process to: {}".format(cat))
        start_worker = threading.Thread(target=worker_cat, args=[cat])
        start_worker.start()
