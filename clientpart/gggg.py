from customtkinter import *


arr = ['gohn', 'mark', 'tvoyamama', 'alih']
tkroot = CTk()
def gg(event, obj):
    print('[CHOOSE]: ' + obj.cget('text'))

def new_chat(name):
    labelfont = ('courier', 20, 'bold')                
    widget = CTkLabel(tkroot, text=name, bg_color='red', font=labelfont, height=70, width=450)
    widget.pack(anchor="center", pady = (1,0))  
    widget.bind("<1>", lambda event, obj=widget: gg(event, obj))

for i in arr:
    new_chat(i)                        
tkroot.mainloop()

