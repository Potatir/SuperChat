from customtkinter import *
from threading import Thread

def mainwin_start(client_socket, BUFSIZ):
    def gg(event, obj):
        mess = '[CHOOSE]: ' + obj.cget('text')
        client_socket.send(mess.encode('utf-8'))
        choosepart.configure(text = obj.cget('text'))
    def new_chat(name):
        widget = CTkLabel(master=chatchoose,text = name,font=("Arial Bold", 30), text_color='purple',width=590, height= 100, fg_color='#ffffff')
        widget.pack(side = 'top', pady = (3, 0))
        widget.bind("<1>", lambda event, obj=widget: gg(event, obj))
    def submut_find():
        mess = '[FIND]: ' + find_field.get()
        client_socket.send(mess.encode('utf-8'))
        if client_socket.recv(BUFSIZ).decode('utf-8') == find_field.get():
            new_chat(find_field.get())
    def send():
        mess = '[SEND]: ' + chat_entry.get()
        client_socket.send(mess.encode('utf-8'))
        text = chat_label.cget('text')+'\n'+username.cget('text') +': ' + chat_entry.get()
        chat_label.configure(text = text)
    def receive():
        while True:
            try:
                mess = client_socket.recv(BUFSIZ).decode('utf-8')
                mess_arr = mess.split(': ')
                if choosepart.cget('text') == mess_arr[0]:
                    teext = chat_label.cget('text')+'\n'+choosepart.cget('text') +': '+ mess_arr[1]
                    chat_label.configure(text = teext)
            except OSError:
                print('gg')
                break





    mess = client_socket.recv(BUFSIZ).decode('utf-8')
    mess2 = client_socket.recv(BUFSIZ).decode('utf-8')
    mess_list = mess.split(' ')
    
    
    if mess2 != 'pass':
        mess2_list = mess2.split(' ')
        mess2_list.pop(-1)
        print(mess2_list)
    print(mess_list)
    mess_list.pop(-1)
    
    win = CTk()
    win.geometry("1600x900")
    win.resizable(False, False)
    
    frame2 = CTkFrame(win, fg_color='purple', width=600, height=900)

    userinf = CTkFrame(frame2, fg_color="#ffffff", width=590, height=150)
    userinf.pack_propagate(False)
    
    username = CTkLabel(userinf, text=mess_list[0], text_color="purple", anchor="w", justify="left",font=("Arial Bold", 40))
    username.pack(side = 'left', padx = (50,0))
    userinf.pack(side='top', pady = (5, 0))
    
    chatchoose = CTkFrame(frame2,  fg_color="purple", width=590, height=740)
    chatchoose.pack_propagate(False)
    if mess2 != 'pass':
        for i in mess2_list:
            new_chat(i)
    chatchoose.pack(side = 'bottom')
    
    frame2.pack_propagate(False)
    frame2.pack(expand=True, side='left')

    frame = CTkFrame(master=win, width=1000, height=900, fg_color="#ffffff")
    frame.pack_propagate(False)
    
    findframe = CTkFrame(frame, width= 990, height=50, fg_color = 'purple')
    findframe.pack_propagate(False)
    
    find_field = CTkEntry(findframe, width=800,text_color='purple', height=40, fg_color='#ffffff',placeholder_text='find by username', font=("Arial Bold", 20))
    find_field.pack(side = 'left', padx = (5,0))
    
    find_button = CTkButton(findframe,width=175, height=40, fg_color='#ffffff', text='submit', text_color='purple',font=("Arial Bold", 20), command=submut_find)
    find_button.pack(side = 'left', padx = (5,0))
    
    findframe.pack(side = 'top', pady = (5, 0))   
    
    chat_frame = CTkFrame(master = frame, width=990, height=835, fg_color='purple')
    chat_frame.pack_propagate(False)
    choosepart = CTkLabel(master=chat_frame, width=980, height=40, fg_color='purple', text='someone', text_color='#ffffff', font=("Arial Bold", 30))
    choosepart.pack(side = 'top', pady = (5,0))
    chat_label = CTkLabel(master=chat_frame,text = '', width = 980, height= 725, fg_color='#ffffff', text_color='purple', font=("Arial Bold", 30))
    chat_label.pack(side = 'top', pady = (5,0))
    chat_entry = CTkEntry(master=chat_frame, width= 900, height=50, fg_color='#ffffff', text_color='purple')
    chat_entry.pack(side = 'left',padx = (5,0))
    send_button = CTkButton(master = chat_frame,command=send, width= 75, height=50, fg_color='#ffffff', text='SEND', text_color='purple')
    send_button.pack(side='left', padx = (5,0))
    chat_frame.pack(side = 'top', pady = (5,0))

    frame.pack(expand=True, side="right")
    receive_thread = Thread(target=receive)
    receive_thread.start()
    win.mainloop()
