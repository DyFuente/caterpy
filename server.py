#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collect data from clients with urls to classify.

This server daemon will use port 60001 to listen connections.
Will save data with date and name of client.
"""


import sys
import socket
import base64


host = "caterpy.info" # socket.gethostname()
port = int(sys.argv[1])
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

key = base64.b64encode('caterpy_classify_url'.encode())


def save_file(file_name, data_file, source_ip, source_port):
    _name = "{}-{}".format(source_ip, file_name.decode())
    print("Connection with IP: {} in the port {}!".format(
        source_ip, source_port))
    print("Saving file on files/files_to_classify/{}".format(_name))
    with open("files/files_to_classify/{}".format(_name), "wb") as s_file:
        s_file.write(b"".join(data_file))


while True:
    try:
        conn, addr = sock.accept()
        with conn:
            get_data = conn.recv(1024)
            if get_data == key:
                conn.send("next".encode())
                get_file_name = conn.recv(1024)
                if get_file_name != b"":
                    conn.send("send_file".encode())
                    data = []
                    get_data = conn.recv(1024)
                    while get_data != b"":
                        data.append(get_data)
                        get_data = conn.recv(1024)
                save_file(get_file_name, data, addr[0], addr[1])
    except Exception as error:
        print(error)
