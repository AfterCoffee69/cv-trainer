import customtkinter
from customtkinter import filedialog
from tkinter import *
from TrainerModule import AITrainer

# Приседания | Градусы (185, 290)

def startSquats():
    AITrainer("assets/squats2.png", 23, 25, 27, "left", 185, 290)

def startSquatsLeftSide():
    AITrainer("assets/squats23.png", 24, 26, 28, "right", 185, 290)

# Подъём на бицепс | Градусы (210, 310)

def startBiceps():
    AITrainer("assets/biceps2.png", 12, 14, 16, "left", 210, 310)

def startBicepsLeftSide():
    AITrainer("assets/biceps23.png", 11, 13, 15, "right", 210, 310)

# Скручивания | Градусы (90, 130)

def startCurl():
    AITrainer("assets/curl.png", 26, 24, 12, "left", 230, 290)

def startCurlLeftSide():
    AITrainer("assets/curl2.png", 25, 23, 11, "right", 230, 290)


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

squats_button = customtkinter.CTkButton(master=widgets, text="Приседания", fg_color="#17612b",  command=startSquats)
squats_button.pack(pady=5, padx=10)

squats_left_button = customtkinter.CTkButton(master=widgets, text="Приседания (L)", fg_color="#17612b", command=startSquatsLeftSide)
squats_left_button.pack(pady=5, padx=10)

biceps_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс", fg_color="#175661", command=startBiceps) 
biceps_button.pack(pady=5, padx=10)

biceps_left_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс (L)", fg_color="#175661", command=startBicepsLeftSide) 
biceps_left_button.pack(pady=5, padx=10)

curl_button = customtkinter.CTkButton(master=widgets, text="Скручивания", fg_color="#371761",  command=startCurl) 
curl_button.pack(pady=5, padx=10)

curl_left_button = customtkinter.CTkButton(master=widgets, text="Скручивания (L)", fg_color="#371761",  command=startCurlLeftSide) 
curl_left_button.pack(pady=5, padx=10)

exit_button = customtkinter.CTkButton(master=widgets, text="Выход", fg_color="red",  command=exit)
exit_button.pack(pady=50, padx=10)

root.mainloop()