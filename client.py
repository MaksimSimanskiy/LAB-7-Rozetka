#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 10000)
print("connecting to {} port {}".format(*server_address))
conn = sock.connect(server_address)


def ask():
    a = input("Введите команду - ")
    print("Команда {!r}".format(a))
    b = bytes(a, "utf-8")
    sock.sendall(b)
    data = sock.recv(1024)
    if a == "exit":
        sys.exit()
    print("Получено {!r}".format(data.decode("utf-8")))
    return a


while True:
    ask()


