#If you are not my friend, ignore this script.

import os
import json
import base64
import hashlib
import toolbox as T
from selenium import webdriver

URL = "Link site"
DIR = ""

def clear():
    os.system("cls")

def pause():
    input("Press Enter to continue...")

class STL_Exception(Exception):
    pass

class Setilia:
    __name = ""
    __id = -1
    __setil = -1
    __msgs = None
    __options = webdriver.ChromeOptions()
    __options.add_argument("headless")
    __driver = webdriver.Chrome(options = __options)

    def __init__(self) -> None:
        self.__driver.get(URL)

    def is_int(self, v) -> bool:
        v = str(v).strip()
        return v == '0' or (v if v.find('..') > -1 else v.lstrip('-+').rstrip('0').rstrip('.')).isdigit()
    
    def js_escape(self, s : str) -> str:
        return s.replace("\\", "\\\\").replace("\n", "\\n").replace("\"", "\\\"")
    
    def to_base64(self, s : str) -> str:
        base64_str = base64.b64encode(bytes(s, 'utf-8'))
        return base64_str.decode("utf-8")

    def cut_and_clean_str(self, s : str, max_len : int = -1) -> str:
        if max_len == -1:
            max_len = len(s)
        
        s = s[:max_len]
        s = s.replace("\\", "\\\\")
        s = s.replace("\"", "\\\"")

        return s

    def send_request(self, request : str) -> str:
        return self.__driver.execute_script(request)
    
    def sha256(self, plain : str) -> str:
        return hashlib.sha256(plain.encode()).hexdigest()

    def configure(self) -> str:
        if T.is_folder(DIR[:-1]) and T.is_file(CON_DIR):
            return "Config OK."
        
        print("Creating config...")

        os.makedirs(DIR[:-1])
        
        with open(CON_DIR, "wt"):
            pass
        
        return "Config was created."
    
    def update_msgs(self, msg : str = "", reciever : str = "Global") -> None:
        if reciever == "" or reciever == None:
            reciever = "Global"
        msg = self.cut_and_clean_str(msg, 200)
        reciever = reciever[:20]
        request = f"return api_send_msg(\"{msg}\", \"{reciever}\");"
        respond = self.send_request(request)

        self.__msgs = json.loads(respond) #ValueError or TypeError
    
    def print_msgs(self) -> None:
        
        print("---- START OF MESSAGES ----\n")
        for i in self.__msgs:
            if i[""] == "<i class=\"material-icons ondelete\">block</i>This message was deleted":
                i[""] = "DELETED MESSAGE"
            print(i[""] + " " + i[""])

    def do_gt(self, job : str, amount : int = 0) -> str:
        request = f"return api_do_gt(\"{job}\", \"{amount}\");"
        respond = self.send_request(request)

        if respond != "Successful." and not self.is_int(respond):
            return "Error: " + str(respond)
        
        return respond
    
    def my_info(self) -> dict:
        request = "return api_my_info();"
        respond = self.send_request(request)

        json_result = json.loads(respond) #ValueError or TypeError
        self.__name = json_result[""]
        self.__id = int(json_result[""])
        self.__setil = int(json_result[""])

        return json_result
    
    def pay_rt(self, amount : int = 0) -> str:
        request = f"return api_pay_rt({amount});"
        respond = self.send_request(request)

        return respond

    def get_id(self, username : str) -> str:
        request = f"return api_get_id(\"{username}\");"
        respond = self.send_request(request)

        return respond
    
    def submit_block(self, block : str, proof) -> str:
        request = f"return api_submit_block(\"{block}\", \"{proof}\");"
        respond = self.send_request(request)

        return respond
    
    def show_info(self) -> None:
        print(f"{self.__name} : {self.__id}")
        print(f"{self.__setil} STL\n")
    
    def reload(self) -> None:
        self.my_info()
    


def main():
    setilia = Setilia()


    print("--- Setilia DESKTOP ---\n")

    username = input("Username: ")
    password = input("Password: ")

    print("Logging in...")
    print(setilia.login(username, password))
    print("Checking config...")
    print(setilia.configure())
    print("Loading...")
    print("Loaded.")
    print("Checking sync...")
    print("Getting necessary info...")
    setilia.reload()
    print("Getting orders from server...")

    while 1:
        clear()
        print("--- Setilia DESKTOP ---\n")

        setilia.show_info()

        print("1) Chat")
        print("2) GT Dargah")
        print("3) RT Dargah")
        print("4) Get ID")
        print("5) Submit Block")
        print("6) Reload")
        print("7) Quit")

        choice = input("\nYour Choice: ")
        clear()

        if choice == "1":
            rec = input("Reciever: ")
            print("Fetching data ... Be patient.")
            setilia.update_msgs(reciever = rec)
        while choice == "1":
            clear()
            setilia.print_msgs()

            msg = input("\nYour Message(! to cancel): ")
            if msg == "!":
                break
            
            clear()
            print("Fetching data ... Be patient.")
            setilia.update_msgs(msg, rec)
        
        while choice == "2":
            clear()
            print("Fetching data ... Be patient.")
            my_info = setilia.my_info()
            my_gt = my_info["gt"]
            my_setil = my_info["setil"]
            gt_rate = setilia.do_gt("get_rate")
            clear()

            print(f"GT rate  : {gt_rate} STL")
            print(f"Your GTs : {my_gt} GT")
            print(f"Your STLs: {my_setil} STL")

            amount = input("Amount of GTs to be converted(! to cancel): ")
            if amount == "!":
                break

            print("Converting... Be patient.")
            respond = setilia.do_gt("convert_gt", int(amount))
            clear()
            print(respond)
            pause()
        
        while choice == "3":
            clear()
            print("Fetching data ... Be patient.")
            my_info = setilia.my_info()
            my_rt = my_info["rt"]
            my_setil = my_info["setil"]
            clear()

            print( "RT Price : 500 STL")
            print(f"Your RTs : {my_rt} RT")
            print(f"Your STLs: {my_setil} STL")

            amount = input("Amount of RTs to be paid off(! to cancel): ")
            if amount == "!":
                break

            print("Paying off... Be patient.")
            respond = setilia.pay_rt(int(amount))
            clear()
            print(respond)
            pause()
        
        if choice == "4":
            clear()
            username = input("Username: ")
            print("Fetching data ... Be patient.")
            their_id = setilia.get_id(username)
            print(f"Their ID: {their_id}")
            pause()
        
        if choice == "5":
            clear()
            block = input("Block: ")
            proof = input("Proof: ")
            print("Fetching data ... Be patient.")
            respond = setilia.submit_block(block, proof)

            clear()
            print(respond)
            pause()
        
        if choice == "6":
            clear()
            print("Reloading your information ... Be patient.")
            setilia.reload()
        
        if choice == "7":
            quit()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou 'Ctrl-C'ed out of this place!")
    except (ValueError, TypeError) as e:
        clear()
        print(f"Value/TypeError caught. Probably a JSON malfunction. Error body:\n\n{e}")
        pause()
    except STL_Exception as e:
        clear()
        print(f"In-Program-Error caught. Error body:\n\n{e}")
        pause()
