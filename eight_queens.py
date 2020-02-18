import random 

def init_board(rowMax=8, colMax=8):
    """
    returns blank board
    """
    board={}
    for i in range(0,rowMax):
        board[i]={}
        for j in range(0,colMax):
            board[i][j]=False
    return board

def to_board(configStr):
    """
    turns string into board with queens on it
    """
    board =  init_board()
    for i in range(0,8):
        board[int(configStr[i])][i] = True
    return board

def random_config(colMax=8):
    """
    makes random config string
    """
    config=''
    for _ in range (0, colMax):
        config = config + str(random.randint(0,7))
    return config

def attacking_queens(board, rowMax=8, colMax=8):
    """
    return number of mutually attacking queens.
    for each qeens find how many attacking, sume, divide by 2
    return
    """
    sum= 0
    for i in range(0,rowMax):
        for j in range(0,colMax):
            if board[i][j]:
                sum += attacked_by(i, j, board)
    return sum

def attacked_by(row, col, board, rowMax=8, colMax=8):
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
    if rowIndex < 0:
        rowIndex=row
        colIndex=col
    while(rowIndex < rowMax and colIndex < colMax):
        if board[rowIndex][colIndex]:
            attackingQueens += 1
        rowIndex +=1
        colIndex +=1
    attackingQueens -=1
     
    rowIndex = row + col
    colIndex = 0
    if rowIndex >= rowMax:
        rowIndex=row
        colIndex=col
    while(rowIndex >= 0 and colIndex < colMax-1):
        if board[rowIndex][colIndex]:
            attackingQueens += 1
        rowIndex -= 1
        colIndex += 1
    attackingQueens -= 1

    return attackingQueens

def fitness(config):
    """
    28 non attacking queens is solution
    """
    return 28 - attacking_queens(to_board(config))

def selection_probability(fitness, totalFitness):
    return fitness/totalFitness

def crossover(parent1, parent2, crossOverPoint=random.randint(0,7), maxCol=8):
    child=''
    for i in range(0, crossOverPoint):
        child=child + parent1[i]

    for i in range(crossOverPoint, maxCol):
        child=child + parent2[i]
    return child

def mutation(config, mutationPoint=random.randint(0,7),
mutation=random.randint(0,7), maxCol=8):
    """
    call mutation randomly outside of function for testing purposes
    """
    mutatedConfig=''

    for i in range(0, mutationPoint):
        mutatedConfig=mutatedConfig + config[i]
    
    mutatedConfig =  mutatedConfig + mutation

    for i in range(mutationPoint+1, maxCol):
        mutatedConfig=mutatedConfig + config[i]
    return mutatedConfig

def fill_lottery(population):
    totalFitness=0
    population= population.keys()
    lottery=[]

    for indv in population:
        #fitnessScore = population[indv]['FITNESS']
        fitness = fitness(config)
        for _ in range(0, fitness):
            lottery.append(indv)
    return lottery