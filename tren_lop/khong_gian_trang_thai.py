from collections import deque

def is_goal(state):
    goal_state = [[1, 4, 2], [3, 7, 5], [6, 0, 7]]
    return state == goal_state

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def move(state, direction):
    i, j = find_zero(state)
    new_state = [row.copy() for row in state]

    if direction == 'up' and i > 0:
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif direction == 'down' and i < 2:
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif direction == 'left' and j > 0:
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif direction == 'right' and j < 2:
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

    return new_state

def print_state(state):
    for row in state:
        print(row)
    print()

def solve_puzzle(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])
    i = 1
    while queue:
        current_state, path = queue.popleft()

        if is_goal(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))
        print('Khong gian trang thai',i,':')
        for direction in ['up', 'down', 'left', 'right']:
            new_state = move(current_state, direction)
            print(direction,':')
            print_state(new_state)
            if tuple(map(tuple, new_state)) not in visited:
                queue.append((new_state, path + [direction]))
        i = i + 1

    return None


state = [[1, 0, 2], [3, 4, 5], [6, 7, 7]]
solution = solve_puzzle(state)

if solution:
    print("Duong di tim duoc:")
    for step in solution:
        print(step)
else:
    print("Khong tim thay duong di.")