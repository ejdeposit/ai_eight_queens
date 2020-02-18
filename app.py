import eight_queens as qu
import random

k = 50
population = {}
populationFitness = 0
lottery=[]

for i in range(0, k):
    #population[i] = {}
    #population[i]['CONFIG'] = qu.random_config()
    population[i] = qu.random_config()

#for i in range(0, k):
#    config = population[i]['CONFIG']
#    fitness = qu.fitness(config)
#    population[i]['FITNESS']=fitness
#    populationFitness += fitness

lottery = qu.fill_lottery(population)
random.shuffle(lottery)
for i in range(0, k):
    parent1=lottery[0]
    parent2=lottery[1]