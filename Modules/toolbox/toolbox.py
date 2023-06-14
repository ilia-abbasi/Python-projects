# Toolbox v1.3.0
# Programmer: Ilia Abbasi

import os
import sys

class Answer_Exception(Exception):
    pass

def is_file(path : str) -> bool:
    return os.path.isfile(path)

def is_folder(path : str) -> bool:
    return os.path.isdir(path)

def path_exists(path : str) -> bool:
    return os.path.exists(path)

def save_file(file_name : str, extension : str, contents, mode : str = "t", smart : bool = False) -> str:
    full_name = file_name + extension

    if not smart or not is_file(full_name):
        with open(full_name, "w" + mode) as file:
            file.write(contents)
        return full_name
    
    i = 1
    while 1:
        file_name += str(i)
        full_name = file_name + extension
        if is_file(full_name):
            i += 1
            continue

        with open(full_name, "w" + mode) as file:
            file.write(contents)
        return full_name

def load_file(file_name : str, mode : str = "t", strict : bool = False, default_contents : str = ""):
    exists = is_file(file_name)
    if not exists and strict:
        raise FileNotFoundError
    if not exists and not strict:
        return default_contents
    
    with open(file_name, "r" + mode) as file:
        return file.read()

def raw_or_file(s : str) -> str:
    if not is_file(s):
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
