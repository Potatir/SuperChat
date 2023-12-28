from customtkinter import *
from threading import Thread
import time


def mainwin_start(client_socket, BUFSIZ):
    global thread_stop
    thread_stop = False
    bflist = []
    def on_closing():
        win.destroy()
        global thread_stop
        thread_stop = True
    def gg(event, obj):
        mess = '[CHOOSE]: ' + obj.cget('text')
        client_socket.send(mess.encode('utf-8'))
        choosepart.configure(text = obj.cget('text'))
        chat_label.configure(text = '')
        mess = client_socket.recv(BUFSIZ).decode('utf-8')
        print(mess)
        mess1_list = mess.split(':')
        print(mess1_list)
        if mess1_list[0] == 'pass':
            pass
        elif mess1_list[0] == '[MESSAGES]':
            mess2_list = mess1_list[1].split(' ')
            mess2_list.pop(-1)
            print(mess2_list)
            for i in mess2_list:
                mess3_list = i.split('-')
                print(mess3_list)
                
                text = chat_label.cget('text') + mess3_list[0] + ': ' + mess3_list[1] + '\n'
                chat_label.configure(text = text)
            chat_frame.after(10, chat_frame._parent_canvas.yview_moveto, 1.0)

            

    def new_chat(name):
        if name not in bflist:
            mess = '[FIND]: ' + name
            client_socket.send(mess.encode('utf-8'))
            print('отправленно')
            time.sleep(0.15)
            mess = client_socket.recv(512).decode('utf-8')
            time.sleep(0.15)
            print('принято: ' + mess)
            if mess == mess:
                new_chat(name)
                find_field.delete(0, END)
            elif mess == 'uncorrect':
                find_button.configure(text = 'no user like this')
                find_field.delete(0, END)
            widget = CTkLabel(master=chatchoose,text = name,font=("Arial Bold", 30), text_color='purple',width=590, height= 100, fg_color='#ffffff', bg_color='#ffffff')
            widget.pack(side = 'top', pady = (3, 0))
            widget.bind("<1>", lambda event, obj=widget: gg(event, obj))

            bflist.append(name)
        else:
            pass
    def submut_find():
        new_chat(find_field.get())
    def send():
        if chat_entry.get() != '':
            mess = '[SEND]: ' + chat_entry.get()
            client_socket.send(mess.encode('utf-8'))
            text = chat_label.cget('text')+username.cget('text') +': ' + chat_entry.get() + '\n'
            chat_label.configure(text = text)
            chat_entry.delete(0, END)
            chat_frame.after(10, chat_frame._parent_canvas.yview_moveto, 1.0)
        else:
            pass
    def receive():
        global thread_stop
        while True:
            if thread_stop:
                break
            else:
                try:
                    mess = client_socket.recv(BUFSIZ).decode('utf-8')
                    mess_arr = mess.split(': ')
                    if choosepart.cget('text') == mess_arr[0]:
                        teext = chat_label.cget('text')+'\n'+choosepart.cget('text') +': '+ mess_arr[1]
                        chat_label.configure(text = teext)
                    elif len(mess_arr) == 2:
                        new_chat(mess_arr[0])
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
    win.title('SuperChat')
    win.protocol("WM_DELETE_WINDOW", on_closing)
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
    chat_frame = CTkScrollableFrame(master = frame, width=990, height=835, fg_color='purple')
    choosepart = CTkLabel(master=chat_frame, width=980, height=40, fg_color='purple', text='someone', text_color='#ffffff', font=("Arial Bold", 30))
    choosepart.pack(side = 'top', pady = 5)
    chat_label = CTkLabel(master=chat_frame,text = '', width = 980, height= 725, fg_color='#ffffff', text_color='purple', font=("Arial Bold", 30))
    chat_label.pack(side = 'top', pady = 5)
    chat_entry = CTkEntry(master=chat_frame, width= 900, height=50, fg_color='#ffffff', text_color='purple')
    chat_entry.pack(side = 'left',padx = 5)
    send_button = CTkButton(master = chat_frame,command=send, width= 75, height=50, fg_color='#ffffff', text='SEND', text_color='purple')
    send_button.pack(side='left', padx =5)
   
    chat_frame.pack(side = 'top', pady = 5)

    frame.pack(expand=True, side="right")
    receive_thread = Thread(target=receive)
    receive_thread.start()
    win.mainloop()
