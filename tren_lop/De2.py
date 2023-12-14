import heapq

def astar_search(start, goal, graph, heuristic):
    open_list = [(0, start)]
    heapq.heapify(open_list)
    came_from = {}
    g_score = {start: 0}

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            total_cost = g_score[current_node]
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, total_cost

        for neighbor, cost in graph[current_node].items():
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None, None

# Example graph represented as an adjacency list
# Each node has its neighbors and corresponding costs
graph = {
    'S': {'A': 3, 'B': 2, 'C': 5},
    'A': {'C': 3, 'G': 2},
    'B': {'A': 5, 'D': 6},
    'C': {'B': 4, 'H': 3},
    'D': {'E': 2, 'F': 3},
    'E': {'F': 5},
    'F': {},
    'G': {'E': 5, 'D': 4},
    'H': {'A': 4, 'D': 4}
}

# Heuristic values for each node (Manhattan distance to the goal)
heuristic_values = {
    'S': 10,
    'A': 8,
    'B': 9,
    'C': 7,
    'D': 4,
    'E': 3,
    'F': 0,
    'G': 6,
    'H': 6
}

# Define the desired path 'S-A-C-B-D-E-F'
desired_path = ['S', 'A', 'C', 'B', 'D', 'E', 'F']
current_node = 'S'

# Loop through the desired path and calculate the total cost
total_cost = 0
for next_node in desired_path[1:]:
    if next_node not in graph[current_node]:
        print("Path not found")
        break
    total_cost += graph[current_node][next_node]
    current_node = next_node

if current_node == 'F':
    print("Desired path:", desired_path)
    print("Total cost:", total_cost)
else:
    print("Desired path not found in the graph")
