#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Validade list of urls."""


import socket
from glob import glob
from tldextract import extract
from collections import UserDict


lists = glob('new_lists/*')
protos = [('HTTP', 80), ('HTTPS', 443)]


def return_list_dict(list_to_dict):
    urls_list = dict()
    with open(list_to_dict, 'r') as f:
        urls = [x.strip() for x in f.readlines() if extract(x).registered_domain != '']
    for url in urls:
        e = extrac(url)
        domain = e.registered_domain
        for proto, port in protos:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(domain, port)
                if domain not in urls_list.keys():
                    if urls_list[domain] = defaultdict(lambda: False)
                if len(url.split(domain)) > 1:
                    if isinstance(urls_list[domain]['paths'], (list)):
                        urls_list[domain]['paths'].append(url.split(domain)[-1])
                    else:
                        urls_list[domain]['paths'] = [url.split(domain)[-1]]
                if e.subdomain != '':
                    if isinstance(urls_list[domain]['subdomain'], (list)):
                        urls_list[domain]['subdomain'].append(e.subdomain)
                    else:
                        urls_list[domain]['subdomain'] = [e.subdomain]
                if isinstance(urls_list[domain]['protocol'], (list)):
                    urls_list[domain]['protocol'].append(proto)
                else:
                    urls_list[domain]['protocol'] = [proto]
            except:
                pass
    return urls_list
