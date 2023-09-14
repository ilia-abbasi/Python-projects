# Password Generator v1.1.0
# Programmer: Ilia Abbasi

from random import randint
from secrets import choice as choose_random

UPPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWS = "abcdefghijklmnopqrstuvwxyz"
NUMS = "0123456789"
SPCS = "!@#$?/"

def generate_password(length : int = 8) -> str:

    password = []
    password.append(secrets.choice(UPPS))
    password.insert(randint(0,1), choose_random(LOWS))
    password.insert(randint(0,2), choose_random(NUMS))
    password.insert(randint(0,3), choose_random(SPCS))
    length -= 4

    everything = UPPS + LOWS + NUMS + SPCS
    for i in range(length):
        password.insert(randint(0,i+5), choose_random(everything))
    
    password = "".join(password)
    return password

def main() -> None:

    while 1:
        length = input("Length: ")
        if length == "":
            length = 8
        length = int(length)

        if length < 8:
            raise Exception("Min length is 8.")
        
        print(generate_password(length))
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou 'Ctrl-C'ed out of this place!")
    except Exception as e:
        print(f"Exception caught:\n{e}")
