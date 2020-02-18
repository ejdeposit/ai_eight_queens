import eight_queens as qu
import random

k = 50
population = []
populationFitness = 0
lottery=[]
nextGeneration=[]

#generate starting population
for i in range(0, k):
    population.append(qu.random_config())

#fill lottery based on fitness score of each individual
lottery = qu.fill_lottery(population)

for i in range(0, k):
    random.shuffle(lottery)
    parent1=lottery[0]
    parent2=lottery[1]