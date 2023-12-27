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
            gg =  cur.fetchall()
            print(gg)
            bf_usrid = ''
            for i in gg:
                bf_usrid = i[0]
            print(bf_usrid)
            if bf_usrid != '':
                cur.execute(f"insert into bfriends(username, userid) values ('{msglist[1]}', {usrid})")
                conn.commit()
                print('good')
                print(msglist[1])
                time.sleep(0.15)
                mess = msglist[1]
                c.send(mess.encode('utf-8'))
                c.send(mess.encode('utf-8'))
                time.sleep(0.15)
                print('sended')
            else:
                time.sleep(0.15)
                c.send('uncorrect'.encode('utf-8'))
                c.send('uncorrect'.encode('utf-8'))
                print('send uncorrect good')
                time.sleep(0.15)
        elif msglist[0] == '[CHOOSE]':
            print('choose: ' + msglist[1])
            cur.execute(f"select userid from Users where username = '{msglist[1]}'")
            if cur.fetchall() is not None:
                partner = msglist[1]
                c.send('success'.encode('utf-8'))
                cur.execute(f"select * from messages where from_username = '{usrnm}' and to_username = '{partner}'or from_username = '{partner}' and to_username = '{usrnm}'")
                mess = cur.fetchall()
                print(mess)
                messlist = ''
                if mess != []:
                    for i in mess:
                        messs_text =i[1] +'-'+ i[2]
                        messlist = messlist + messs_text + ' '
                    messlist.strip()
                    messlist = '[MESSAGES]:'+messlist
                    c.send(messlist.encode('utf-8'))     
                else:
                    c.send('pass'.encode('utf-8'))
            else:
                c.send('error'.encode('utf-8'))
        elif msglist[0] == '[SEND]':
            print('send: ' + msglist[1])
            print(clients)
            try:
                print(clients[partner])
            except KeyError:
                pass
            broadcast(clients, partner, msglist[1], usrnm, cur, conn)


    
def broadcast(clients, partner, msg, usrnm, cur, conn):
    cur.execute(f"insert into messages(from_username, mess_text, to_username) values ('{usrnm}', '{msg}','{partner}')")
    conn.commit()
    try:
        mess = usrnm + ': ' + msg
        partnerinf = clients[partner]
        for sock in clients.values():
            if sock == partnerinf:
                print('good')
                sock.send(bytes(mess, 'utf-8'))
                print('ended')
    except KeyError:
        pass