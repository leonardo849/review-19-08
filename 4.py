board = [[" ", " ", " "], 
         [" ", " ", " "], 
         [" ", " ", " "]]



def showBoard():
    print(f"{board[0][0]}|{board[0][1]}|{board[0][2]}")
    print(f"{board[1][0]}|{board[1][1]}|{board[1][2]}")
    print(f"{board[2][0]}|{board[2][1]}|{board[2][2]}")

board[0][0] = "O"
board[1][1] = "X"
board[2][2] = "X"

showBoard()