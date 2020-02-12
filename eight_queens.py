def init_board(board, rowMax=8, colMax=9):
    for i in range(0,rowMax):
        board[i]={}
        for j in range(0,colMax):
            board[i][j]=None

def attacking_queens(board):
    """
    return number of mutually attacking queens.
    for each qeens find how many attacking, sume, divide by 2
    return
    """
    pass

def attacks(row, col, board):
    colMax=8
    rowMax=8
    attackingQueens=0

    #check rest of row
    for i in range(0, col):
        if board[row][i]:
            attackingQueens +=1
    for i in range(col+1, colMax):
        if board[row][i]:
            attackingQueens +=1

    #check rest of column
    for i in range(0, row):
        if board[i][col]:
            attackingQueens +=1
    for i in range(row+1, rowMax):
        if board[i][col]:
            attackingQueens +=1

    #check diagnols

    return attackingQueens
