import customtkinter
from customtkinter import filedialog
from tkinter import *
from TrainerModule import AITrainer

# Приседания | Градусы (195, 280)

def startSquats():
    AITrainer("assets/squats2.png", 23, 25, 27)

def startSquatsLeftSide():
    AITrainer("assets/squats2.png", 24, 26, 28)

# Подъём на бицепс | Градусы (210, 310)

def startBiceps():
    AITrainer("assets/biceps2.png", 12, 14, 16)

def startBicepsLeftSide():
    AITrainer("assets/biceps2.png", 11, 13, 15)

# Скручивания | Градусы (190, 270)

def startCurl():
    AITrainer("assets/curl.png", 12, 24, 26)

def startCurl():
    AITrainer("assets/curl.png", 11, 23, 25)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_widget_scaling(2.0)
customtkinter.set_window_scaling(2.0)

root = customtkinter.CTk()

root.title('AI Trainer')

widgets = customtkinter.CTkFrame(master=root)
widgets.pack(side = RIGHT, padx=15, pady=15, expand=TRUE, fill=BOTH)

label = customtkinter.CTkLabel(master=widgets, text="AI Trainer", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=24))
label.pack(pady=20)

squats_button = customtkinter.CTkButton(master=widgets, text="Приседания",  command=startSquats)
squats_button.pack(pady=5, padx=10)

biceps_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс",  command=startBiceps) 
biceps_button.pack(pady=5, padx=10)

curl_button = customtkinter.CTkButton(master=widgets, text="Скручивания",  command=startCurl) 
curl_button.pack(pady=5, padx=10)

exit_button = customtkinter.CTkButton(master=widgets, text="Выход", fg_color="red",  command=exit)
exit_button.pack(pady=50, padx=10)

root.mainloop()