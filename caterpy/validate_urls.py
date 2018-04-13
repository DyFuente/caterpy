#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Validade list of urls."""


import socket
from tldextract import extract
from collections import defaultdict


def return_list_dict(list_to_dict):
    protos = [('HTTP', 80), ('HTTPS', 443)]
    """Return a dict of urls."""
    urls_list = dict()
    with open(list_to_dict, 'r') as f:
        urls = [x.strip() for x in f.readlines()
                if extract(x).registered_domain != '']
    for url in urls:
        e = extract(url)
        domain = e.registered_domain
        print(domain)
        for proto, port in protos:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3.0)
                s.connect((domain, port))
                if domain not in urls_list.keys():
                    urls_list[domain] = defaultdict(lambda: False)
                    urls_list[domain]['urls'] = set([])
                urls_list[domain]['urls'].add(url)
                if len(url.split(domain)) > 1:
                    if isinstance(urls_list[domain]['paths'], (set)):
                        urls_list[domain]['paths'].add(
                            url.split(domain)[-1])
                    else:
                        urls_list[domain]['paths'] = set(
                            [url.split(domain)[-1]])
                if e.subdomain != '':
                    if isinstance(urls_list[domain]['subdomain'], (set)):
                        urls_list[domain]['subdomain'].add(e.subdomain)
                    else:
                        urls_list[domain]['subdomain'] = set([e.subdomain])
                if isinstance(urls_list[domain]['protocol'], (set)):
                    urls_list[domain]['protocol'].add(proto)
                else:
                    urls_list[domain]['protocol'] = set([proto])
            except Exception:
                pass
    return urls_list
