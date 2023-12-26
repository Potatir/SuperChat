import socket
from threading import Thread
import userinf
from socket import AF_INET, SOCK_STREAM


def incoming_conn():
    while True:
        c, addr = SERVER.accept()
        print("пользователь %s:%s подключен" % addr)
        addresses[c] = addr
        Thread(target=new_user, args=(c, addr, BUFSIZ)).start()


def new_user(c, addr, BUFSIZ):
    while True:
        try:
            mess = c.recv(BUFSIZ).decode('utf-8')
            if mess == 'registration':
                print('registr')
                userinf.registration(c, addr, BUFSIZ)
            elif mess == 'autorization':
                print('авторизация')
                userinf.autorization(c, addr, BUFSIZ, clients)
        except ConnectionResetError:
            print("пользователь %s:%s отключен" % addr)
            break
            



clients = {}
addresses = {}

HOST = '10.250.0.15'
PORT = 1111
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket.socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
if __name__ == "__main__":
    SERVER.listen(5)
    print("ожидание соединения")
    ACCEPT_THREAD = Thread(target=incoming_conn)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()











'''
ረክጅርፊቪይስ፡
    እኦግ9ርውልድስ
    ርገ4ፍፈእ842ንፍ


ኢቭስንቹእኢወ = እግቢክደእ

@ወፍቪፍይውሰግ፡
    እርግፍቭ
'''