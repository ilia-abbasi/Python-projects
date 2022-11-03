class Chess:
    __board = [['wR','wN','wB','wQ','wK','wB','wN','wR'],['wP']*8,['0']*8,['0']*8,['0']*8,['0']*8,['bP']*8,['bR','bN','bB','bQ','bK','bB','bN','bR']]
    __turn = 'w'
    __files = ['a','b','c','d','e','f','g','h']
    __king_moved = [False, False]
    __rook_moved = [[False, False], [False, False]]

    def get_pos(self, pos : str) -> list:
        result = [int(pos[1])-1,-1]
        for i in range(8):
            if pos[0] == self.__files[i]:
                result[1] = i
        return result
    
    def is_in_range(self, pos : str or list) -> bool:
        pos = self.get_pos(pos) if type(pos) is str else pos
        return (pos[0] < 8 and pos[0] > -1 and pos[1] < 8 and pos[1] > -1)
    
    def get_piece(self, pos : str or list, board : list = __board) -> str:
        pos = self.get_pos(pos) if type(pos) is str else pos
        piece = board[pos[0]][pos[1]]
        return piece if self.is_in_range(pos) else '!'

    def find_piece(self, piece : str, board : list = __board) -> list:
        for i in range(8):
            for j in range(8):
                if board[i][j] == piece:
                    return [i,j]
        return [-1,-1]

    def translate_specials(self, move : str, turn : str):
        result = move
        
        if move == '0-0' and turn == 'w':
            result = ['e1g1', 'h1f1']
        if move == '0-0' and turn == 'b':
            result = ['e8g8', 'h8f8']
        
        return result
        #Function not complete

    def __play(self, move : str, board : list = __board) -> list:
        start = self.get_piece(move[:2:], board)
        end = self.get_pos(move[2::])
        board[end[0]][end[1]] = start
        start = self.get_pos(move[:2:])
        board[start[0]][start[1]] = '0'
        return board
    
    def get_rook_move(self, pos : str or list, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        result = []

        temp_pos = list(pos)
        temp_pos[0] += 1
        while temp_pos[0] < 8:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] += 1
        
        temp_pos = list(pos)
        temp_pos[0] -= 1
        while temp_pos[0] > -1:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] -= 1
        
        temp_pos = list(pos)
        temp_pos[1] += 1
        while temp_pos[1] < 8:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[1] += 1
        
        temp_pos = list(pos)
        temp_pos[1] -= 1
        while temp_pos[1] > -1:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[1] -= 1
        
        return result
    
    def get_bishop_move(self, pos : str or list, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        result = []

        temp_pos = list(pos)
        temp_pos[0] += 1
        temp_pos[1] += 1
        while temp_pos[0] < 8 and temp_pos[1] < 8:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] += 1
            temp_pos[1] += 1
        
        temp_pos = list(pos)
        temp_pos[0] += 1
        temp_pos[1] -= 1
        while temp_pos[0] < 8 and temp_pos[1] > -1:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] += 1
            temp_pos[1] -= 1
        
        temp_pos = list(pos)
        temp_pos[0] -= 1
        temp_pos[1] += 1
        while temp_pos[0] > -1 and temp_pos[1] < 8:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] -= 1
            temp_pos[1] += 1
        
        temp_pos = list(pos)
        temp_pos[0] -= 1
        temp_pos[1] -= 1
        while temp_pos[0] > -1 and temp_pos[1] > -1:
            p = self.get_piece(temp_pos, board)
            result.append(list(temp_pos))
            if p != '0':
                break
            temp_pos[0] -= 1
            temp_pos[1] -= 1
        
        return result
    
    def get_knight_move(self, pos : str or list, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        result = []

        temp_pos = list(pos)
        temp_pos[0] += 2
        temp_pos[1] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[1] -= 2
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[0] -= 1
        temp_pos[1] -= 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[0] -= 2
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[0] -= 1
        temp_pos[1] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[1] += 2
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[0] += 1
        temp_pos[1] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        temp_pos[0] += 2
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        return result
    
    def get_pawn_move(self, pos : str or list, turn : str = __turn, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        val = 1 if turn == 'w' else -1
        result = []

        temp_pos = list(pos)
        temp_pos[0] += val
        if self.get_piece(temp_pos, board) != '0':
            return []
        result.append(list(temp_pos))
        temp_pos[0] += val
        if (pos[0] == 1 or pos[0] == 6) and (temp_pos[0] > -1 and temp_pos[0] < 8) and self.get_piece(temp_pos, board) == '0':
            result.append(list(temp_pos))
        
        return result

    def get_pawn_take(self, pos : str or list, turn : str = __turn, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        val = 1 if turn == 'w' else -1
        result = []

        temp_pos = list(pos)
        temp_pos[0] += val
        temp_pos[1] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[1] -= 2
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        return result
    
    def get_king_move(self, pos : str or list, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        result = []

        temp_pos = list(pos)

        temp_pos[0] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[1] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[0] -= 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[0] -= 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[1] -= 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[1] -= 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[0] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        temp_pos[0] += 1
        if self.is_in_range(temp_pos):
            result.append(list(temp_pos))
        
        return result
    
    def get_queen_move(self, pos : str or list, board : list = __board) -> list:
        pos = self.get_pos(pos) if type(pos) is str else pos
        return self.get_rook_move(pos, board) + self.get_bishop_move(pos, board)
    
    def is_check(self, pos : str or list, king_color : str, board : list = __board) -> bool:
        pos = self.get_pos(pos) if type(pos) is str else pos
        colors = ['w','b']
        index = colors.index(king_color)

        mylist = self.get_rook_move(pos, board)
        for i in mylist:
            p = self.get_piece(i, board)
            if p == (colors[not index] + 'R') or p == (colors[not index] + 'Q'):
                return True
        
        mylist = self.get_bishop_move(pos, board)
        for i in mylist:
            p = self.get_piece(i, board)
            if p == (colors[not index] + 'B') or p == (colors[not index] + 'Q'):
                return True
        
        mylist = self.get_knight_move(pos, board)
        for i in mylist:
            p = self.get_piece(i, board)
            if p == (colors[not index] + 'N'):
                return True
        
        mylist = self.get_pawn_take(pos, colors[index], board)
        for i in mylist:
            p = self.get_piece(i, board)
            if p == (colors[not index] + 'P'):
                return True
        
        return False
    
    def is_legal_move(self, move : str, turn : str = __turn, board : list = __board) -> bool:
        colors = ['w','b']
        index = colors.index(turn)
        
        if move == '0-0':
            rank = 7 if index else 0
            if board[rank][5] != '0' or board[rank][6] != '0':
                return False
            if board[rank][7] != colors[index] + 'R':
                return False
            if self.__king_moved[index]:
                return False
            if self.__rook_moved[index][1]:
                return False
            if self.is_check([rank, 4], colors[index], board) or self.is_check([rank, 5], colors[index], board) or self.is_check([rank, 6], colors[index], board):
                return False
            
            self.__king_moved[index] = True
            self.__rook_moved[index][1] = True

            return True

        if move == '0-0-0':
            pass

        if move[:2] == 'ep':
            pass
        
        if len(move) != 4:
            return False

        pos1 = self.get_pos(move[:2])
        pos2 = self.get_pos(move[2:])

        if not self.is_in_range(pos1) or not self.is_in_range(pos2):
            return False

        moving_piece = self.get_piece(pos1)
        landing_square = self.get_piece(pos2)
        
        if moving_piece[0] != turn or landing_square[0] == turn:
            return False
        
        if moving_piece[1] == 'R' and pos2 not in self.get_rook_move(pos1, board):
            return False
        if moving_piece[1] == 'B' and pos2 not in self.get_bishop_move(pos1, board):
            return False
        if moving_piece[1] == 'N' and pos2 not in self.get_knight_move(pos1, board):
            return False
        if moving_piece[1] == 'P' and not (pos2 in self.get_pawn_move(pos1, turn, board) or (pos2 in self.get_pawn_take(pos1, turn, board) and landing_square[0] == colors[not index])):       
            return False
        if moving_piece[1] == 'K' and pos2 not in self.get_king_move(pos1, board):
            return False
        if moving_piece[1] == 'Q' and pos2 not in self.get_queen_move(pos1, board):
            return False
        
        copy_board = []
        for f in board:
            copy_board.append(list(f))
        
        copy_board = self.__play(move, copy_board)
        if self.is_check(self.find_piece(turn + 'K', copy_board), turn, copy_board):
            return False
        #The move is legal and will happen.

        if move[:2] == 'a1' or move[2:] == 'a1':
            self.__rook_moved[0][0] = True
        if move[:2] == 'h1' or move[2:] == 'h1':
            self.__rook_moved[0][1] = True
        if move[:2] == 'a8' or move[2:] == 'a8':
            self.__rook_moved[1][0] = True
        if move[:2] == 'h8' or move[2:] == 'h8':
            self.__rook_moved[1][1] = True
        
        if self.get_piece(move[:2]) == 'wK':
            self.__king_moved[0] = True
        if self.get_piece(move[:2]) == 'bk':
            self.__king_moved[1] = True
        
        return True
    
    def go_for(self, move : str, turn : str = __turn, board : list = __board) -> None:
        if self.is_legal_move(move, turn, board):
            move = self.translate_specials(move, turn)
            if type(move) is list:
                for i in move:
                    self.__play(i, board)
                return True
            self.__play(move, board)
            return True
        return False
    
    def view(self, board : list = __board) -> None:
        print("_________________________________________")
        for i in range(7,-1,-1):
            for j in range(8):
                string = board[i][j] if board[i][j] != "0" else "  "
                print("| " + string + " ", end="")
            print("|")
            print("|____|____|____|____|____|____|____|____|")

def main():

    game = Chess()
    t = 'w'
    turns = ['w', 'b']
    index = 0

    print("welcome to chess!")
    print("* Long castle, En passant and Promotion is not available yet.")
    print("1) Player vs Player")
    print("2) Player vs Computer (Not available, coming soon.)")
    x = input()

    while x == "1":
        game.view()
        move = input('Play a move (Format: e2e4): ')

        if game.go_for(move,t):
            index = not index
            t = turns[index]

if __name__ == "__main__":
    main()