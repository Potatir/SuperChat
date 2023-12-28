import tkinter as tk
from tkinter import ttk


def open_chat():
    new_window = tk.Tk()
    new_window.geometry("900x800")
    new_window.title("SupaChad")
    new_window.attributes('-fullscreen', True)

    first_frame = tk.Frame(width=600, height=1030, bg='lightblue')
    second_frame = tk.Frame(width=1270, height=1030, bg='lightgreen')
    third_frame = tk.Frame(width=610, height=200, bg='red', borderwidth=1, relief='solid', padx=66, pady=59)
    ava_frame = tk.Frame(width=120, height=130, bg = 'grey')



    first_frame.grid(row=0, column=0, padx=10, pady=10)



    second_frame.grid(row=0, column=1, padx=10, pady=10)

    name_label = ttk.Label(third_frame, text="Введите имя", background='red', font=('Arial', 20))
    name_label.pack(anchor='n', padx=150)


    third_frame.place(relx=0.005, rely=0.08, anchor="w")
    ava_frame.place(relx=.02, rely=.08, anchor="w")


    new_window.mainloop()

