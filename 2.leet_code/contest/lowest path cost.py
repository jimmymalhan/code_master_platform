lowest_path_cost = float('inf')
path_costs = [1, 100, 2000000000000, 50]
for path in path_costs:
    if path < lowest_path_cost:
        lowest_path_cost = path

print(lowest_path_cost)