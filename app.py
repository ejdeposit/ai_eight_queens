import eight_queens as qu
import random

k = 20
maxGeneration=20
population = []
populationFitness = 0
nextGen=[]
solution=''


#generate starting population
for i in range(0, k):
    config = qu.random_config()
    score = qu.fitness(config) 
    populationFitness += score
    population.append((score, config))
    


for gen in range(0, maxGeneration):
    population.sort()
    print(gen)
    nextGen=[]

    #create next generation
    for i in range(0, k):
        parent1 = qu.get_reproducer(population, random.randint(0, populationFitness))
        parent2 = qu.get_reproducer(population, random.randint(0, populationFitness))

        childConfig = qu.cross_over(parent1, parent2)
        child = (qu.fitness(childConfig), childConfig)
        nextGen.append(child)

        if child[0] == 28:
            print('found solution')
            solution = child[1]
            break

    if solution:
        break

    population = nextGen

if not solution:
    solution = '01234567'
print(solution)
print(qu.fitness(solution))
solutionBoard=qu.to_board(solution)
qu.print_board(solutionBoard)