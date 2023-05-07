#STH (SeTil Hash) algorithm
#Designer: Ilia Abbasi
#https://github.com/ilia-abbasi/Python-projects/blob/main/STH/STH.py

BASE = 16
DIGEST_LENGTH = 64

def STH(s : str) -> str:
	
	pieces = ['N', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'L', 'R', 'E', 'X', 'T']
	chars = []
	digest = ""
	
	for i in range(len(s)):
		chars.append(ord(s[i]) % BASE)
	
	for i in range(DIGEST_LENGTH):
		x = (chars[i] * (len(chars) + 23) * chars[len(chars) - 1] + 5) % 2221
		chars.append(x)
	
	
	itr = 0
	while len(chars) > DIGEST_LENGTH:
		if itr >= DIGEST_LENGTH:
			itr = 0
		
		x = ((chars[len(chars) - 2] * chars[len(chars) - 1] * len(chars)) - 2) % 43 + 1
		chars[itr] = x
		chars.pop()
		itr += 1
	
	for i in range(DIGEST_LENGTH):
		digest += pieces[chars[i] % BASE + 1]
	
	
	return digest

def main():
    while 1:
        plain = input()
        print(STH(plain));

if __name__ == "__main__":
    main()
