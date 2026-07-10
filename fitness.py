from itertools import combinations


def calculate_fitness(
        chromosome,
        relation_matrix):

    fitness = 0

    tables = {}

    for guest_index, table_id in enumerate(chromosome):

        if table_id not in tables:
            tables[table_id] = []

        tables[table_id].append(
            guest_index
        )

    for members in tables.values():

        for i, j in combinations(
                members,
                2):

            fitness += relation_matrix[i][j]

    return fitness


def get_table_scores(
        chromosome,
        relation_matrix):

    result = {}

    tables = {}

    for guest_index, table_id in enumerate(chromosome):

        if table_id not in tables:
            tables[table_id] = []

        tables[table_id].append(
            guest_index
        )

    for table_id, members in tables.items():

        score = 0

        for i, j in combinations(
                members,
                2):

            score += relation_matrix[i][j]

        result[table_id] = score

    return result


def get_total_relationships(
        relation_matrix):

    total = 0

    n = len(relation_matrix)

    for i in range(n):

        for j in range(i + 1, n):

            total += relation_matrix[i][j]

    return total


def decode_solution(
        chromosome,
        guest_names):

    tables = {}

    for guest_index, table_id in enumerate(chromosome):

        if table_id not in tables:
            tables[table_id] = []

        tables[table_id].append(
            guest_names[guest_index]
        )

    return tables

if __name__ == "__main__":

    matrix = [
        [0, 100, 500],
        [100, 0, 300],
        [500, 300, 0]
    ]

    chromosome = [1, 1, 2]

    print(
        calculate_fitness(
            chromosome,
            matrix
        )
    )