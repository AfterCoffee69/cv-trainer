import customtkinter
import os
from customtkinter import filedialog
from tkinter import *
from TrainerModule import AITrainer

def startSquats():
    AITrainer("assets/squats.png", 24, 26, 28)

def startBiceps():
    AITrainer("assets/biceps2.png", 12, 14, 16)

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
label.pack(pady=15)

squats_button = customtkinter.CTkButton(master=widgets, text="Приседания",  command=startSquats)
squats_button.pack(pady=20, padx=10)

biceps_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс",  command=startBiceps) 
biceps_button.pack(pady=5, padx=10)

exit_button = customtkinter.CTkButton(master=widgets, text="Выход", fg_color="red",  command=exit)
exit_button.pack(pady=50, padx=10)

root.mainloop()