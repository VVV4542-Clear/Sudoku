from random import choice
import random

def emp() -> list[list[None]]:
    board = [
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             [None,None,None,None,None,None,None,None,None],
             ]
    return board

def fill(board):
    for i in range(9):
        for j in range(9):
            board[i][j] = [1,2,3,4,5,6,7,8,9]
    return board

def get_block(row, column):
    if row in (0,1,2):
        n = 1
    elif row in (3,4,5):
        n = 2
    else:
        n = 3
    if column in (0,1,2):
        m = 1
    elif column in (3,4,5):
        m = 2
    else:
        m = 3
    return (n,m)


def create_board(board):
    #Initialising Blocklisst
    blocks = {(1,1):[],(1,2):[],(1,3):[],(2,1):[],(2,2):[],(2,3):[],(3,1):[],(3,2):[],(3,3):[]}
    b=[[],[],[],[],[],[],[],[],[]]

    for row in range(9):
        ln = []
        for column in range(9):
            l = [1,2,3,4,5,6,7,8,9]
            cured = []
            bn = b[column]

            #filter block
            for num in l:
                if num in bn or num in ln or num in blocks[get_block(row, column)]:
                    pass
                else:
                    cured.append(num)
            if cured == []:
                return

            #update block
            ch = choice(cured)
            b[column].append(ch)
            ln.append(ch)
            blocks[get_block(row, column)].append(ch)
            board[row][column] = ch

    global n
    n=False
    return board

n=True
while n:
    board = create_board(emp())
    if not n:
        print(board)
        for i in board:
            print(i)


