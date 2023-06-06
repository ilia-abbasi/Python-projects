# siLocker v1.0.1
# Programmer: Ilia Abbasi 

import os
import sys
import base64
import hashlib
import toolbox as T # ReadMe
from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init as c_init
from cryptography.fernet import Fernet

VERSION = "1.0.0"
RELEASE = "Windows/Linux"
OS = os.name
SLSH = T.path_splitter()
BIOS_COMMAND = "wmic bios" if OS == "nt" else "dmidecode"
OWN_FILE_NAME = SLSH + T.own_file_name()
NO_LOCK_FOLDER = SLSH + "NO_LOCK_FOLDER" + SLSH
DEFAULT_KEY = "HQelmSeeZGKdX1AF6QyG5WTTNhOFjcb4FVMyTp4Don0="

failed_files = 0
all_files = 0


def wait() -> None:
    input()

def print_err(text) -> None:
    print(f"{Fore.RED}{text}{Style.RESET_ALL}")

def print_ok(text) -> None:
    print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")

def print_fatal(text) -> None:
    print(f"{Back.RED}{text}{Style.RESET_ALL}")

def print_warn(text) -> None:
    print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")

def sha256(s = None) -> str:    #returns sha256(s) in base64 encoding
    return base64.b64encode(hashlib.sha256(str(s).encode()).digest()).decode()

def show_help() -> None:
    print("-h   Show options(this page)\n")
    print("-v   Show version and release\n\n")
    print("Other options will be added in future updates.")

def show_version() -> None:
    print(f"siLocker v{VERSION} | Release: {RELEASE} | Ilia Abbasi")

def handle_key(key : str, mode : str) -> str:

    hashed_key = sha256(key)
    if mode == "N":
        return hashed_key.encode()
    
    bios_data = T.get_cmd_result(BIOS_COMMAND)

    if len(bios_data) < 80:
        raise Exception("Permission denied while trying to get BIOS info. try 'sudo'.")

    encryption_key = sha256(hashed_key + bios_data)

    return encryption_key.encode()

def setilock_all(f : Fernet, action : str, path : str = (os.getcwd() + SLSH), original_path : str = "") -> None:
    global failed_files, all_files

    if original_path == "":
        original_path = path
    
    for file in os.listdir(path):

        file_path = path + file

        if OWN_FILE_NAME == file_path[-len(OWN_FILE_NAME):]:
            continue
        if NO_LOCK_FOLDER in file_path:
            return
        
        if not os.path.isfile(file_path):
            setilock_all(f, action, file_path + SLSH, original_path)
            continue
        
        try:
            with open(file_path,"rb") as hostage:
                contents = hostage.read()
            
            all_files += 1
            better_file_path = file_path[len(original_path):]
            
            if action == "L":
                new_content = f.encrypt(contents)
            if action == "U":
                new_content = f.decrypt(contents)
            
            with open(file_path,"wb") as hostage:
                hostage.write(new_content)
        except:
            if action == "L":
                print_err(f"[-] Failed to lock {better_file_path}")
            if action == "U":
                print_err(f"[-] Failed to unlock {better_file_path}")
            failed_files += 1
        else:
            if action == "L":
                print(f"[+] Locked {better_file_path}")
            if action == "U":
                print(f"[+] Unlocked {better_file_path}")

def handle_argvs() -> None:

    argvs = list(sys.argv)
    if "-h" in argvs:
        argvs.remove("-h")
        show_help()
        exit()

    if "-v" in argvs:
        argvs.remove("-v")
        show_version()
        exit()
    

    if len(argvs) > 1:
        raise Exception("Invalid option. Try 'silocker -h' for help.")
        

def main():

    global failed_files, all_files

    c_init()
    handle_argvs()

    print(f"You are messing with:\n{T.cwd()}\ndirectory!\n")
    mode = input("STRICT MODE? (N/y) ")
    mode = T.handle_answer(mode, ["N", "Y"], default="N")

    key = input("KEY : ")
    key = handle_key(key, mode)
    
    action = input("(L)ock or (U)nlock? ")
    action = T.handle_answer(action, ["L", "U"])
    
    word = action + "nl" if action == "U" else action
    print("\n" + word + "ocking your files...\n")
    
    f = Fernet(key)
    setilock_all(f, action)
    
    print()
    if all_files == 0:
        print_warn(f"No file to {word.lower()}ock.")
    elif failed_files == 0:
        print_ok(f"Your files are {word.lower()}ocked.")
    elif failed_files == all_files and action == "L":
        print_fatal("Not even a single file was locked. Give the program enough privileges.")
    elif failed_files == all_files and action == "U":
        print_fatal("Not even a single file was unlocked. WRONG KEY.")
    elif action == "L":
        print_fatal(f"{failed_files} files out of {all_files} were not locked. Give the program enough privileges.")
    elif action == "U":
        print_fatal(f"{failed_files} files out of {all_files} were not unlocked. Corrupted data?")
    wait()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as k:
        print("You 'Ctrl-C'ed out of this place!")
    except Exception as e:
        print(f"Exception caught:\n{e}")
        wait()
