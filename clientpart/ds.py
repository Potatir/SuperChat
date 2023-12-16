from tkinter import *
from tkinter import ttk
import socket
from socket import AF_INET, SOCK_STREAM
import time

HOST = '127.0.0.1'
PORT = 1111


BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket.socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)


def open_new_window():


    client_socket.send("registration".encode("utf-8"))



    def submit_reg():
        client_socket.send(entry_reg1.get().encode("utf-8"))
        time.sleep(0.04)
        client_socket.send(entry_reg2.get().encode("utf-8"))
        time.sleep(0.04)
        client_socket.send(entry_reg3.get().encode("utf-8"))
        time.sleep(0.04)
        client_socket.send(entry_reg4.get().encode("utf-8"))
        time.sleep(0.04)
        client_socket.send(entry_reg5.get().encode("utf-8"))
        time.sleep(0.04)
        if client_socket.recv(BUFSIZ).decode("utf-8") == 'success':
            new_window.destroy()
            
            
            
    new_window = Toplevel(window)
    new_window.geometry("700x500")
    new_window.title("New Window")

    new_label = ttk.Label(new_window, text="Регистрация")
    new_label.pack(pady=20)

    entry_reg1 = ttk.Entry(new_window)
    entry_reg1.insert(0, 'username')
    entry_reg1.pack(pady=10)  
   
    entry_reg1.focus_set()  
    new_window.update_idletasks()  
    width = entry_reg1.winfo_width()  
    entry_reg1.place(relx=.5, rely=.2, anchor="c")
   
    entry_reg2 = ttk.Entry(new_window)
    entry_reg2.insert(0, 'password')
    entry_reg2.pack(pady=10)  
   
    entry_reg2.focus_set()  
    new_window.update_idletasks()  
    width = entry_reg2.winfo_width()  
    entry_reg2.place(relx=.5, rely=.3, anchor="c")

    entry_reg3 = ttk.Entry(new_window)
    entry_reg3.insert(0, 'email')
    entry_reg3.pack(pady=10)  
   
    entry_reg3.focus_set()  
    new_window.update_idletasks()  
    width = entry_reg3.winfo_width()  
    entry_reg3.place(relx=.5, rely=.4, anchor="c")

    entry_reg4 = ttk.Entry(new_window)
    entry_reg4.insert(0, 'name')
    entry_reg4.pack(pady=10)  
   
    entry_reg4.focus_set()  
    new_window.update_idletasks()  
    width = entry_reg4.winfo_width()  
    entry_reg4.place(relx=.5, rely=.5, anchor="c")

    entry_reg5 = ttk.Entry(new_window)
    entry_reg5.insert(0, 'surname')
    entry_reg5.pack(pady=10)  
   
    entry_reg5.focus_set()  
    new_window.update_idletasks()  
    width = entry_reg5.winfo_width()  
    entry_reg5.place(relx=.5, rely=.6, anchor="c")

    btn_sub = ttk.Button(text="Submit", width="20", master=new_window, command=submit_reg)
    btn_sub.place(relx=.5, rely=.7, anchor="c")


def open_login_window():
    new_window = Toplevel(window)
    new_window.geometry("500x300")
    new_window.title("New Window")
    client_socket.send('autorization'.encode('utf-8'))



    def submit_log():    
        client_socket.send(entry_log1.get().encode("utf-8"))
        time.sleep(0.04)
        client_socket.send(entry_log2.get().encode("utf-8"))
        time.sleep(0.04)
        print("Send")

        answer = client_socket.recv(BUFSIZ).decode("utf-8")
        if answer == 'success':
            print('good')
            new_window.destroy()    
        elif answer == 'uncorrect password':
            print("incorrect password")
            log_label['text'] = 'incorrect password!'
        elif answer == 'no username like this':
            print("incorrect username")
            log_label['text'] = 'incorrect username!'


    log_label = ttk.Label(new_window, text="Авторизация", font=('Arial', 20))
    log_label.pack(pady=20)


    


    entry_log1 = ttk.Entry(new_window)
    entry_log1.insert(0, 'username')
    entry_log1.pack(pady=10)  
   
    entry_log1.focus_set()  
    new_window.update_idletasks()  
    width = entry_log1.winfo_width()  
    entry_log1.place(relx=.5, rely=.3, anchor="c")
   
    entry_log2 = ttk.Entry(new_window)
    entry_log2.insert(0, 'password')
    entry_log2.pack(pady=10)  
   
    entry_log2.focus_set()  
    new_window.update_idletasks()  
    width = entry_log2.winfo_width()  
    entry_log2.place(relx=.5, rely=.4, anchor="c")

    btn_log_sub = ttk.Button(text="Submit", width="20", master=new_window, command=submit_log)
    btn_log_sub.place(relx=.5, rely=.5, anchor="c")


    





window = Tk()
window.geometry("800x800")
window.title("SuperChat")

for c in range(2):
    window.columnconfigure(index=c, weight=1)
for r in range(2):
    window.rowconfigure(index=r, weight=1)

label = ttk.Label(text="SUPERCHAT", font=("Arial", 24))
label.place(relx=.5, rely=.1, anchor="c")

btn3 = ttk.Button(text="Log In", width="50", command=open_login_window)
btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)

btn4 = ttk.Button(text="Sign Up", width="50", command=open_new_window)
btn4.grid(row=1, column=1, ipadx=6, ipady=6, padx=5, pady=5)

window.mainloop()
