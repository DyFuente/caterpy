#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validade list of urls."""


import sys
import socket
from tldextract import extract
from collections import namedtuple


def test_connection(server, port):
    """Test connection with url server. Return True is its ok."""
    _return = False
    try:
        _s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _s.settimeout(3.0)
        _s.connect((server, port))
        _return = True
    except Exception as error:
        pass
    return _return


def return_url_dict(url):
    """Return a dict of urls."""
    _url = namedtuple('url', 'url domain subdomain protocol')
    protos = [('HTTP', 80), ('HTTPS', 443)]
    _url.url = set([url])
    tld = extract(url)
    _url.domain = tld.registered_domain
    if _url.domain == '':
        _url.domain = tld.domain
    _url.subdomain = tld.subdomain
    _url.protocol = []
    for proto, port in protos:
        if test_connection(url, port):
            _url.protocol.append(proto)
        if _url.subdomain != '' and test_connection(
                ".".join([_url.subdomain, _url.domain]), port):
            _url.url.add(".".join([_url.subdomain, _url.domain]))
    return _url


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("To validate you needs an url...")
    get_url = return_url_dict(sys.argv[1])
    if len(get_url.protocol) >= 1:
        print("Test for url {}".format(sys.argv[1]))
        print("URL Domain: {}".format(get_url.domain))
        if get_url.subdomain != '':
            print("URL Subdomain: {}".format(get_url.subdomain))
        print("URL Protocol Responses: {}".format(" ".join(get_url.protocol)))
    else:
        print("Impossible to test url: {}".format(sys.argv[1]))
