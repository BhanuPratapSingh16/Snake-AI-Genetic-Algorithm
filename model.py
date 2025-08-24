import json
import os
import numpy as np

def save_generation(gen, population, fitness_scores, folder="gen_logs"):
    os.makedirs(folder, exist_ok=True)

    for i, pop in enumerate(population):
        population[i] = pop.tolist()

    data = {
        "generation": gen,
        "population": population,
        "fitness": fitness_scores
    }

    filename = f"{folder}/gen_{gen}.json"
    with open(filename, "w") as f:
        json.dump(data, f)

    print(f"Saved generation {gen} -> {filename}")

def load_last_generation(folder="gen_logs"):
    if not os.path.exists(folder):
        return None, None, None

    files = [f for f in os.listdir(folder) if f.startswith("gen_")]
    if not files:
        return None, None, None

    last_gen = 0
    for file in files:
        last_gen = max(last_gen, int(file[file.index("_")+1:file.index(".json")]))

    filename = f"{folder}/gen_{last_gen}.json"
    with open(filename, "r") as f:
        data = json.load(f)

    population = data["population"]
    for i, pop in enumerate(population):
        population[i] = np.array(pop)
    fitness_scores = data["fitness"]

    return last_gen, population, fitness_scores
