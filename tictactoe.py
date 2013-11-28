ROW_1_INDEX = 1
ROW_2_INDEX = 2
ROW_3_INDEX = 3

COL_1_INDEX = 2
COL_2_INDEX = 4
COL_3_INDEX = 6

MARKER1 = 'X'
MARKER2 = 'O'
WINNER = ''


def tic_tac_toe():
    #initialize board
    board = [[' ',' ','1',' ','2',' ','3'], ['1',' ',' ',' ',' ',' ',' '], ['2',' ',' ',' ',' ',' ',' '], ['3',' ',' ',' ',' ',' ',' ']]
    current_loop = 0
    
    while not is_board_full(board) and not is_row_win(board) and not is_column_win(board) and not is_diagonal_win(board):
        print_board(board)
        if current_loop % 2 == 0:
            print 'USER X'
            marker = 'X'
        else:
            print 'USER O'
            marker = 'O'
        while True:
            row, col = get_input()
            if is_cell_empty(row, col, board):
                board[int(row)][int(col) * 2] = marker
                break
        current_loop = current_loop + 1
    
    print '-----\n'
    print '-----'
    print 'FINAL BOARD'
    print_board(board)
    print '-----'
    print WINNER
    print '-----'


def is_cell_empty(row, col, board):
    if board[int(row)][int(col) + 2] != ' ':
        print 'You may only enter in a valid cell'
        return False
    else:
        return True
        

def get_input():
    while True:
        row = raw_input('Enter Row (1/2/3): ')
        if row != '1' and row != '2' and row != '3':
            print 'Please enter a valid row'
        else:
            break
    
    while True:
        col = raw_input('Enter Column (1/2/3): ')
        if col != '1' and col != '2' and col != '3':
            print 'Please enter a valid column'
        else:
            break
    
    return row, col


def is_board_full(board):
    #look for tie
    board = [[board[ROW_1_INDEX][COL_1_INDEX], board[ROW_1_INDEX][COL_2_INDEX], board[ROW_1_INDEX][COL_3_INDEX]], [board[ROW_2_INDEX][COL_1_INDEX], board[ROW_2_INDEX][COL_2_INDEX], board[ROW_2_INDEX][COL_3_INDEX]], [board[ROW_3_INDEX][COL_1_INDEX], board[ROW_3_INDEX][COL_2_INDEX], board[ROW_3_INDEX][COL_3_INDEX]]]
    for row in board:
        for cell in row:
            if cell.upper() != MARKER1 and cell.upper() != MARKER2:
                return False
    global WINNER
    WINNER = 'USER X AND USER O TIE!'
    return True


def is_diagonal_win(board):
    #look for X or O occupying either diagonal
    global WINNER
    board = [[board[ROW_1_INDEX][COL_1_INDEX], board[ROW_1_INDEX][COL_2_INDEX], board[ROW_1_INDEX][COL_3_INDEX]], [board[ROW_2_INDEX][COL_1_INDEX], board[ROW_2_INDEX][COL_2_INDEX], board[ROW_2_INDEX][COL_3_INDEX]], [board[ROW_3_INDEX][COL_1_INDEX], board[ROW_3_INDEX][COL_2_INDEX], board[ROW_3_INDEX][COL_3_INDEX]]]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and (board[1][1].upper() == MARKER1 or board[1][1].upper() == MARKER2):
        WINNER = 'USER ' + board[1][1].upper() + ' IS THE WINNER!'
        return True
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and (board[1][1].upper() == MARKER1 or board[1][1].upper() == MARKER2):
        WINNER = 'USER ' + board[1][1].upper() + ' IS THE WINNER!'
        return True
    else:
        return False


def is_consecutive(first_value, cell, last_consecutive):
    consecutive = True
    if first_value == '' and (cell.upper() == MARKER1 or cell.upper() == MARKER2):
        first_value = cell
    elif cell == first_value:
        consecutive = True
    else:
        consecutive = False

    return first_value, consecutive and last_consecutive


def is_row_win(board):
    #look for X or O occupying any single row
    global WINNER
    board = [[board[ROW_1_INDEX][COL_1_INDEX], board[ROW_1_INDEX][COL_2_INDEX], board[ROW_1_INDEX][COL_3_INDEX]], [board[ROW_2_INDEX][COL_1_INDEX], board[ROW_2_INDEX][COL_2_INDEX], board[ROW_2_INDEX][COL_3_INDEX]], [board[ROW_3_INDEX][COL_1_INDEX], board[ROW_3_INDEX][COL_2_INDEX], board[ROW_3_INDEX][COL_3_INDEX]]]
    for row in board:
        consecutive = True
        first_row_value = ''
        for cell in row:
            first_row_value, consecutive = is_consecutive(first_row_value, cell, consecutive)
        if consecutive:
            WINNER = 'USER ' + first_row_value.upper() + ' IS THE WINNER!'
            return True
    return False


def is_column_win(board):
    #look for X or O occupying any single column
    board = [[board[ROW_1_INDEX][COL_1_INDEX], board[ROW_1_INDEX][COL_2_INDEX], board[ROW_1_INDEX][COL_3_INDEX]], [board[ROW_2_INDEX][COL_1_INDEX], board[ROW_2_INDEX][COL_2_INDEX], board[ROW_2_INDEX][COL_3_INDEX]], [board[ROW_3_INDEX][COL_1_INDEX], board[ROW_3_INDEX][COL_2_INDEX], board[ROW_3_INDEX][COL_3_INDEX]]]
    consecutive1 = True
    consecutive2 = True
    consecutive3 = True
    first_col1_value = ''
    first_col2_value = ''
    first_col3_value = ''
    col1_index = 0
    col2_index = 1
    col3_index = 2
    global WINNER
    
    for row in board:
        first_col1_value, consecutive1 = is_consecutive(first_col1_value, row[col1_index], consecutive1)
        first_col2_value, consecutive2 = is_consecutive(first_col2_value, row[col2_index], consecutive2)
        first_col3_value, consecutive3 = is_consecutive(first_col3_value, row[col3_index], consecutive3)
    
    if consecutive1:
        WINNER = 'USER ' + first_col1_value.upper() + ' IS THE WINNER!'
        return True
    if consecutive2:
        WINNER = 'USER ' + first_col2_value.upper() + ' IS THE WINNER!'
        return True
    if consecutive3:
        WINNER = 'USER ' + first_col3_value.upper() + ' IS THE WINNER!'
        return True
    return False


def print_board(board):
    print '-----\n'
    result = ''
    for row in board:
        for cell in row:
            result = result + cell
        result = result + '\n'
    print result
    print '-----'

tic_tac_toe()