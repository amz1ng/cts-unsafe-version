# -*- coding: utf-8 -*-
import os
import socket
import threading
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mode = input("Введите режим работы: connect/start_serv > ")


def ConnectMode():
    try:
        ip = input("Введите IP удалённого сервера. Например: 255.255.255.255 > ")
        port = int(input("Введите порт для подключения к серверу > "))
        password = input("Введите пароль для доступа к серверу > ")

        s.connect((ip, port))
        s.sendall(password.encode('utf-8'))
        response = s.recv(1024).decode('utf-8')
        print(response)

        if response == "Неверный пароль. Подключение закрыто.":
            s.close()
            return
        else:
            print("Подключение прошло успешно. ")

        s.settimeout(1)  # Устанавливаем таймаут на 1 секунду

        while True:
            command = input("cts@cts > ")
            s.sendall(command.encode('utf-8'))

            try:
                out = s.recv(1024).decode('utf-8')
                print(out)
            except socket.timeout:
                print("Таймаут. Сервер не отправил ответ.")

    except:
        print("Что-то пошло не-так во время соединения")


def ServerMode():
    port = int(input("Введите порт для запуска сервера > "))
    passwd = input("Задайте пароль для подключения > ")
    s.bind(("localhost", port))
    s.listen(1)
    #conn, addr = s.accept()

    while True:
        conn, addr = s.accept()
        print('Client connected:', addr)

        password_attempt = conn.recv(1024).decode('utf-8')
        print(password_attempt)
        if password_attempt == passwd:
            conn.sendall("Пароль верный. Вы подключены.".encode('utf-8'))

        else:
            conn.sendall("Неверный пароль. Подключение закрыто.".encode('utf-8'))
            conn.close()
            return;

        while True:


            data = conn.recv(1024)
            data = data.decode('utf-8')
            try:
                def executeCommand():
                      # os.system("cmd /k %s" % (data,))
                      result = os.popen(data).read()
                      #print(result)
                      conn.sendall(result.encode('utf-8'))

                thread = threading.Thread(target=executeCommand)
                thread.start()
            except:
                print("Указана неверная команда")
            if not data:
                break
            print(data)
        # print(data.decode('utf-8'))


if(mode == "connect"):
    ConnectMode()


if (mode == "start_serv"):
    ServerMode()





