# Setilia Safe v1.0.0
# Programmer: Ilia Abbasi

import os
import rsa
import base64
import hashlib
import toolbox as T
from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init as c_init


def clear() -> None:
    os.system("cls")

def pause() -> None:
    input()

def print_pub(text : any = "") -> None:
    print(f"{Fore.BLACK}{Back.GREEN}{text}{Style.RESET_ALL}")

def print_pri(text : any = "") -> None:
    print(f"{Fore.BLACK}{Back.RED}{text}{Style.RESET_ALL}")

def print_cph(text : any = "") -> None:
    print(f"{Fore.BLACK}{Back.YELLOW}{text}{Style.RESET_ALL}")


class Setilia_Safe:
    __public_key = {"key": None, "name": None, "tag": None}
    __private_key = {"key": None, "name": None, "tag": None}
    __cipher = None
    __cipher_tag = None

    def sha384(self, b : bytes) -> str:
        return base64.b64encode(hashlib.sha384(b).digest()).decode()
    
    def cipher_is_none(self) -> bool:
        return self.__cipher == None

    def pub_key_is_none(self) -> bool:
        return self.__public_key["key"] == None
    
    def pri_key_is_none(self) -> bool:
        return self.__private_key["key"] == None
    
    def keys_are_none(self) -> bool:
        return self.pub_key_is_none() and self.pri_key_is_none()

    def set_pub_key_info(self, key_name : str) -> bool:
        if self.__public_key["key"] == None:
            return False
        
        pub_bytes = self.__public_key["key"].save_pkcs1("PEM")
        digest = self.sha384(pub_bytes)
        tag = digest[:7]

        self.__public_key["name"] = key_name
        self.__public_key["tag"] = tag

        return True
    
    def set_pri_key_info(self, key_name : str) -> bool:
        if self.__private_key["key"] == None:
            return False
        
        pri_bytes = self.__private_key["key"].save_pkcs1("PEM")
        digest = self.sha384(pri_bytes)
        tag = digest[:7]

        self.__private_key["name"] = key_name
        self.__private_key["tag"] = tag

        return True

    def set_cipher_tag(self) -> bool:
        if self.__cipher == None:
            return False
        
        digest = self.sha384(self.__cipher)
        tag = digest[:7]
        self.__cipher_tag = tag

        return True

    def generate_keys(self, key_name : str, key_size : int) -> bool:
        pub_name = key_name + "_Public.pem"
        pri_name = key_name + "_Private.pem"

        if T.is_file(pub_name) or T.is_file(pri_name):
            return False
        
        (public_key, private_key) = rsa.newkeys(key_size)
        with open(pub_name, "wb") as p:
            p.write(public_key.save_pkcs1("PEM"))
        with open(pri_name, "wb") as p:
            p.write(private_key.save_pkcs1("PEM"))
        
        if self.keys_are_none():
            self.load_keys(key_name)
        
        return True
    
    def load_pub_key(self, key_name : str) -> bool:
        pub_name = key_name + "_Public.pem"

        if not T.is_file(pub_name):
            return False
        
        with open(pub_name, "rb") as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        
        self.__public_key["key"] = public_key
        self.set_pub_key_info(key_name)

        return True
    
    def load_pri_key(self, key_name : str) -> bool:
        pri_name = key_name + "_Private.pem"

        if not T.is_file(pri_name):
            return False
        
        with open(pri_name, "rb") as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        
        self.__private_key["key"] = private_key
        self.set_pri_key_info(key_name)

        return True
    
    def load_keys(self, key_name : str) -> bool:
        pub_name = key_name + "_Public.pem"
        pri_name = key_name + "_Private.pem"

        if not (T.is_file(pub_name) and T.is_file(pri_name)):
            return False

        self.load_pub_key(key_name)
        self.load_pri_key(key_name)

        return True

    def save_cipher(self, file_name : str) -> str:
        new_file_name = T.save_file(file_name, ".dat", self.__cipher, "b", True)
        return new_file_name

    def load_cipher(self, file_name : str) -> bool:
        new_file_name = ""
        if T.is_file(file_name + ".dat"):
            new_file_name = file_name + ".dat"
        if T.is_file(file_name):
            new_file_name = file_name
        file_name = new_file_name

        if file_name == "":
            return False

        with open(file_name, "rb") as file:
            self.__cipher = file.read()
        self.set_cipher_tag()
        
        return True

    def encrypt(self, message : str, key) -> bool:
        try:
            self.__cipher = rsa.encrypt(message.encode("ascii"), key)
        except:
            return False
        
        self.set_cipher_tag()

        return True

    def decrypt(self, key):
        try:
            msg = rsa.decrypt(self.__cipher, key).decode("ascii")
        except:
            return False
        
        return msg
    
    def get_pub_name(self) -> str:
        return str(self.__public_key["name"])
    
    def get_pri_name(self) -> str:
        return str(self.__private_key["name"])
    
    def get_pub_key(self) -> rsa.PublicKey:
        return self.__public_key["key"]
    
    def get_pri_key(self) -> rsa.PrivateKey:
        return self.__private_key["key"]

    def show_info(self) -> None:
        print_pub( " _________________________________ ")
        print_pub( "| PUBLIC  KEY                     |")
        print_pub( "|---------------------------------|")
        print_pub(f"| {self.__public_key['name']}" + ((32 - len(str(self.__public_key["name"]))) * " ") + "|")
        print_pub(f"| {self.__public_key['tag']}" + ((32 - len(str(self.__public_key["tag"]))) * " ") + "|")
        print_pub( "|_________________________________|")
        print_pub( "                                   ")
        print()

        print_pri( " _________________________________ ")
        print_pri( "| PRIVATE  KEY                    |")
        print_pri( "|---------------------------------|")
        print_pri(f"| {self.__private_key['name']}" + ((32 - len(str(self.__private_key["name"]))) * " ") + "|")
        print_pri(f"| {self.__private_key['tag']}" + ((32 - len(str(self.__private_key["tag"]))) * " ") + "|")
        print_pri( "|_________________________________|")
        print_pri( "                                   ")
        print()

        print_cph( " _____________ ")
        print_cph( "| CIPHER      |")
        print_cph( "|-------------|")
        print_cph(f"| {self.__cipher_tag}" + ((12 - len(str(self.__cipher_tag))) * " ") + "|")
        print_cph( "|_____________|")
        print_cph( "               ")



