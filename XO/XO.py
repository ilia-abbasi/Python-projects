class XO:
    __board = [0,0,0,0,0,0,0,0,0]
    
    #plays a move
    def play(self, val : int, pos : int, b : list = __board) -> bool:
        if val > 2 or val < 1 or pos > 8 or pos < 0 or b[pos] != 0:
            return False
        b[pos] = val
        return True
    
    #finds how many val is present in b[positions]
    def count(self, val : int, positions : tuple, b : list = __board) -> int:
        result = 0
        for i in positions:
            if b[i] == val:
                result += 1
        return result

    #finds where the val is in b[positions]
    def find(self, val : int, positions : tuple, b : list = __board) -> int:
        for i in positions:
            if b[i] == val:
                return i
    
    #finds the cell that computer should play on a row or column or diagonal
    def find_danger(self, positions : tuple, piece : int, b : list = __board) -> int:
        if self.count(0,positions,b) == 1 and self.count(piece,positions,b) == 2:
            return self.find(0,positions,b)
        return -1
    
    #scans the whole b for moves
    def spot_moves(self, piece : int, b : list = __board) -> list:
        dangers = []
        dangers.append(self.find_danger((0,1,2),piece,b))
        dangers.append(self.find_danger((3,4,5),piece,b))
        dangers.append(self.find_danger((6,7,8),piece,b))
        dangers.append(self.find_danger((0,3,6),piece,b))
        dangers.append(self.find_danger((1,4,7),piece,b))
        dangers.append(self.find_danger((2,5,8),piece,b))
        dangers.append(self.find_danger((0,4,8),piece,b))
        dangers.append(self.find_danger((2,4,6),piece,b))
        
        dangers = list(filter(lambda x: x != -1, dangers))
        return dangers
    
    #analyzes the b in future to find a move
    def analyze(self, piece : int, moves : int, b : list = __board) -> int:
        default = 0
        for i in range(9):
            if b[i] == 0:
                default = i+10
                b[i] = piece
                if len(self.spot_moves(piece,b)) >= moves:
                    b[i] = 0
                    return i
                b[i] = 0
        
        return default
    
    #computer plays a move
    def computer(self, b : list = __board) -> None:
        dangers = self.spot_moves(1,b)
        wins = self.spot_moves(2,b)
        x = 0
        if len(wins) > 0: #instant win?
            self.play(2,wins[0])
            return
        if len(dangers) > 0: #instant block?
            self.play(2,dangers[0])
            return
        if len(wins) == 0: #create double threat
            x = self.analyze(2,2,b)
            if x > -1 and x < 9:
                self.play(2,x)
                return
        if len(wins) == 0: #create threat
            x = self.analyze(2,1,b)
            if x > -1 and x < 9:
                self.play(2,x)
                return
        if len(dangers) == 0: #avoid double dangers
            x = self.analyze(1,2,b)
            if x > -1 and x < 9:
                self.play(2,x)
                return
        if b[4] == 0:
            self.play(2,4)
            return
        x -= 10
        self.play(2,x)
    
    def check_winner(self, val : int, b : list = __board) -> bool:
        x = []
        x.append(self.count(val,(0,1,2),b))
        x.append(self.count(val,(3,4,5),b))
        x.append(self.count(val,(6,7,8),b))
        x.append(self.count(val,(0,3,6),b))
        x.append(self.count(val,(1,4,7),b))
        x.append(self.count(val,(2,5,8),b))
        x.append(self.count(val,(0,4,8),b))
        x.append(self.count(val,(2,4,6),b))
        for i in x:
            if i == 3:
                return True
        return False

    def is_draw(self, b : list = __board) -> bool:
        for i in b:
            if i == 0:
                return False
        return True

    def view(self, b : list = __board) -> None:
        new_b = []
        for i in b:
            if i == 0:
                new_b.append(" ")
                continue
            if i == 1:
                new_b.append("O")
                continue
            if i == 2:
                new_b.append("X")
        
        print(f"  {new_b[0]}  |  {new_b[1]}  |  {new_b[2]}  ")
        print("-----+-----+-----")
        print(f"  {new_b[3]}  |  {new_b[4]}  |  {new_b[5]}  ")
        print("-----+-----+-----")
        print(f"  {new_b[6]}  |  {new_b[7]}  |  {new_b[8]}  ")

def main():
    
    game = XO()
    
    choice = input("Do you want to play first?(y/n) ")
    if choice == 'n':
        game.computer()
    game.view()

    while 1:
        choice = int(input("\nPlay a move: "))
        choice -= 1
        print("" if game.play(1,choice) else "Illegal move")
        
        if game.check_winner(1):
            game.view()
            print("YOU WON!")
            break

        game.computer()
        game.view()

        if game.check_winner(2):
            print("YOU LOST!")
            break
        if game.is_draw():
            print("DRAW!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Exception caught: {e}")