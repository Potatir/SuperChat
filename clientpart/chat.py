from customtkinter import *

win = CTk()
win.geometry("800x600")
win.resizable(False, False)

frameleft1 = CTkFrame(win, width=300, height=600, fg_color='gray', bg_color='gray')
frameleft1.pack(expand=True, side='left', anchor='w')

frameleft2 = CTkFrame(frameleft1, width=100, height=90, fg_color='red')
frameleft2.pack(expand=True, side='left', anchor='nw')

frameright = CTkFrame(win, width=500, height=600)
frameright.pack(expand=True, side='right', anchor='e')

win.mainloop()
