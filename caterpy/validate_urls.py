#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""Validade list of urls."""


import time
import socket
import colorama
import threading
from glob import glob
from queue import Queue
from tldextract import extract
from collections import defaultdict


def return_url_dict(url, cat):
    protos = [('HTTP', 80), ('HTTPS', 443)]
    """Return a dict of urls."""
    e = extract(url)
    domain = e.registered_domain
    if domain == '':
        domain = e.domain
    for proto, port in protos:
        try:
            _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            _s.settimeout(3.0)
            _s.connect((domain, port))
            print("{}Parseando: {} -> {}".format(
                colorama.Fore.GREEN, cat, domain))
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
        except Exception as error:
            print("{}Impossivel parsear: {} -> {} -> {}".format(
                colorama.Fore.RED, cat, domain, error))


def save_file(file_to_save):
    with open('csv_files/{}.csv'.format(file_to_save), 'a') as fts:
        fts.write("|".join(
            ['domain', 'urls', 'paths', 'subdomains', 'proto'])+"\n")
        for x in urls_list:
            urls = ";".join([u for u in urls_list[x]['urls']])
            if urls_list[x]['paths']:
                paths = ";".join([p for p in urls_list[x]['paths']])
            else:
                paths = ''
            if urls_list[x]['subdomains']:
                subdomains = ";".join([s for s in urls_list[x]['subdomains']])
            else:
                subdomains = ''
            proto = ";".join([p for p in urls_list[x]['protocol']])
            fts.write("|".join([x, urls, paths, subdomains, proto])+"\n")


cats_to_validate = list(sorted([x.split('/')[1] for x in glob('lists/*')]))

for cat in cats_to_validate:

    urls_list = dict()
    print("Iniciando validação para: {}".format(cat))
    q_urls = Queue()
    [q_urls.put(x) for x in list(filter(None, open(
        'lists/{}'.format(cat), 'r').read().split('\n')))]

    while q_urls.qsize() != 0:
        if threading.activeCount() < 300:
            start_process = threading.Thread(
                target=return_url_dict, args=[q_urls.get(0), cat])
            start_process.start()
        else:
            time.sleep(2)

    while threading.activeCount() > 1:
        time.sleep(2)

    print("\n{}Salvando arquivo csv_files/{}.csv\n".format(
        colorama.Fore.YELLOW, cat.lower()))
    save_file(cat.lower())
    del(urls_list)
    del(q_urls)
