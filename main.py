import os
import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mode = input("Введите режим работы: connect/start_serv > ")

if(mode == "connect"):
 try:

    ip = input("Введите IP удалённого сервера. Например: 255.255.255.255 > ")



    port = int(input("Введите порт для подключения к серверу > "))
    s.connect((ip, port))
    print("Подключение прошло успешно. ")
    while True:
        command = input("cts@cts > ")
        s.send(command.encode('utf-8'))

 except:
     print("Что-то пошло не-так во время соединения")


if (mode == "start_serv"):

    port = int(input("Введите порт для запуска сервера > "))
    s.bind(("localhost", port))
    s.listen(1)
   # conn, addr = s.accept()

    while True:
        conn, addr = s.accept()
        print('Client connected:', addr)
        while True:

         data = conn.recv(1024)
         data = data.decode('utf-8')
         try:
          def executeCommand():
           os.system("cmd /k %s" % (data,))
          thread = threading.Thread(target=executeCommand)
          thread.start()
         except:
             print("Указана неверная команда")
         if not data:
            break
         print(data)
        # print(data.decode('utf-8'))





