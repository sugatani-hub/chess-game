class Game_Status():
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["  ","  ","  ","  ","  ","  ","  ","  "],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.player = True

    def checkmate(self):
        if(self.player):
            for row in range(8):
                for col in range(8):
                    if(self.board[row][col] == "wK"):
                        return False
            return True
        else:
            for row in range(8):
                for col in range(8):
                    if(self.board[row][col] == "bK"):
                        return False
            return True
    
    def make_move(self,player_click):
        self.board[player_click[1][0]][player_click[1][1]] = self.board[player_click[0][0]][player_click[0][1]]
        self.board[player_click[0][0]][player_click[0][1]] = "  "
        self.player = not self.player

    def check_move(self,player_click):
        origin =  player_click[0]
        dest = player_click[1]
        return not(self.board[origin[0]][origin[1]] == "  " or origin == dest or self.player and self.board[origin[0]][origin[1]][0] == "b" or not(self.player) and self.board[origin[0]][origin[1]][0] == "w" or self.board[origin[0]][origin[1]][0] == self.board[dest[0]][dest[1]][0])
    
    def check_move_piece(self,player_click):
        match self.board[player_click[0][0]][player_click[0][1]][1]:
            case "P":
                return self.get_Pawn_moves(player_click)
            case "R":
                return self.get_Rook_moves(player_click)
            case "N":
                return self.get_Night_moves(player_click)
            case "B":
                return self.get_Bishop_moves(player_click)
            case "Q":
                return self.get_Queen_moves(player_click)
            case "K":
                return self.get_King_moves(player_click)
        return False
    
    def get_Pawn_moves(self, player_click):
        origin_row = player_click[0][0]
        origin_col = player_click[0][1]
        dest_row = player_click[1][0]
        dest_col = player_click[1][1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            return ((origin_col == dest_col and (origin_row == 6 and dest_row==4 or origin_row == dest_row+1) and self.board[dest_row][dest_col] == "  ") or (abs(origin_col-dest_col) == 1 and origin_row == dest_row+1 and self.board[dest_row][dest_col][0]=="b"))
        elif(self.board[origin_row][origin_col][0]=="b" and not self.player):
            return ((origin_col == dest_col and (origin_row == 1 and dest_row==3 or origin_row == dest_row-1) and self.board[dest_row][dest_col] == "  ") or (abs(origin_col-dest_col) == 1 and origin_row == dest_row-1 and self.board[dest_row][dest_col][0]=='w'))

    def get_Rook_moves(self, player_click):
        origin_row = player_click[0][0]
        origin_col = player_click[0][1]
        dest_row = player_click[1][0]
        dest_col = player_click[1][1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            if((origin_col==dest_col or origin_row == dest_row) and not(origin_col == dest_col and origin_row == dest_row)):
                if(origin_col == dest_row):
                    if(origin_row<dest_row):
                        for i in range(origin_row+1,dest_row):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_row-1,dest_row,-1):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                else:
                    if(origin_col<dest_col):
                        for i in range(origin_col+1,dest_col):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_col-1,dest_col,-1):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
            else:
                return False
        elif(self.board[origin_row][origin_col][0] == "b" and not self.player):
            if((origin_col == dest_col or origin_row == dest_row) or (not(origin_col == dest_col and origin_row == dest_row)) and not(self.board[dest_row][dest_col][0] == "b")):
                if(origin_col==dest_col):
                    if(origin_row<dest_row):
                        for i in range(origin_row+1,dest_row):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_row-1,dest_row,-1):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                else:
                    if(origin_col<dest_col):
                        for i in range(origin_col+1, dest_col):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_col-1,dest_col,-1):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
            else:
                return False
        else:
            return False

    def get_Night_moves(self,player_click):
        origin_row = player_click[0][0]
        origin_col = player_click[0][1]
        dest_row = player_click[1][0]
        dest_col = player_click[1][1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            if((abs(origin_col-dest_col) == 2 and abs(origin_row-dest_row) == 1) or (abs(origin_col-dest_col) == 1 and abs(origin_row-dest_row) == 2)):
                return True
            else:
                return False
        elif(self.board[origin_row][origin_col][0] == "b" and not self.player):
            if((abs(origin_col-dest_col) == 2 and abs(origin_row-dest_row) == 1) or (abs(origin_col-dest_col) == 1 and abs(origin_row-dest_row) == 2)):
                return True
            else:
                return False
        else:
            return False

    def get_Bishop_moves(self,player_click):
        origin_row = player_click[0][0]
        origin_col = player_click[0][1]
        dest_row = player_click[1][0]
        dest_col = player_click[1][1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            if(abs(origin_row-dest_row) == abs(origin_col-dest_col)):
                if(origin_row<dest_row and origin_col<dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row+i][origin_col+i] == "  ")):
                            return False
                    return True
                elif(origin_row>dest_row and origin_col>dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row-i][origin_col-i] == "  ")):
                            return False
                    return True
                elif(origin_row<dest_row and origin_col>dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row+i][origin_col-i] == "  ")):
                            return False
                    return True
                else:
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row-i][origin_col+i] == "  ")):
                            return False
                    return True
            else:
                return False
        elif(self.board[origin_row][origin_col][0] == "b" and not self.player):
            if(abs(origin_row-dest_row) == abs(origin_col-dest_col)):
                if(origin_row<dest_row and origin_col<dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row+i][origin_col+i] == "  ")):
                            return False
                    return True
                elif(origin_row>dest_row and origin_col>dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row-i][origin_col-i] == "  ")):
                            return False
                    return True
                elif(origin_row<dest_row and origin_col>dest_col):
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row+i][origin_col-i] == "  ")):
                            return False
                    return True
                else:
                    for i in range(1,abs(origin_row-dest_row)):
                        if(not(self.board[origin_row-i][origin_col+i] == "  ")):
                            return False
                    return True
            else:
                return False
        else:
            return False

    def get_Queen_moves(self,player_click):
        origin_row = player_click[0][0]
        origin_col = player_click[0][1]
        dest_row = player_click[1][0]
        dest_col = player_click[1][1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            if(origin_col == dest_col or origin_row == dest_row or abs(origin_row - dest_row) == abs(origin_col - dest_col)):
                if(origin_col==dest_col):
                    if(origin_row<dest_row):
                        for i in range(origin_row+1,dest_row):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_row-1,dest_row,-1):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                elif(origin_row == dest_row):
                    if(origin_col<dest_col):
                        for i in range(origin_col+1, dest_col):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_col-1,dest_col,-1):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                elif(abs(origin_row-dest_row) == abs(origin_col-dest_col)):
                    if(origin_row<dest_row and origin_col<dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row+i][origin_col+i] == "  ")):
                                return False
                        return True
                    elif(origin_row>dest_row and origin_col>dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row-i][origin_col-i] == "  ")):
                                return False
                        return True
                    elif(origin_row<dest_row and origin_col>dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row+i][origin_col-i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row-i][origin_col+i] == "  ")):
                                return False
                        return True
            else:
                return False
        elif(self.board[origin_row][origin_col][0] == "b" and not self.player):
            if(origin_col == dest_col or origin_row == dest_row or abs(origin_row - dest_row) == abs(origin_col - dest_col)):
                if(origin_col==dest_col):
                    if(origin_row<dest_row):
                        for i in range(origin_row+1,dest_row):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_row-1,dest_row,-1):
                            if(not(self.board[i][origin_col] == "  ")):
                                return False
                        return True
                elif(origin_row == dest_row):
                    if(origin_col<dest_col):
                        for i in range(origin_col+1, dest_col):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(origin_col-1,dest_col,-1):
                            if(not(self.board[origin_row][i] == "  ")):
                                return False
                        return True
                elif(abs(origin_row-dest_row) == abs(origin_col-dest_col)):
                    if(origin_row<dest_row and origin_col<dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row+i][origin_col+i] == "  ")):
                                return False
                        return True
                    elif(origin_row>dest_row and origin_col>dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row-i][origin_col-i] == "  ")):
                                return False
                        return True
                    elif(origin_row<dest_row and origin_col>dest_col):
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row+i][origin_col-i] == "  ")):
                                return False
                        return True
                    else:
                        for i in range(1,abs(origin_row-dest_row)):
                            if(not(self.board[origin_row-i][origin_col+i] == "  ")):
                                return False
                        return True
            else:
                return False
        else:
            return False

    def get_King_moves(self,player_click):
        origin_row,origin_col = player_click[0]
        dest_row, dest_col = player_click[1]
        if(self.board[origin_row][origin_col][0]=="w" and self.player):
            if(abs(origin_row-dest_row) <= 1 and abs(origin_col-dest_col) <= 1):
                return True
            else:
                return False
        elif(self.board[origin_row][origin_col][0] == "b" and not self.player):
            if(abs(origin_row-dest_row) <= 1 and abs(origin_col-dest_col) <= 1):
                return True
            else:
                return False
        else:
            return False