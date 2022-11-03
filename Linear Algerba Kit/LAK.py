# Programmer: Ilia Abbasi
import os

nums = ["0","1","2","3","4","5","6","7","8","9","."]

def pause():
    pause_program = input("")
    os.system("cls")

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

def get_num_before(s: str,index: int,c=1) -> str:
    if index == 0:
        return "0"
    if s[index - 1] in nums:
        return str(get_num_before(s,index - 1,c+1) + s[index - 1])
    if c == 1:
        return "0"
    return ""

def generate_equation(a,b) -> str:

    a = to_int(a)
    b = to_int(b)

    result = "y ="
    if a != 0:
        result += " "
        if a != 1 and a != -1:
            result += str(a)
        if a == -1:
            result += "-"
        result += "x"
    if a == 0 or (a != 0 and b != 0):
        result += " "
        if b > 0 and a != 0:
            result += "+ "
        if b < 0:
            result += "- "
        result += str(abs(b))
    return result

def solve(e: str,main: str,other: str,mode = 0):
    eq = no_space(e) + " "
    y = 0
    n = 0
    x = 0
    fase = 1

    for l in range(len(eq)):

        if eq[l] == main:
            g = float(get_num_before(eq,l))
            g = to_int(g)
            if g == 0 and eq[l - 1] != "0":
                g = 1

            if eq[l - len(str(g)) - 1] == "-" or (g == 1 and eq[l-1] == "-"):
                g *= -1

            y += fase * g
            
            continue
        
        if eq[l] == other:
            g = float(get_num_before(eq,l))
            g = to_int(g)
            if g == 0 and eq[l - 1] != "0":
                g = 1

            if eq[l - len(str(g)) - 1] == "-" or (g == 1 and eq[l-1] == "-"):
                g *= -1

            x -= fase * g
            
            continue

        if eq[l] not in nums:
            g = float(get_num_before(eq,l))
            g = to_int(g)

            if g != 0 and eq[l - len(str(g)) - 1] == "-":
                g *= -1

            n -= fase * g
        
        if eq[l] == "=":
            fase = -1
    
    if y < 0:
        y *= -1
        n *= -1
        x *= -1
    
    if y != 0:
        n /= y
        x /= y
        y = 1
    
    n = to_int(n)
    x = to_int(x)
    
    if mode == 1:
        return n

    result = generate_equation(x,n)

    return result

def fl1(vec1: tuple,vec2: tuple) -> str:

    a = None
    b = None

    if vec1[0] != vec2[0]:
        a = (vec1[1] - vec2[1]) / (vec1[0] - vec2[0])
        a = to_int(a)
    
    if a != None:
        b = (a * -vec1[0]) + vec1[1]
        b = to_int(b)
    
    if b == None:
        return ("x = " + str(vec1[0]))
    
    result = generate_equation(a,b)
    return result

def fl2(vec: tuple, a: float) -> str:
    
    b = vec[1] - (a * vec[0])
    result = generate_equation(a,b)
    return result

def fl3(vec: tuple, b: float) -> str:
    
    a = (vec[1] - b) / vec[0]
    result = generate_equation(a,b)
    return result

def fl4(eq: str) -> str:
    return solve(eq,"y","x")

def fv5(line1: str, line2: str) -> tuple:
    l1 = no_space(solve(line1,"y","x"))
    #print(l1)
    l2 = no_space(solve(line2,"y","x"))
    #print(l2)
    l1 = l1[2::]
    l2 = l2[2::]
    #print(l1)
    #print(l2)
    s = l1 + "=" + l2
    x = solve(s,"x","y",1)
    #print(s)
    #print(x)
    s = ""
    l1 += " "
    for i in range(len(l1)):

        if l1[i] == "x":
            g = float(get_num_before(l1,i))
            g = to_int(g)
            if g == 0 and l1[i - 1] != "0":
                g = 1
            if l1[ i - len(str(g)) - int(g!=1)] == "-":
                g *= -1
                #print("YES")
            
            g *= x
            g = to_int(g)
            s += ("+" + str(g))
            continue

        if l1[i] not in nums:
            g = float(get_num_before(l1,i))
            g = to_int(g)

            if g != 0 and l1[i - len(str(g)) - 1] == "-":
                g *= -1
            if g != 0:
                s += ("+" + str(g))

    y = solve(s,"y","x",1) * -1
    #print(s)
    #print(y)
    return (x,y)
            
#End of Funcs

if __name__ == "__main__":

    while 1:
        print("Line: Y = aX + b")
        print("Vector: (X,Y)\n\n")
        print("FIND LINE:")
        print("1) Vector, Vector")
        print("2) Vector, a")
        print("3) Vector, b")
        print("4) Line (Not Standard)\n")
        print("FIND VECTOR:")
        print("5) Line, Line\n")
        choice = input("Your Choice: ")
        print("\n\n")

        if choice == "1":
            vec1x = float(input("Vector1 X = "))
            vec1y = float(input("Vector1 Y = "))
            vec2x = float(input("Vector2 X = "))
            vec2y = float(input("Vector2 Y = "))
            
            print(fl1((vec1x,vec1y),(vec2x,vec2y)))
            pause()
        if choice == "2":
            vecx = float(input("Vector X = "))
            vecy = float(input("Vector Y = "))
            a = float(input("a = "))

            print(fl2((vecx,vecy),a))
            pause()
        if choice == "3":
            vecx = float(input("Vector X = "))
            vecy = float(input("Vector Y = "))
            b = float(input("b = "))

            print(fl3((vecx,vecy),b))
            pause()
        if choice == "4":
            line = input("Line: ")

            print(fl4(line))
            pause()
        if choice == "5":
            line1 = input("Line1: ")
            line2 = input("Line2: ")

            print(fv5(line1,line2))
            pause()