def main() -> None:
    
    c_init()

    safe = Setilia_Safe()

    while True:
        clear()
        safe.show_info()

        print()
        print("1) Generate Key Pair            2) Load Key Pair")
        print("3) Load Public Key              4) Load Private Key")
        print("5) Encrypt                      6) Decrypt")
        print("7) Load Cipher                  8) Quit")
        print()
        choice = input("Your Choice: ")
        clear()

        if choice == "1":
            key_name = input("The name of your key pair: ")
            
            print("Choose the security level of your key pair:")
            print()
            print("1) Sus    (117 chars) 1024-bit")
            print("2) Decent (245 chars) 2048-bit")
            print("3) High   (501 chars) 4096-bit")
            print()
            x = input("Your Choice: ")
            x = int(x)

            clear()
            if x < 1 or x > 3:
                print("Invalid choice.")
                pause()
                continue

            print("Please be patient. This process can take minutes.")

            key_size = 2 ** (9 + x)
            succeed = safe.generate_keys(key_name, key_size)
            
            clear()

            if not succeed:
                print("Failed. At least one key exists with the same name.")
                pause()
                continue
            
            print("Successful.")
            pause()
            continue
        
        if choice == "2":
            key_name = input("The name of the key pair: ")
            clear()

            succeed = safe.load_keys(key_name)
            
            if not succeed:
                print("Failed. At least one key is missing.")
                pause()
                continue

            print("Successful.")
            pause()
            continue

        if choice == "3":
            key_name = input("The name of the public key: ")
            clear()

            succeed = safe.load_pub_key(key_name)
            
            if not succeed:
                print("Failed. The key is missing.")
                pause()
                continue

            print("Successful.")
            pause()
            continue
        
        if choice == "4":
            key_name = input("The name of the private key: ")
            clear()

            succeed = safe.load_pri_key(key_name)
            
            if not succeed:
                print("Failed. The key is missing.")
                pause()
                continue

            print("Successful.")
            pause()
            continue

        if choice == "5":
            if safe.keys_are_none():
                print("Key slots are empty.")
                pause()
                continue
            
            print("Choose the encryption key:")
            print()
            if not safe.pub_key_is_none():
                print(f"1) Public  ({safe.get_pub_name()})")
            if not safe.pri_key_is_none():
                print(f"2) Private ({safe.get_pri_name()})")
            print()
            x = input("Your Choice: ")
            clear()

            if x != "1" and x != "2":
                print("Invalid choice.")
                pause()
                continue

            if x == "1" and safe.pub_key_is_none():
                print("Public key is not loaded.")
                pause()
                continue

            if x == "2" and safe.pri_key_is_none():
                print("Private key is not loaded.")
                pause()
                continue
            
            key = None

            if x == "1":
                key = safe.get_pub_key()
            if x == "2":
                key = safe.get_pri_key()
            
            max_chars = 0
            key_size = key.n.bit_length()

            if key_size == 1024:
                max_chars = 117
            if key_size == 2048:
                max_chars = 245
            if key_size == 4096:
                max_chars = 501

            text = input(f"Your text (max {max_chars}):\n\n")
            clear()

            if len(text) > max_chars:
                file_name = T.save_file("text", ".txt", text, "t", True)
                print(f"Max is {max_chars} but you entered {len(text)} chars.")
                print(f"Your text was saved in \"{file_name}\" so you can edit it.")
                pause()
                continue

            succeed = safe.encrypt(text, key)
            if not succeed:
                print("Something went wrong.")
                pause()
                continue

            file_name = safe.save_cipher("cipher")
            print(f"Cipher saved as \"{file_name}\".")
            pause()
            continue
        
        if choice == "6":
            if safe.cipher_is_none():
                print("Cipher slot is empty")
                pause()
                continue

            if safe.keys_are_none():
                print("Key slots are empty.")
                pause()
                continue
            
            print("Choose the decryption key:")
            print()
            if not safe.pub_key_is_none():
                print(f"1) Public  ({safe.get_pub_name()})")
            if not safe.pri_key_is_none():
                print(f"2) Private ({safe.get_pri_name()})")
            print()
            x = input("Your Choice: ")
            clear()

            if x != "1" and x != "2":
                print("Invalid choice.")
                pause()
                continue

            if x == "1" and safe.pub_key_is_none():
                print("Public key is not loaded.")
                pause()
                continue

            if x == "2" and safe.pri_key_is_none():
                print("Private key is not loaded.")
                pause()
                continue
            
            key = None

            if x == "1":
                key = safe.get_pub_key()
            if x == "2":
                key = safe.get_pri_key()
            
            succeed = safe.decrypt(key)
            if not type(succeed) is str:
                print("Failed. Wrong key or corrupted cipher.")
                pause()
                continue

            print(succeed)
            print()
            x = input("Save? (Y/n): ")
            x = T.handle_answer(x, ["y", "n"], default = "y").lower()

            clear()
            if x != "y":
                continue

            file_name = T.save_file("plain", ".txt", succeed, "t", True)
            print(f"Saved as \"{file_name}\".")
            pause()
            continue
        
        if choice == "7":
            file_name = input("Name of the cipher file: ")
            clear()

            succeed = safe.load_cipher(file_name)
            if not succeed:
                print("File not found.")
                pause()
                continue

            print("Successful.")
            pause()
            continue

        if choice == "8":
            quit(0)



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("You 'Ctrl-C'ed out of this place!")
    except Exception:
        print("Something went wrong, Can't display the error due to security reasons.")
        print("Maybe the key is wrong or the data is corrupted.")
        print("Contact the developer.")
