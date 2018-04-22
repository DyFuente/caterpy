#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Return models by category."""


from glob import glob


def return_models(limit=-1, diff=False):
    """Return two dicts with model data and model data with unique words."""
    models = glob('classifiers/*')
    _data_models = dict()

    for model in models:
        name_model = model.split('/')[1]
        _data_models[name_model] = set([])
        for w in [word for word, count in list(
                sorted([(w.split('|')[0], int(w.split('|')[1])) for w in list(
                    filter(None, open(model, 'r').read().split('\n')))],
                       key=lambda f: int(f[1]), reverse=True))]:
            _data_models[name_model].add(w)

    _intersect = set.intersection(
        *[_data_models[name] for name in _data_models])

    for model in _data_models:
        _data_models[model] = set([name for name in _data_models[model]
                                  if name not in _intersect][0:limit])

    if diff:
        _diff_models = dict()
        for model in _data_models:
            _diff_models[model] = _data_models[model].difference(
                *[_data_models[name] for name in _data_models
                  if name != model])
        return _data_models, _diff_models

    return (_data_models)
