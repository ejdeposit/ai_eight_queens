import eight_queens as qu
import random
import csv
import matplotlib.pyplot as plt
import sys 

population = []
populationFitness = 0
nextGen=[]
points=[]

argLen=len(sys.argv)
if argLen == 1:
    PopulationSize = 100
    NumIterations=1000
    MutationPct = 10
elif argLen == 4:
    PopulationSize = int(sys.argv[1])
    NumIterations = int(sys.argv[2])
    MutationPct = int(sys.argv[3])
else:
    print(
        """
        Not enough arguments.
        Enter Desired PopulationSize, NumIterations, and MutationPct as arguments.  
        To use default arguments enter no arguments. 
        """
    )
    exit(1)

#generate starting population
for i in range(0, PopulationSize):
    config = qu.random_config()
    score = qu.fitness(config) 
    populationFitness += score
    population.append((score, config))

bestSolution=(0,'0')

for gen in range(0, NumIterations):
    population.sort()
    nextGen=[]
    nextGenFitness=0

    #create next generation
    for i in range(0, PopulationSize):
        #crossover
        #resuse this random number for random mutation likelyhood to save call to rand
        randomFitness1= random.randint(0, populationFitness)
        randomFitness2= random.randint(0, populationFitness)
        parent1 = qu.get_reproducer(population, randomFitness1)
        parent2 = qu.get_reproducer(population, randomFitness2)
        childConfig = qu.cross_over(parent1, parent2)

        #mutation
        randomMutation =  (randomFitness1 + 100)%100
        if randomMutation <  MutationPct:
            childConfig= qu.mutation(childConfig, randomFitness1%8, randomFitness2%8)

        #add to next gen
        child = (qu.fitness(childConfig), childConfig)
        nextGen.append(child)
        nextGenFitness += child[0]

        if child > bestSolution:
            bestSolution = child

    avgFitness= populationFitness/PopulationSize
    point=(gen,avgFitness)
    points.append(point)

    if bestSolution[0] ==  28:
        break

    population = nextGen
    populationFitness= nextGenFitness

if bestSolution[0] != 28:    
    print('No Solution found! Change PopulationSize, NumIterations, and MutationPct arguments or use defaults to find a optimal solution.')
print(f'Best Solution:{bestSolution[1]} Score:{bestSolution[0]}')
solutionBoard=qu.to_board(bestSolution[1])
qu.print_board(solutionBoard)

pointsDict=[{'Generation':point[0] , 'Fitness':point[1]} for point in points]

with open('graph.csv', 'wt') as fout:
    cout = csv.DictWriter(fout, ['Generation', 'Fitness'])
    cout.writeheader()
    cout.writerows(pointsDict)

plt.plot([point[0] for point in points], [point[1] for point in points], 'ro')
plt.ylabel('Average Fitness')
plt.xlabel('Generation')
plt.show()
