# Wacky Translator v1.0.0
# Programmer: Ilia Abbasi

from translate import Translator

FROM = "English"
TO = "Persian"

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

    text = input("")
    result = ""
    
    trn = Translator(from_lang = FROM, to_lang = TO)
    for word in words_of(text):
        trn_word = trn.translate(word)
        result = result + trn_word + " "

    with open("translation.txt", "wb") as file:
        file.write(result.encode("utf-8"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception caught: {e}")
        x = input()
