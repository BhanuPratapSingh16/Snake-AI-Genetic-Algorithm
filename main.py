from genetic_algorithm import *
from simulate import *

POP_SIZE = 5000
GENERATIONS = 70
INDIVIDUAL_SIZE = 24 * 18 + 18 * 18 + 54
np.random.seed(42)
population = [np.random.uniform(-1, 1, INDIVIDUAL_SIZE) for _ in range(POP_SIZE)]

for gen in range(GENERATIONS):
    fitness_scores = []
    scores = []
    print(f"Generation : {gen}")
    for i, individual in enumerate(population):
        fitness, score = simulate(individual)
        fitness_scores.append(fitness)
        scores.append(score)
        if i% 100 == 0:
            print(i," : ",fitness)
    print(sum(fitness_scores)/POP_SIZE)
    
    best_fitness_ind = np.argmax(fitness_scores)
    print("Best fitness : ", fitness_scores[best_fitness_ind], "Score : ", scores[best_fitness_ind])
    best_individual = population[best_fitness_ind]
    visualize(best_individual.copy())

    population = evolve_population(population, np.array(fitness_scores))