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

def if_filled(board):
    flag = True
    for row in range(9):
        for column in range(9):
            if type(board[row][column]) == list:
                flag = False
    return flag

def set_filter(board, row_filter, column_filter, blocks_filter):

    for row in range(9):
        for column in range(9):
            num = board[row][column]

            if type(num) == int:
                row_filter[row].append(num)
                column_filter[column].append(num)
                blocks_filter[get_block(row, column)].append(num)
    # print(f'{row_filter}\n{column_filter}\n{blocks_filter}')

def set_number(board, row_filter, column_filter, blocks_filter):
    fill = [1,2,3,4,5,6,7,8,9]

    for row in range(9):
        for column in range(9):
            l_var = list()
            num = board[row][column]

            if type(num) != int:
                for i in fill:
                    if i not in column_filter[column] and i not in row_filter[row] and i not in blocks_filter[get_block(row, column)]:
                        l_var.append(i)
                board[row][column] = l_var

def set_singleton(board,flag):
    flag.clear()
    for row in range(9):
        for column in range(9):
            num = board[row][column]
            if type(num) == int:
                pass
            elif len(num) == 1:
                board[row][column] = num[0]
                flag.append(True)



def solve(board):
    blocks = {(1,1):[],(1,2):[],(1,3):[],(2,1):[],(2,2):[],(2,3):[],(3,1):[],(3,2):[],(3,3):[]}
    b = [[],[],[],[],[],[],[],[],[]]
    l = [[],[],[],[],[],[],[],[],[]]

    flag = [True]


    while flag:
        set_filter(board, l, b, blocks)
        set_number(board, l, b, blocks)
        set_singleton(board, flag)

    #Logic Correction
    for row in range(9):
        for column in range(9):
            num = board[row][column]
            if type(num) == list:
                for maybe in num:
                    board[row][column] = maybe
                    temp_board = solve(board)
                    if if_filled(temp_board):
                        return temp_board

    return board






# board = [
#         [9,None,None,5,None,8,None,None,7],
#         [None,8,None,3,None,2,9,None,5],
#         [None,5,4,None,None,None,None,8,None],
#         [None,7,None,6,8,None,None,3,2],
#         [1,None,None,None,None,4,None,None,8],
#         [5,None,None,2,1,9,None,6,None],
#         [None,None,None,9,None,6,None,None,1],
#         [7,2,6,None,None,1,None,4,None],
#         [None,None,1,4,7,None,None,5,6],
#         ]

board = [
        [None,None,None,5,None,8,None,None,7],
        [None,8,None,3,None,2,9,None,5],
        [None,None,4,None,None,None,None,8,None],
        [None,7,None,6,8,None,None,3,2],
        [1,None,None,None,None,4,None,None,8],
        [5,None,None,2,1,9,None,6,None],
        [None,None,None,None,None,6,None,None,1],
        [None,None,None,None,None,1,None,4,None],
        [None,None,1,4,7,None,None,5,6],
        ]


answer = [
        [9,1,3,5,6,8,4,2,7],
        [6,8,7,3,4,2,9,1,5],
        [2,5,4,1,9,7,6,8,3],
        [4,7,9,6,8,5,1,3,2],
        [1,6,2,7,3,4,5,9,8],
        [5,3,8,2,1,9,7,6,4],
        [3,4,5,9,2,6,8,7,1],
        [7,2,6,8,5,1,3,4,9],
        [8,9,1,4,7,3,2,5,6],
        ]
for i in solve(board):
    print(i)

