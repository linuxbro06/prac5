import random

distance = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

def total_distance(tour):
    cost = 0
    for i in range(len(tour)):
        cost += distance[tour[i-1]][tour[i]]
    return cost

def get_neighbor(current):
    neighbor = current[:]
    i = random.randrange(len(neighbor))
    j = random.randrange(len(neighbor))
    while j == i:
        j = random.randrange(len(neighbor))
    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
    return neighbor

def swap_two_cities(tour):
    new_tour = tour[:]
    i, j = random.sample(range(len(new_tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

def hill_climb(iterations=1000):
    current = list(range(len(distance)))
    random.shuffle(current)
    current_cost = total_distance(current)
    best = current[:]
    best_cost = current_cost
    for _ in range(iterations):
        neighbor = get_neighbor(current)
        neighbor_cost = total_distance(neighbor)
        if neighbor_cost < current_cost:
            current, current_cost = neighbor, neighbor_cost
            if current_cost < best_cost:
                best, best_cost = current[:], current_cost
    return best, best_cost

if __name__ == "__main__":
    random.seed()
    start_tour = list(range(len(distance)))
    random.shuffle(start_tour)
    start_cost = total_distance(start_tour)
    print("Starting tour:", start_tour, "Cost:", start_cost)
    best_tour, best_cost = hill_climb(1000)
    print("Best tour found:", best_tour, "Cost:", best_cost)

