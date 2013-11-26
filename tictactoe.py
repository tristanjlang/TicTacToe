##############
# PSEUDOCODE #
##############

# [  A B C]
# [1      ]
# [2      ]
# [3      ]

# 1. set board equal to the following, and print:
# [[  A B C], [       ], [1      ], [2      ], [3      ]]

# 2. prompt user1 for input regarding the row he wants to enter an X/O into
#       >> http://stackoverflow.com/questions/70797/python-and-user-input
# 3. prompt user1 for input regarding the col he wants to enter an X/O into
# 4. update board and print
# 5. check diagonal, row, and column for three consecutive X/O's to declare win
# 6. check for full board to declare tie
# 7. repeat steps 2-6 for input from user2
# 8. repeat steps 2-7 until board is full or winner is declared

####################################

def tic_tac_toe():
    #initialize board
    board = [[  A B C], [       ], [1      ], [2      ], [3      ]]
    
    #loop through users...get row and col for user's input

def check_full_board(board):
    #look for tie

def check_diagonal_win(board):
    #look for X or O occupying either diagonal
    
def check_row_win(board):
    #look for X or O occupying any single row

def check_column_win(board):
    #look for X or O occupying any single column
    
