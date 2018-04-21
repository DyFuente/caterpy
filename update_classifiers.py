#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Update classifier files with words and count."""


import sys
from caterpy.learn_category import cat_words


item = cat_words(sys.argv[1], False)

for w, c in item.items():
    with open('classifiers/{}'.format(sys.argv[1]), 'a') as class_model:
        class_model.write("{}|{}\n".format(w.replace("|", ""), c))
