# Toolbox v1.0.1
# Programmer: Ilia Abbasi

import os
import sys

class Answer_Exception(Exception):
    pass

def save_file(file_name : str, contents, mode : str = "t", smart : bool = False) -> str:
    if not smart or not os.path.isfile(file_name):
        with open(file_name, "w" + mode) as file:
            file.write(contents)
        return file_name
    
    i = 1
    while 1:
        file_name += str(i)
        if os.path.isfile(file_name):
            i += 1
            continue

        with open(file_name, "w" + mode) as file:
            file.write(contents)
        return file_name

def raw_or_file(s : str) -> str:
    if not os.path.isfile(s):
        return s
    
    with open(s, "rt") as file:
        return file.read()

def handle_answer(answer : str, options : list, case_sensitive : bool = False, one_char : bool = True, default : str = "") -> str:
    if answer == "":
        answer = default
    if answer == "":
        raise Answer_Exception("No answer recieved.")
    
    if one_char:
        answer = answer[0]

    if not case_sensitive:
        answer = answer.upper()
        for i in range(len(options)):
            options[i] = str(options[i]).upper()
    
    if answer not in options:
        raise Answer_Exception(f"Invalid answer: {answer}")
    
    return answer

def own_file_name() -> str:
    return os.path.basename(sys.argv[0])

def cwd() -> str:
    return os.getcwd()

def path_splitter() -> str:
    if "/" in cwd():
        return "/"
    if "\\" in cwd():
        return "\\"
    
    raise Exception("Failed to find path_splitter of this OS.")

def roaming_appdata() -> str:
    return os.getenv('APPDATA')

def local_appdata() -> str:
    return os.getenv('LOCALAPPDATA')

def get_cmd_result(command : str) -> str:
    os.system(command + " > temp.tbx")
    with open("temp.tbx", "rt") as file:
        contents = file.read()
    os.remove("temp.tbx")
    return contents
