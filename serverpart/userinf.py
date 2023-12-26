import socket
import psycopg2
import chatset
import re



def registration(c, addr, BUFSIZ):
    conn = psycopg2.connect(dbname = 'superchat', user = 'postgres', password = '222222', port = '5432')
    cur = conn.cursor()
    mess = c.recv(BUFSIZ).decode("utf-8")
    mess2 = c.recv(BUFSIZ).decode("utf-8")
    mess3 = c.recv(BUFSIZ).decode("utf-8")
    mess4 = c.recv(BUFSIZ).decode("utf-8")
    mess5 = c.recv(BUFSIZ).decode("utf-8")
    print('принято')
    print(mess)
    print(mess2)
    print(mess3)
    print(mess4)
    print(mess5)
    reg1 = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$')
    reg2 = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(reg1, mess2):
        if re.fullmatch(reg2, mess3):
            cur.execute(f"""
                        insert into Users(username, password) values ('{mess}','{mess2}');
                        insert into email(username, password, email) values('{mess}','{mess2}','{mess3}');
                        """)
            conn.commit()
            cur.execute(f"select userid from Users where username = '{mess}';")
            for i in cur.fetchall():
                user_id = i[0]
            cur.execute(f"""
                        insert into allip(ipadress, userid) values('{addr[0]}',{user_id});
                        insert into profile(userid, name, sname) values ('{user_id}', '{mess4}', '{mess5}')
                        """)
            conn.commit()
            print('добавденно')
            c.send("success".encode("utf-8"))
        else:
            c.send('incorrect email'.encode("utf-8"))
    else:
        c.send('incorrect password'.encode("utf-8"))


def autorization(c, addr, BUFSIZ, clients):
    userlist = []
    
    conn = psycopg2.connect(dbname = 'superchat', user = 'postgres', password = '222222', port = '5432')
    cur = conn.cursor()
    while True:
        usrnm = c.recv(BUFSIZ).decode("utf-8")
        print(usrnm)
        print('принято')
        pssword = c.recv(BUFSIZ).decode("utf-8")
        print(pssword)
        print('принято')
        cur.execute(f"select username, password from Users where username = '{usrnm}'")
        fech = cur.fetchall()
        if fech is not None:
            for i in fech:
                print(i[0])
                print(i[1])
                userlist.append(i[0])
                userlist.append(i[1])
            if usrnm in userlist:
                if pssword in userlist:
                    c.send('success'.encode('utf-8'))
                    print('успешно')
                    cur.execute(f"select userid from Users where username = '{usrnm}'")
                    usrid = ''
                    for i in cur.fetchall():
                        usrid = int(i[0])
                    cur.execute(f"UPDATE allip SET ipadress = '{addr[0]}' where userid = '{usrid}'")
                    conn.commit()
                    clients[usrnm] = c
                    print(clients[usrnm])
                    chatset.main(c, addr, BUFSIZ, clients, usrid, usrnm)
                else:
                    c.send('uncorrect password'.encode('utf-8'))
                    print('не успешно')
                    break
            else:
                c.send('no username like this'.encode('utf-8'))
                print('не успешно')
                break
        else:
                c.send('no username like this'.encode('utf-8'))
                print('не успешно')
                break
    