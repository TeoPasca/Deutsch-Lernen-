#!/usr/bin/python
import sys
import json
from termcolor import colored
import os
from pathlib import Path
import random
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

import os

def load_dict(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

    
def save_dict(file_path, my_dict):
    with open(file_path, "w") as f:
        json.dump(my_dict, f, indent=4)

def select_word(my_dict):
    selected_word = random.choice(list(my_dict.keys()))
    return selected_word, my_dict[selected_word]

def practice(file_path_lektion, file_path_lektion_correct, language):
    my_dict = load_dict(file_path_lektion)
    removed_dict = load_dict(file_path_lektion_correct)

    if language == "rumänische":
        new_dict = {v: k for k, v in my_dict.items()}

    while True:
        if not my_dict:
            print(colored("Keine Worte mehr zum Üben!", "red"))
            break
        selected_word, correct_answer = select_word(my_dict)
        for i in range(3):
            user_input = input(f"Wie lautet die {language} Übersetzung von '{colored(selected_word, attrs=['bold'])}': ")
            if user_input == correct_answer:
                print(colored("Richtig!", "green"))
                removed_dict[selected_word] = my_dict.pop(selected_word)
                save_dict(file_path_lektion_correct, removed_dict)
                break
            elif user_input.lower() == "q":
                sys.exit()
            elif user_input.lower() == "r":
                list_text()
            else:
                print(colored("Incorrect", "red"))
                if i == 2:
                    print(colored("Die richtige Übersetzung ist:", "red"), colored(correct_answer, "green"))
    return

def print_menu():
    print(f"+------------------+\n|1. Datei wählen   |\n+------------------+\n|Drücken Sie q/r   |\n+------------------+")


def enter(name_file):
    file_path_lektion = os.path.join(ROOT_DIR, "Deutsch lernen", "Lektionen", name_file)
    print(f"Aktuelle Lektion: {name_file}")
    my_dict = load_dict(file_path_lektion)

    while True:
        key = input(colored("Wort: ", "black", "on_white"))
        if key == "q":
            sys.exit()
        elif key == "r":
            list_text()
        value = input("Cuvant: ")
        if value == "q":
            break
        elif value == "w":
            list_text()
        my_dict[key] = value
        save_dict(file_path_lektion, my_dict)

    return            
def choose_data(language, ro, color):
    file_name = "lektion_"
    format = ".json"
    string ="Wählen:"
    bold = attr=['bold']

    while True:
        user_input = input(f"{colored(string ,color, attrs=['bold'] )}{file_name}")
        if user_input == "r":
            list_text()
        elif user_input == "q":
            list_text()
        else:
            file_path_lektion = os.path.join(ROOT_DIR, "Deutsch lernen", "Lektionen", f"{file_name}{user_input}{format}")
            file_path_lektion_wrong = os.path.join(ROOT_DIR, "Deutsch lernen", "Niedrige Priorität", f"{file_name}{user_input}{ro}{format}")
            if os.path.exists(file_path_lektion):
                practice(file_path_lektion, file_path_lektion_wrong, language)
            else:
                print("Datei nicht gefunden. Bitte versuchen Sie es erneut.")

def choose_data_en():
    file_name = "lektion_"
    lektion = ".json"
    user_input = input("Wählen:lektion_")
    file_lektion =f"{file_name}{user_input}{lektion}"
    
    file_path_lektion = os.path.join(ROOT_DIR, "Deutsch lernen", "Lektionen", file_lektion)
    
    if not os.path.isfile(file_path_lektion):
        print(colored(f"Die Datei {file_lektion} existiert nicht.", "red"))
        return
    
    enter(file_path_lektion)

def create_data():
    file_name = "lektion_"
    lektion = ".json"
    lektion_correct = "_correct.json"
    lektion_correct_ro = "_correct_ro.json"
    print("+-----------------+")
    print("|Lektion erstellen|")
    print("+-----------------+")
    print("|Drücken Sie q/r  |")
    print("+-----------------+")
    user_input = input("lektion_")
    
    if user_input == "r":
        list_directory()
    elif user_input == "q":
        sys.exit()
    
    file_lektion =f"{file_name}{user_input}{lektion}"
    file_lektion_correct  =f"{file_name}{user_input}{lektion_correct}"
    file_lektion_correct_ro  =f"{file_name}{user_input}{lektion_correct_ro}"

    dir_path_lek = os.path.join(ROOT_DIR, "Deutsch lernen", "Lektionen", file_lektion)
    dir_path_correct = os.path.join(ROOT_DIR, "Deutsch lernen","Niedrige Priorität",file_lektion_correct)
    dir_path_correctro = os.path.join(ROOT_DIR, "Deutsch lernen","Niedrige Priorität",file_lektion_correct_ro)
    try:
        save_dict(dir_path_lek, {})
        save_dict(dir_path_correct, {})
        save_dict(dir_path_correctro, {})
        print(f"Die {file_lektion} wurde erstellt")
    except FileExistsError:
         print(f"Die {file_lektion} existiert bereits") 
    list_directory()   
def list_directory_ro():
    print_menu()
    lektionen_dir = os.path.join(ROOT_DIR, "Deutsch lernen","Lektionen")
    lektionen_content = os.listdir(lektionen_dir)
    for files in lektionen_content:
        print(files)
    print("+------------------+")
    choose_data("rumänische", "_correct_ro", "black")
def list_directory_de():
    print_menu()
    lektionen_dir = os.path.join(ROOT_DIR, "Deutsch lernen","Lektionen")
    lektionen_content = os.listdir(lektionen_dir)
    for files in lektionen_content:
        print(files)
    print("+------------------+")
    choose_data("deutsche", "_correct", "yellow")
def list_directory():
    print("+----------------+")
    print("|1.Datei erstellen|")
    print("|2.Datei wählen   |")
    print("+-----------------+")
    print("|Drücken Sie q/r  |")
    print("+-----------------+")
    
    lektionen_dir = os.path.join(ROOT_DIR, "Deutsch lernen","Lektionen")
    lektionen_content = os.listdir(lektionen_dir)
    for files in lektionen_content:
        print(files)
    print("-------------")
    while True:
        choose_1 = input(colored("Wählen:","green", attrs=["bold"]))
        if choose_1 == "1":
            create_data()  
        elif choose_1 == "2":
            choose_data_en()
        elif choose_1 == "r":
            list_text()
        elif choose_1 == "q":
            sys.exit()
        else:
            print("Wählen Sie oben aus")
def list_text(): 
    print("+--------------------------+")
    print("|1 Lektion erstellen\wählen|")
    print("|2.Üben                    |") 
    print("|3.Exerciții               |")
    print("+--------------------------+")
    print("|Drücken Sie q/r           |")
    print("+--------------------------+")
    while True:
        choose_1 = input(colored("Wählen:", "red", attrs=["bold"]))
        if choose_1 == "1":
            list_directory()
        elif choose_1 == "2":
            list_directory_de()
        elif choose_1 == "3":
            list_directory_ro()
        elif choose_1 == "q":
            sys.exit()
        else:
            print("Wählen Sie oben aus")
def directories():
    

    root_dir = "Deutsch lernen"
    root_dir_path = os.path.join(ROOT_DIR, root_dir)
    os.makedirs(root_dir, exist_ok=True)

    sub_dir1 = "Lektionen"
    sub_dir2 = "Niedrige Priorität"
    sub_dir1_path= os.path.join(root_dir_path, sub_dir1)
    sub_dir2_path= os.path.join(root_dir_path, sub_dir2)
    
    os.makedirs(sub_dir1_path, exist_ok=True)
    os.makedirs(sub_dir2_path, exist_ok=True)
    list_text()
if __name__  == '__main__':
    directories()