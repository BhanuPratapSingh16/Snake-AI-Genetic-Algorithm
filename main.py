from genetic_algorithm import *
from simulate import *
from model import *

POP_SIZE = 5000
GENERATIONS = 30
INDIVIDUAL_SIZE = 24 * 18 + 18 * 18 + 54
np.random.seed(42)
last_gen, population, fitness_scores = load_last_generation()
if last_gen is not None:
    start_gen = last_gen + 1
else:
    start_gen = 0
    population = [np.random.uniform(-1, 1, INDIVIDUAL_SIZE) for _ in range(POP_SIZE)]


for gen in range(GENERATIONS):
    scores = []
    fitness_scores = []
    print(f"Generation : {gen+start_gen}")
    for i, individual in enumerate(population):
        fitness, score = simulate(individual)
        fitness_scores.append(fitness)
        scores.append(score)
        if i% 100 == 0:
            print(i," : ",fitness)
    print(sum(fitness_scores)/POP_SIZE)

    if (gen + start_gen) % 5 == 0:
        save_generation(start_gen + gen, population.copy(), fitness_scores.copy())
    
    best_fitness_ind = np.argmax(fitness_scores)
    print("Best fitness : ", fitness_scores[best_fitness_ind], "Score : ", scores[best_fitness_ind])
    best_individual = population[best_fitness_ind]
    visualize(best_individual.copy())

    population = evolve_population(population, np.array(fitness_scores))

