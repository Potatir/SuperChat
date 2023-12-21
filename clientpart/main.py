from customtkinter import *
from reg import regwin

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
CTkLabel(master=frame, text="Войдите в свой аккаунт", text_color="#7E7E7E", anchor="w", justify="left",
         font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="Логин", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="Пароль:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14),
         compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000",
         show="*").pack(anchor="w", padx=(25, 0))

CTkButton(master=frame, text="Войти", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

CTkButton(master=frame, text="Зарегистрироваться", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225, command=regwin).pack(anchor="w", pady=(40, 0), padx=(25, 0))

win.mainloop()
