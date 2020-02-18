import eight_queens as qu
import random

k = 10
population = []
populationFitness = 0
lottery=[]
nextGen=[]
solution=''
maxGeneration=200

#generate starting population
for i in range(0, k):
    population.append(qu.random_config())


for _ in range(0, maxGeneration):
    #fill lottery based on fitness score of each individual
    lottery = qu.fill_lottery(population)
    random.shuffle(lottery)

    #create next generation
    for i in range(0, k):
        parent1=lottery[random.randint(0,k-1)]
        parent2=lottery[random.randint(0,k-1)]
        child=qu.cross_over(parent1, parent2)
        nextGen.append(child)

        if qu.fitness(child) == 28:
            solution = child
            break
    
    if solution:
        break

    population = nextGen

if not solution:
    solution = '01234567'
print(child)
print(qu.fitness(child))
solutionBoard=qu.to_board(child)
qu.print_board(solutionBoard)