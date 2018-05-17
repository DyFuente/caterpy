#!/usr/bin/env python3
# -*- codinf: utf-8 -*-
"""
Client to send data to socket server.

This client will send urls to be classified.
"""


import sys
import time
import socket
import base64


time_file = time.strftime("%Y_%m_%d_%H_%M_%S")
host = "caterpy.info"  # socket.gethostname()
port = int(sys.argv[1])
get_file = sys.argv[2]
file_name = socket.gethostname()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

key = base64.b64encode('caterpy_classify_url'.encode())

with client:
    client.send(key)
    get_data = client.recv(1024)
    if get_data == "next".encode():
        client.send("{}-{}".format(file_name, time_file).encode())
    get_data = client.recv(1024)
    if get_data == "send_file".encode():
        with open(get_file, 'rb') as read_file:
            client.send(read_file.read())
