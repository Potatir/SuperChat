from customtkinter import *
import socket
import time
import mainwin

ADDR = '192.168.0.102'
PORT = 1111
BUFSIZ = 1024


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ADDR, PORT))




def regwin():
    def on_closing():
        win.destroy()
    
    def submit_reg():
        delay_time = 0.45
        client_socket.send('registration'.encode('utf-8'))
        log = entrylog.get()
        password = entrypass.get()
        mail = entrymail.get()
        name = entryname.get()
        sname = entrysname.get()
        mess_text = log + ' ' + password + ' ' + mail + ' ' + name + ' ' + sname
        client_socket.send(mess_text.encode('utf-8'))

        mess = client_socket.recv(BUFSIZ).decode('utf-8')
        if mess == 'success':
            win.destroy()
        elif mess == 'incorrect email':
            emaillab.configure(text = 'Incorrect Email!')
        elif mess == 'incorrect password':
            passlab.configure(text = 'Incorrect Password!')


    win = CTk()
    win.geometry("600x600")
    win.resizable(False, False)
    win.protocol("WM_DELETE_WINDOW", on_closing)
    CTkLabel(master=win, text="").pack(expand=True, side="left")

    frame2 = CTkFrame(win, fg_color='purple', width=300, height=600)
    frame2.pack(expand=True, side='left')

    frame = CTkFrame(master=win, width=300, height=600, fg_color="#ffffff")
    frame.pack_propagate(0)
    frame.pack(expand=True, side="right")

    CTkLabel(master=frame, text="Регистрация", text_color="#601E88", anchor="w", justify="left",
             font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
    CTkLabel(master=frame, text="Создайте свой аккаунт", text_color="#7E7E7E", anchor="w", justify="left",
             font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Логин", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
             compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
    entrylog = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
    entrylog.pack(anchor="w", padx=(25, 0))

    passlab = CTkLabel(master=frame, text="  Пароль:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left")
    passlab.pack(anchor="w", pady=(21, 0), padx=(25, 0))
    entrypass = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000",show="*")
    entrypass.pack(anchor="w", padx=(25, 0))
    
    emaillab = CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), compound="left")
    emaillab.pack(anchor="w", pady=(21, 0), padx=(25, 0))
    entrymail = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,text_color="#000000")
    entrymail.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Имя:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
             compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    entryname = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,text_color="#000000")
    entryname.pack(anchor="w", padx=(25, 0))

    CTkLabel(master=frame, text="  Фамилия:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
             compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
    entrysname = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,text_color="#000000")
    entrysname.pack(anchor="w", padx=(25, 0))

    CTkButton(master=frame, text="Зарегистрироваться", fg_color="#601E88", hover_color="#E44982",
              font=("Arial Bold", 12), text_color="#ffffff", width=225, command=submit_reg).pack(anchor="w", pady=(40, 0), padx=(25, 0))
    win.mainloop()

def submit_autoriz():
    client_socket.send('autorization'.encode('utf-8'))
    usern = username.get()
    passs = passentry.get()
    mess_text = usern + ' ' + passs
    client_socket.send(mess_text.encode('utf-8'))
    mess = client_socket.recv(BUFSIZ).decode('utf-8')
    if mess == 'success':
        win.destroy()
        mainwin.mainwin_start(client_socket, BUFSIZ)
    elif mess == 'no username like this':
        mainn.configure(text = 'Incorrect Username!')
    elif mess == 'uncorrect password':
        mainn.configure(text = 'Incorrect Password!')

win = CTk()
win.geometry("600x480")
win.resizable(False, False)

CTkLabel(master=win, text="").pack(expand=True, side="left")

frame2 = CTkFrame(win, fg_color='purple', width=300, height=480)
frame2.pack(expand=True, side='left')

frame = CTkFrame(master=win, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")




CTkLabel(master=frame, text="Добро пожаловать!", text_color="#601E88", anchor="w", justify="left",
         font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
mainn = CTkLabel(master=frame, text="Войдите в свой аккаунт", text_color="#7E7E7E", anchor="w", justify="left",
         font=("Arial Bold", 12))
mainn.pack(anchor="w", padx=(25, 0))
CTkLabel(master=frame, text="Логин:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
username = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="Пароль:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
passentry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000",show="*")
passentry.pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Войти", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=submit_autoriz).pack(anchor="w", pady=(40, 0), padx=(25, 0))

CTkButton(master=frame, text="Зарегистрироваться", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=regwin).pack(anchor="w", pady=(40, 0), padx=(25, 0))

win.mainloop()
