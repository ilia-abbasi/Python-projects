# Wacky Translator v2.0.0
# Programmer: Ilia Abbasi

import toolbox as T
from translate import Translator

FROM = "English"
TO = "Persian"

def wait() -> None:
    input()

def smart_trim(s : str) -> str:

    s = s.rstrip()
    s = s.lstrip()
    result = ""

    for char in s:
        if char != " ":
            result += char
            continue
        
        if result[-1] == " ":
            continue
        result += char
    
    return result

def words_of(s : str) -> None:
    
    word = ""
    for i in range(len(s)):
        if s[i] == " ":
            yield word
            word = ""
            continue
        word = word + s[i]

    yield word
    return


def main():

    text = smart_trim(input("Text: "))
    result = ""
    
    trn = Translator(from_lang = FROM, to_lang = TO)
    for word in words_of(text):
        trn_word = trn.translate(word)
        result = result + trn_word + " "

    name = "translation"
    txt = ".txt"
    result = result.encode("utf-8")
    mode = "b"
    print(f"Translation saved as \"{T.save_file(name, txt, result, mode, True)}\" !")
    wait()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nYou 'Ctrl-C'ed out of this place!")
    except Exception as e:
        print(f"Exception caught: {e}")
        wait()
