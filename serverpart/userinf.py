import socket
import psycopg2
import chatset
import re



def registration(c, addr, BUFSIZ):
    conn = psycopg2.connect(dbname = 'superchat', user = 'postgres', password = '222222', port = '5432')
    cur = conn.cursor()
    mess = c.recv(BUFSIZ).decode("utf-8")
    mess_list = mess.split(' ')
    reg1 = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$')
    reg2 = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(reg1, mess_list[1]):
        if re.fullmatch(reg2, mess_list[2]):
            cur.execute(f"""
                        insert into Users(username, password) values ('{mess_list[0]}','{mess_list[1]}');
                        insert into email(username, password, email) values('{mess_list[0]}','{mess_list[1]}','{mess_list[2]}');
                        """)
            conn.commit()
            cur.execute(f"select userid from Users where username = '{mess_list[0]}';")
            for i in cur.fetchall():
                user_id = i[0]
            cur.execute(f"""
                        insert into allip(ipadress, userid) values('{addr[0]}',{user_id});
                        insert into profile(userid, name, sname) values ('{user_id}', '{mess_list[3]}', '{mess_list[4]}')
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
        mess = c.recv(BUFSIZ).decode("utf-8")
        mess_list = mess.split(" ")
        usrnm = mess_list[0]
        pssword = mess_list[1]
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
    