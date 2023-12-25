from customtkinter import *


arr = ['gohn', 'mark', 'tvoyamama', 'alih']
tkroot = CTk()
def gg(event, obj):
    print('[CHOOSE]: ' + obj.cget('text'))
    
for i in arr:
    labelfont = ('courier', 20, 'bold')                
    widget = CTkLabel(tkroot, text=i, bg_color='red', font=labelfont, height=70, width=450)
    widget.pack(anchor="center", pady = (1,0))  
    widget.bind("<1>", lambda event, obj=widget: gg(event, obj))                         
tkroot.mainloop()

