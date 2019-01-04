import os

# Tao mang 2 chieu co kich thuoc 3X3

# CAC HAM CHUC NANG
# ==========================================================
def checkValueIsIntAndInArray(value, n, m):
    while True:
        value = input()
        try:
            value = int(value)
            if value >= n and value <= m:
                return value
            else:
                print("Gia tri phai >= %d va <= %d" %(n, m))
        except:
            print("Gia tri phai la 1 so:")

# ==========================================================

def displayBoard(board):
    print(' %s | %s | %s ' % (board[0][0], board[0][1], board[0][2]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[1][0], board[1][1], board[1][2]))
    print('-' * 11)
    print(' %s | %s | %s ' % (board[2][0], board[2][1], board[2][2]))

# Kiem tra mang da day chua
def isFullBoard(board):
    return (sum(x.count(' ') for x in board) == 0)

def checkWinner(board, letter):
            # Hang ngang
    return ((board[0][0] == letter and board[0][1] == letter and board[0][2] == letter) or
            (board[1][0] == letter and board[1][1] == letter and board[1][2] == letter) or
            (board[2][0] == letter and board[2][1] == letter and board[2][2] == letter) or
            # Hang doc
            (board[0][0] == letter and board[1][0] == letter and board[2][0] == letter) or
            (board[0][1] == letter and board[1][1] == letter and board[2][1] == letter) or
            (board[0][2] == letter and board[1][2] == letter and board[2][2] == letter) or
            # Cheo
            (board[0][0] == letter and board[1][1] == letter and board[2][2] == letter) or
            (board[0][2] == letter and board[1][1] == letter and board[2][0] == letter))

# Ham ghi gia tri "X" or "O" vao board
def go(board, row, col, letter):
    board[row][col] = letter

def changeLetter(letter):
    if letter == 'X':
        return 'O'
    else:
        return 'X'

def changePlayer(player):
    if(player == 'player 1'):
        return 'player 2'
    else:
        return 'player 1'

def isSpace(board, row, col):
    return board[row][col] == ' '  


def reset():
    global board
    board = [[' '] * 3 for i in range(3)]
    select()

def play(board, player):
    temp = 0
    row = 0
    col = 0
    playerLetter = ''
    playerName = 'player 1'

    if player == 1:
        playerLetter = 'X'
    else:
        playerLetter = 'O'
    os.system("cls")
    while True:
        os.system('cls')
        if not isFullBoard(board):
            # os.system('cls')
            displayBoard(board)
            print('%s danh: ' %playerName)
            while True:
                temp = checkValueIsIntAndInArray(temp, 1, 9)
                row = int((temp - 1)/3)
                col = int((temp - 1)%3)
                if isSpace(board, row, col):
                    break
                else:
                    print("Da co, danh lai:")
                    
            go(board, row, col, playerLetter)
            if checkWinner(board, playerLetter):
                os.system('cls')
                displayBoard(board)
                print("%s thang" %(playerName))
                break
            else:
                playerLetter = changeLetter(playerLetter)
                playerName = changePlayer(playerName)
        else:
            print("2 ben hoa nhau!")
            break

    temp = input("Ban co muon choi tiep? (y/n): ")
    if temp.startswith('y'):
        os.system('cls')
        select()
    else:
        return

def menu():
    print("1. Play with X")
    print("2. Play with O")
    print("3.Exit")

def select():
    player = 1
    board = [[' '] * 3 for i in range(3)]
    menu()
    print("Ban chon: ")
    player = checkValueIsIntAndInArray(player, 1, 3)
    if player == 1:
        play(board, player)
    
    if player == 2:
        play(board, player)
    
    if player == 3:
        return
        

def main():
    select()

main()