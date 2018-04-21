#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Return models by category."""


from glob import glob


def return_models():
    """Return two dicts with model data and model data with unique words."""
    models = glob('classifiers/*')
    _diff_models = dict()
    _data_models = dict()

    for model in models:
        name_model = model.split('/')[1]
        _data_models[name_model] = set([])
        for w in [word for word, count in list(
                sorted([(w.split('|')[0], int(w.split('|')[1])) for w in list(
                    filter(None, open(model, 'r').read().split('\n')))],
                       key=lambda f: f[1], reverse=True))]:
            _data_models[name_model].add(w)

    for model in [name for name in _data_models]:
        union = set.union(*[_data_models[name] for name in _data_models
                            if name != model])
        _diff_models[model] = _data_models[model].difference(union)

    return (_data_models, _diff_models)
