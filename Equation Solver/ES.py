nums = ["0","1","2","3","4","5","6","7","8","9","."]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def to_int(x):
    if x == int(x):
        return int(x)
    return x

def no_space(s: str) -> str:
    result = ""
    for i in s:
        if i != " ":
            result += i
    return result

def get_num_before(s: str,index: int,c=True) -> str:
    if s[index - 1] in nums:
        return str(get_num_before(s,index - 1,False) + s[index - 1])
    if c:
        return "0"
    return ""

def get_letter_after(s: str, index: int):
    if s[index + 1] in letters:
        return s[index + 1] + get_letter_after(s, index + 1)
    return ""

def solve(e: str, majhool: str = "x"):
    eq = no_space(e) + " "
    x = 0
    n = 0
    fase = 1
    other_majhool = dict({})

    for l in range(len(eq)):

        if eq[l] == majhool and eq[l] + get_letter_after(eq,l) == majhool:
            if eq[l - 1] in letters:
                continue
            g = float(get_num_before(eq,l))
            g = to_int(g)
            if g == 0 and eq[l - 1] != "0":
                g = 1

            if eq[l - len(str(g)) - 1] == "-" or (g == 1 and eq[l-1] == "-"):
                g *= -1

            x += fase * g
            
            continue
        
        if eq[l] in letters:
            if eq[l - 1] in letters:
                continue
            nmajhool = eq[l] + get_letter_after(eq,l)
            g = float(get_num_before(eq,l))
            g = to_int(g)
            if g == 0 and eq[l - 1] != "0":
                g = 1

            if eq[l - len(str(g)) - 1] == "-" or (g == 1 and eq[l-1] == "-"):
                g *= -1

            if nmajhool not in other_majhool.keys():
                other_majhool[nmajhool] = 0
            
            other_majhool[nmajhool] -= fase * g 
            
            continue

        if eq[l] not in nums:
            g = float(get_num_before(eq,l))
            g = to_int(g)

            if g != 0 and eq[l - len(str(g)) - 1] == "-":
                g *= -1

            n -= fase * g
        
        if eq[l] == "=":
            fase = -1
    
    if x < 0:
        n *= -1
        for i in other_majhool.keys():
            other_majhool[i] *= -1
        x *= -1
    
    if x != 0 and x != 1:
        n /= x
        for i in other_majhool.keys():
            other_majhool[i] /= x
        x = 1
    
    n = to_int(n)
    for i in other_majhool.keys():
        other_majhool[i] = to_int(other_majhool[i])
    
    result = ""
    if not(n == 0 and len(other_majhool.keys()) >= 1):
        result = str(n)

    for i in other_majhool.keys():
        if other_majhool[i] != 0:
            if other_majhool[i] > 0:
                result += "+"
            if other_majhool[i] != 1 and other_majhool[i] != -1:
                result += str(other_majhool[i])
            if other_majhool[i] == -1:
                result += "-"
            result += i

    return result
            

if __name__ == "__main__":

    eq = input("Enter your equation: ")
    answer = solve(eq)

    print(answer)