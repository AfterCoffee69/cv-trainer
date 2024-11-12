import customtkinter
from tkinter import *
import PIL
from PIL import Image
from TrainerModule import AITrainer
import json
import os
from UserModule import *

def exit_fullscreen(event):
    root.attributes('-fullscreen', False)
    
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

def back_to_users():
    widgets.pack_forget()
    enter.pack(side=LEFT, padx=(15,15), pady=15, expand=TRUE, fill=BOTH)

def save_user_data(data):
    username = data['username']
    filename = os.path.join(users_folder, f'{username}.json')

    with open(filename, 'w') as file:
        json.dump(data, file)

def load_user_data(username):
    filename = os.path.join(users_folder, f'{username}.json')

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return None

def user_exists(username):
    for profile in user_profiles:
        if profile['username'] == username:
            return True
    return False

def choose_user(username):
    json_filename = f"users_data/{username}.json"
    
    try:
        with open(json_filename, 'r') as file:
            user_data = json.load(file)

            user_height = int(user_data.get('height'))
            user_weight = int(user_data.get('weight'))

            bmi = user_weight / (user_height / 100) ** 2
            print(f"ИМТ {round(bmi, 1)}")

        widgets.pack(side=RIGHT, padx=(10, 15), pady=15, expand=TRUE, fill=BOTH)
        enter.pack_forget()
        bg_lbl.pack_forget()
    except FileNotFoundError:
        print(f"Файл {json_filename} не найден")

def choose_user_on_click(username):
    choose_user(username)

def submit():
    if entry_name.get() and entry_age.get() and entry_height.get() and entry_weight.get():
        username = entry_name.get()

        if user_exists(username):
            error_label.configure(text=f'Профиль "{username}" уже существует', text_color='red')
        else:
            error_label.configure(text=f'Профиль "{entry_name.get()}" создан', text_color='green')

        data = {
            'username': entry_name.get(),
            'age': entry_age.get(),
            'height': entry_height.get(),
            'weight': entry_weight.get()
        }
        save_user_data(data)

        user_profiles.append(data)

        # profile_button = customtkinter.CTkButton(master=profile_list, text=profile['username'], font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=lambda username=profile['username']: choose_user_on_click(username))
        # profile_button.pack(pady=5)
        

        profile_button = customtkinter.CTkButton(master=profile_list, text=entry_name.get(), font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=lambda username=entry_name.get(): choose_user_on_click(username))
        profile_button.pack(pady=5)

    else:
        error_label.configure(text='Заполните все поля', text_color='red')

users_folder = 'users_data'
if not os.path.exists(users_folder):
    os.makedirs(users_folder)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_widget_scaling(1.5)
customtkinter.set_window_scaling(1.5)

root = customtkinter.CTk()
root.geometry('800x600')
root.attributes('-fullscreen', True)
root.bind('<Escape>', exit) 

root.title('AI Trainer')

widgets = customtkinter.CTkFrame(master=root)
# widgets.pack(side = RIGHT, padx=(10,15), pady=15, expand=TRUE, fill=BOTH)
widgets.pack_forget()

label = customtkinter.CTkLabel(master=widgets, text="AI Trainer", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=26))
label.pack(pady=20)

squats_button = customtkinter.CTkButton(master=widgets, text="Приседания", fg_color="#17612b", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startSquats)
squats_button.pack(pady=5, padx=10)

squats_left_button = customtkinter.CTkButton(master=widgets, text="Приседания (L)", fg_color="#17612b", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startSquatsLeftSide)
squats_left_button.pack(pady=5, padx=10)

biceps_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс", fg_color="#175661", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startBiceps) 
biceps_button.pack(pady=5, padx=10)

biceps_left_button = customtkinter.CTkButton(master=widgets, text="Подъём на бицепс (L)", fg_color="#175661", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startBicepsLeftSide) 
biceps_left_button.pack(pady=5, padx=10)

curl_button = customtkinter.CTkButton(master=widgets, text="Скручивания", fg_color="#371761", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startCurl) 
curl_button.pack(pady=5, padx=10)

curl_left_button = customtkinter.CTkButton(master=widgets, text="Скручивания (L)", fg_color="#371761", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=startCurlLeftSide) 
curl_left_button.pack(pady=5, padx=10)

exit_button = customtkinter.CTkButton(master=widgets, text="Назад", fg_color="red", font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=back_to_users)
exit_button.pack(pady=(20,30), padx=10)

###################
# DATA ENTRY LABEL
###################


enter = customtkinter.CTkFrame(master=root)
enter.pack(side=LEFT, padx=(15,15), pady=15, expand=TRUE, fill=BOTH)

enter_label = customtkinter.CTkLabel(master=enter, text="Создание профиля", font=customtkinter.CTkFont(family="Roboto", weight="bold", size=24))
enter_label.pack(pady=20, padx=10)

entry_name = customtkinter.CTkEntry(master=enter, placeholder_text="Имя", width=400, height=40, state="normal")
entry_name.pack(pady=5, padx=10)

entry_age = customtkinter.CTkEntry(master=enter, placeholder_text="Возраст",  width=400, height=40, state="normal")
entry_age.pack(pady=5, padx=10)

entry_height = customtkinter.CTkEntry(master=enter, placeholder_text="Рост",  width=400, height=40, state="normal")
entry_height.pack(pady=5, padx=10)

entry_weight = customtkinter.CTkEntry(master=enter, placeholder_text="Вес",  width=400, height=40, state="normal")
entry_weight.pack(pady=5, padx=10)

submit = customtkinter.CTkButton(master=enter, text="Создать",  width=400, height=40, command=submit)
submit.pack(pady=(20,0), padx=10)

error_label = customtkinter.CTkLabel(master=enter, text="", font=customtkinter.CTkFont(family="Roboto", weight="bold", size=12))
error_label.pack(pady=0)

profile_list = customtkinter.CTkScrollableFrame(master=enter, border_width=2)
profile_list.pack(side=RIGHT, padx=5, pady=15, expand=TRUE, fill=BOTH)

profile_label = customtkinter.CTkLabel(master=profile_list, text="Выберите профиль", font=customtkinter.CTkFont(family="Roboto", weight="bold", size=20))
profile_label.pack(pady=20, padx=10)

user_profiles = []

for file in os.listdir(users_folder):
    if file.endswith('.json'):
        data = load_user_data(file.split('.')[0])
        if data:
            user_profiles.append(data)

for profile in user_profiles:

    profile_button = customtkinter.CTkButton(master=profile_list, text=profile['username'], font=customtkinter.CTkFont(family="Roboto", weight="bold" , size=22), width=500, height=50, command=lambda username=profile['username']: choose_user_on_click(username))
    profile_button.pack(pady=5)

root.mainloop()