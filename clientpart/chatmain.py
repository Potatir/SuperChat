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

def open_chat():
    new_window = Tk()
    new_window.geometry("900x800")
    new_window.title("SupaChad")

    first_frame = tk.Frame(root, width=200, height=200, bg='lightblue')
    second_frame = tk.Frame(root, width=200, height=200, bg='lightgreen')


 