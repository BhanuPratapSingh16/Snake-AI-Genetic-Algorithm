import numpy as np
import random


def select_parent(fitness_sum, fitness_scores, population): # Roullete selection
    rand = random.uniform(0, fitness_sum)
    sum = 0
    for i, score in enumerate(fitness_scores):
        sum += score
        if sum >= rand:
            return population[i]

def evolve_population(population, fitness_scores):
    POP_SIZE = len(population)
    fitness_sum = np.sum(fitness_scores)

    sorted_indices = np.argsort(-fitness_scores)
    sorted_pop = [population[i] for i in sorted_indices]
    next_generation = []
    
    for i in range(int(1 / 100 * POP_SIZE)):
        next_generation.append(sorted_pop[i])
        next_generation.append(mutate(sorted_pop[i].copy()))
    
    while len(next_generation) != POP_SIZE:
        parent1, parent2 = select_parent(fitness_sum, fitness_scores, population), select_parent(fitness_sum, fitness_scores, population)
        child = crossover(parent1, parent2, len(parent1))
        child = mutate(child)
        next_generation.append(child)

    return next_generation

def crossover(parent1, parent2, individual_size):
    # Random one point crossover
    point = random.randint(0, individual_size)
    child = np.empty(individual_size)
    for i in range(individual_size):
        if i<=point:
            child[i] = parent1[i]
        else:
            child[i] = parent2[i]
    return child

def mutate(individual, mutation_rate=0.15):
    for i in range(len(individual)):
        if random.uniform(0, 1) < mutation_rate:
            individual[i] += random.uniform(-1, 1)
            if individual[i] > 1:
                individual[i] = 1
            elif individual[i] < -1:
                individual[i] = -1
    return individual
