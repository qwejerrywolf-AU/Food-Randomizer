import json
from datetime import datetime

def load_dishes():
    #Load dish data from dishes.json file
    with open("dishes.json", "r", encoding="utf-8") as file:
        return json.load(file)

def save_history(history):
    #Save consumption history to history.json
    with open("history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)

def load_history():
    #Load consumption history from history.json
    try:
        with open("history.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_dish(new_dish):
    #Add a new dish to dishes.json with validation
    try:
        dishes = load_dishes()
    except FileNotFoundError:
        dishes = []
    dishes.append(new_dish)
    with open("dishes.json", "w", encoding="utf-8") as file:
        json.dump(dishes, file, ensure_ascii=False, indent=2)