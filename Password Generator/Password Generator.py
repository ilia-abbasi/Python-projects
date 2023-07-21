# Password Generator
# Programmer: Ilia Abbasi

from random import randint

UPPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWS = "abcdefghijklmnopqrstuvwxyz"
NUMS = "0123456789"
SPCS = "!@#$?/"

def generate_password(length : int = 8) -> str:

    password = []
    password.append(UPPS[randint(0,25)])
    password.insert(randint(0,1), LOWS[randint(0,25)])
    password.insert(randint(0,2), NUMS[randint(0,9)])
    password.insert(randint(0,3), SPCS[randint(0,5)])
    length -= 4

    all = UPPS + LOWS + NUMS + SPCS
    for i in range(length):
        password.insert(randint(0,i+5), all[randint(0,67)])
    
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
