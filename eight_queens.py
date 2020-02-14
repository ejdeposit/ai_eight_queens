def init_board(rowMax=8, colMax=8):
    board={}
    for i in range(0,rowMax):
        board[i]={}
        for j in range(0,colMax):
            board[i][j]=None
    return board

def to_board(configStr):
    board =  init_board()
    for i in range(0,8):
        board[int(configStr[i])][i] = True
    return board

def attacking_queens(board):
    """
    return number of mutually attacking queens.
    for each qeens find how many attacking, sume, divide by 2
    return
    """
    pass

def attacked_by(row, col, board):
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

    #check diaganols
    rowIndex = row - col
    colIndex = 0
    while(rowIndex < rowMax and colIndex < colMax):
        if board[rowIndex][colIndex]:
            attackingQueens += 1
        rowIndex +=1
        colIndex +=1
    attackingQueens -=1

    rowIndex = row + col
    colIndex = 0
    while(rowIndex >= 0 and colIndex < colMax):
        if board[rowIndex][colIndex]:
            attackingQueens += 1
        rowIndex -= 1
        colIndex += 1
    attackingQueens -= 1

    return attackingQueens
