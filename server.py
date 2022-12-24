#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import perf_counter
from datetime import datetime
import struct
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("localhost", 10000)
print("Запущено {} порт {}".format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print("Ожидание команды")
    connection, client_address = sock.accept()
    start = 0
    try:
        print("Подключено с ", client_address)
        while True:
            data = connection.recv(1024)
            decode_data = data.decode("utf-8")
            print("Получена команда - {} ".format(decode_data))
            if decode_data == "on":
                msg = "Устройство включено, 220V, имя = Кухня".encode(encoding="utf-8")
                start = perf_counter()
                print("Данные отправлены клиенту")
                connection.sendall(msg)
            elif decode_data == "off":
                end = f"Устройство выключено.Время работы {perf_counter() - start:0.4f} секунд"
                end_by = str(end).encode(encoding="utf-8")
                print("Данные отправлены клиенту")
                connection.sendall(end_by)
            else:
                print("Ожидание команды", client_address)
                break
    finally:
        connection.close()
