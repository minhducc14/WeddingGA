import random

from fitness import calculate_fitness


def create_individual(
        num_guests,
        num_tables):

    chromosome = []

    for _ in range(num_guests):

        chromosome.append(
            random.randint(
                1,
                num_tables
            )
        )

    return chromosome


def create_population(
        population_size,
        num_guests,
        num_tables):

    population = []

    for _ in range(
            population_size):

        population.append(
            create_individual(
                num_guests,
                num_tables
            )
        )

    return population


def selection(
        population,
        relation_matrix):

    tournament = random.sample(
        population,
        min(
            3,
            len(population)
        )
    )

    return max(
        tournament,
        key=lambda x:
        calculate_fitness(
            x,
            relation_matrix
        )
    )


def crossover(
        parent1,
        parent2):

    if len(parent1) < 2:

        return parent1.copy()

    point = random.randint(
        1,
        len(parent1) - 1
    )

    child = (
        parent1[:point]
        + parent2[point:]
    )

    return child


def mutation(
        chromosome,
        num_tables):

    child = chromosome.copy()

    position = random.randint(
        0,
        len(child) - 1
    )

    child[position] = random.randint(
        1,
        num_tables
    )

    return child


def elitism(
        population,
        relation_matrix,
        elite_size=2):

    sorted_population = sorted(
        population,
        key=lambda x:
        calculate_fitness(
            x,
            relation_matrix
        ),
        reverse=True
    )

    return sorted_population[
        :elite_size
    ]


def get_best_solution(
        population,
        relation_matrix):

    best = max(
        population,
        key=lambda x:
        calculate_fitness(
            x,
            relation_matrix
        )
    )

    score = calculate_fitness(
        best,
        relation_matrix
    )

    return best, score


def run_ga(
        relation_matrix,
        num_guests,
        num_tables,
        population_size=100,
        generations=300,
        mutation_rate=0.1):

    population = create_population(
        population_size,
        num_guests,
        num_tables
    )

    best_solution = None

    best_fitness = -1

    fitness_history = []

    for generation in range(
            generations):

        new_population = elitism(
            population,
            relation_matrix
        )

        while len(
                new_population
        ) < population_size:

            parent1 = selection(
                population,
                relation_matrix
            )

            parent2 = selection(
                population,
                relation_matrix
            )

            child = crossover(
                parent1,
                parent2
            )

            if (
                random.random()
                < mutation_rate
            ):

                child = mutation(
                    child,
                    num_tables
                )

            new_population.append(
                child
            )

        population = new_population

        current_best, current_score = \
            get_best_solution(
                population,
                relation_matrix
            )

        if (
            current_score
            > best_fitness
        ):

            best_fitness = current_score

            best_solution = (
                current_best.copy()
            )

        fitness_history.append(
            best_fitness
        )

        print(
            f"Generation "
            f"{generation + 1} "
            f"| Fitness = "
            f"{best_fitness}"
        )

    return (
        best_solution,
        best_fitness,
        fitness_history
    )