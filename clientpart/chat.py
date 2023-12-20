from customtkinter import *

win = CTk()
win.geometry("800x600")
win.resizable(False, False)

frameleft = CTkFrame(win, width=300, height=600, fg_color='gray', bg_color='gray')
frameleft.pack(expand=True, side='left', anchor='w')

frameright = CTkFrame(win, width=500, height=600)
frameright.pack(expand=True, side='right', anchor='e')



win.mainloop()