import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_NAME = os.path.join(BASE_DIR, "DATABASE", "error.json")

def load_error():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    


def save_log(level, message):

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            logs= json.load(file)
    else:
        logs = []

    log = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "level": level,
        "message": message
    }

    logs.append(log)

    with open(FILE_NAME, "w") as file:
        json.dump(logs, file, indent=4)

def view_error():
    errors = load_error() 

    if not errors:
        log_warning("Error not found")
        print("Error not found")   
        return

    print("=========================================")
    print("            View Error                   ") 
    print("==========================================")

    for error in errors:
        print("Time:", error["time"])
        print("Level:",error["level"]),
        print("Message:",error["message"]),

        print("=========================================")


def log_info(message):
    save_log("INFO", message)


def log_warning(message):
    save_log("WARNING", message)


def log_error(message):
    save_log("ERROR", message) 

         