board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

def display_board():
    print('|', board[0],'|', board[1],'|', board[2],'|')
    print('|', board[3],'|', board[4],'|', board[5],'|')
    print('|', board[6],'|', board[7],'|', board[8],'|')


def check_horizontal(val1, val2, val3, sign):
    if board[val1] == board[val2] == board[val3] == sign:
        print(f"{sign} WINS !")
        return True
    
def check_vertical(val1, val2, val3, sign):
    if board[val1] == board[val2] == board[val3] == sign:
        print(f"{sign} WINS !")
        return True
    
def check_diagonal(val1, val2, val3):
    if board[val1] == board[val2] == board[val3] == "x":
        print("X WINS !")
        return True
    elif board[val1] == board[val2] == board[val3] == "o":
        print("O WINS !")
        return True


def check_win():
    win = False
    for i in range(0, 9, 3):
        win = check_horizontal(i, i+1, i+2, 'x')
        if win:
            return win
        win = check_horizontal(i, i+1, i+2, 'o')
        if win:
            return win
    for i in range(3):
        win = check_vertical(i, i+3, i+6, 'x')
        if win:
            return win
        win = check_vertical(i, i+3, i+6, 'o')
        if win:
            return win
    
    win = check_diagonal(0, 4, 8)
    if win:
        return win
    win = check_diagonal(2, 4, 6)
    if win:
        return win
    
    
def move(sign):
    turn = int(input(f"Choose a spot {sign}: [1-9] "))
    if turn > 0 and turn < 10 and board[turn - 1] == "_":
        board[turn - 1] = sign
    else:
        print("Invalid move !")
        move(sign)
        
        
def game():
    count = 0
    while True:

        display_board()
        if count > 2:
            if check_win():
                break

        move("x")
        display_board()

        if count > 1:
            if check_win():
                break

        if count == 4:
            print("YOU BOTH PLAYED WELL !\n IT'S A TIE !!!")
            break

        move("o")

        count += 1

game()