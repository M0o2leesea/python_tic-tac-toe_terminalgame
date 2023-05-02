board=['-','-','-','-','-','-','-','-','-']

def display_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

def check(display_board):
    p1= 'X'
    p2= 'O'
    if board[0]==board[1]==board[2]==p1 or board[3]==board[4]==board[5]==p1 or board[6]==board[7]==board[8]==p1 or board[0]==board[3]==board[6]==p1 or board[1]==board[4]==board[7]==p1 or board[2]==board[5]==board[8]==p1 or board[0]==board[4]==board[8]==p1 or board[2]==board[4]==board[6]==p1:
        print("Player 1 wins")
        return True
    elif board[0]==board[1]==board[2]==p2 or board[3]==board[4]==board[5]==p2 or board[6]==board[7]==board[8]==p2 or board[0]==board[3]==board[6]==p2 or board[1]==board[4]==board[7]==p2 or board[2]==board[5]==board[8]==p2 or board[0]==board[4]==board[8]==p2 or board[2]==board[4]==board[6]==p2:
        print("Player 2 wins")
        return True 
    else:
        return False
    
player1=input("Enter the name of player 1: ")   
player2=input("Enter the name of player 2: ")
print("Welcome to the game of tic-tac-toe")
print("Player 1 is X and Player 2 is O")
print("The board is as follows")
display_board()
print("Player 1 will start the game")
print("Enter the position where you want to place your mark")
print("The positions are as follows")
print("1 | 2 | 3")
print("4 | 5 | 6")
print("7 | 8 | 9")
print("Enter the position number from 1 to 9")
def game():
    i=0
    while i<9:
        if i%2==0:
            print(player1+"'s turn")
            position=int(input())
            board[position-1]='X'
            display_board()
            if check(display_board):
                break
        else:
            print(player2+"'s turn")
            position=int(input())
            board[position-1]='O'
            display_board()
            if check(display_board):
                break
        i=i+1
game()