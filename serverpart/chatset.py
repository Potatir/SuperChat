import socket
from socket import AF_INET, SOCK_STREAM
import psycopg2
import time
def main(c, addr, BUFSIZ, clients, usrid, usrnm):
    
    datalist = []
    partner = ''
    conn = psycopg2.connect(dbname = 'superchat', user = 'postgres', password = '222222', port = '5432')
    cur = conn.cursor()
    cur.execute(f'select username from Users where userid = {usrid}')
    for i in cur.fetchall():
        datalist.append(i[0])
    cur.execute(f'select name, sname from profile where userid = {usrid}')
    for i in cur.fetchall():
        datalist.append(i[0])
        datalist.append(i[1])

    datatext = ''
    for i in datalist:
        datatext = datatext + i + ' '
    datatext.strip()
    c.send(datatext.encode('utf-8'))
    datalist = []
    cur.execute(f'select username from bfriends where userid = {usrid}')
    gh = cur.fetchall()
    print(gh)
    if not gh == []:
        for i in gh:
            datalist.append(i[0])
        print(datalist)
        print(datalist)
        datatext = ''
        for i in datalist:
            datatext = datatext + i + ' '
        datatext.strip()
        time.sleep(0.15)
        c.send(datatext.encode('utf-8'))
    else:
        time.sleep(0.15)
        c.send('pass'.encode('utf-8'))
    while True:
        msg = c.recv(BUFSIZ).decode('utf-8')
        msglist = msg.split(': ')
        if msglist[0] == '[FIND]':
            print('find: ' + msglist[1])
            cur.execute(f"select userid from users where username = '{msglist[1]}'")
            bf_usrid = ''
            for i in cur.fetchall():
                bf_usrid = i[0]
            if bf_usrid != '':
                cur.execute(f"insert into bfriends( username, userid) values ('{msglist[1]}', {usrid})")
                conn.commit()
                c.send(msglist[1].encode('utf-8'))
            else:
                c.send('uncorrect'.encode('utf-8'))
        elif msglist[0] == '[CHOOSE]':
            print('choose: ' + msglist[1])
            cur.execute(f"select userid from Users where username = '{msglist[1]}'")
            if cur.fetchall() is not None:
                partner = msglist[1]
                c.send('success'.encode('utf-8'))
            else:
                c.send('error'.encode('utf-8'))
        elif msglist[0] == '[SEND]':
            print('send: ' + msglist[1])
            print(clients)
            print(clients[partner])
            broadcast(clients, partner, msglist[1], usrnm)


    
def broadcast(clients, partner, msg, usrnm):
    msg = usrnm + ': ' + msg
    partnerinf = clients[partner]
    for sock in clients.values():
        if sock == partnerinf:
            print('good')
            sock.send(bytes(msg, 'utf-8'))
            print('ended')