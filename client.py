#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

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
    print("Получено {!r}".format(data.decode("utf-8")))
    return b

amount_received = 0
amount_expected = len(ask())
while amount_received < amount_expected:
    ask()
else:
    sock.close()
