import pygame
import random
from collections import deque

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 600

# Kích thước lưới
ROWS, COLS = 30, 30
CELL_SIZE = WIDTH // COLS

# Mã số các loại ô trong mê cung
EMPTY = 0
WALL = 1


# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def read_maze_from_file(filename):
    with open(filename, 'r') as file:
        maze = [[int(cell) for cell in line.split()] for line in file]
    return maze

# Chọn vị trí ngẫu nhiên cho start và end
def choose_end(maze,start):        
    possible_positions = [(i, j) for i in range(ROWS) for j in range(COLS) if maze[i][j] == 0 and (i,j) != start]
    end = random.choice(possible_positions)
    return end[1],end[0]

# Vẽ mê cung lên cửa sổ
def draw_maze(screen, maze):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 0 else BLACK
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Hàm kiểm tra xem một điểm có hợp lệ để di chuyển không
def is_valid_move(x, y,maze):
    return 0 <= x < COLS and 0 <= y < ROWS and maze[y][x] == 0

# Tìm đường đi từ start đến end bằng BFS
def BFS(start, end, maze):
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        x, y = current

        if current == end:
            return path + [current]  # Trả về đường đi từ start đến end

        if is_valid_move(x, y,maze) and not visited[x][y]:
            visited[x][y] = True
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                queue.append(((new_x, new_y), path + [current]))

    return None
# Hàm tìm đường đi từ start đến end bằng DFS
def DFS(start, end, maze):
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
    stack = [(start, [])]

    while stack:
        current, path = stack.pop()
        x, y = current

        if current == end:
            return path + [current]  # Trả về đường đi từ start đến end

        if is_valid_move(x, y, maze) and not visited[x][y]:
            visited[x][y] = True
            for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                stack.append(((new_x, new_y), path + [current]))

    return None
# check va cham
def is_wall(x,y,maze):
    return maze[y][x] != WALL

# Hàm chính của trò chơi
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Maze game')
    clock = pygame.time.Clock()

    maze = read_maze_from_file('maze2.txt')
    start = (0,0)
    end = choose_end(maze,start)
    draw_path_BFS = False
    draw_path_DFS = False
    running = True
    font = pygame.font.Font(None, 20)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    draw_path_BFS = not draw_path_BFS
                if event.key == pygame.K_d:
                    draw_path_DFS = not draw_path_DFS
                if event.key == pygame.K_UP:
                    if start[1] > 0 and is_wall(start[0],start[1]-1,maze):  
                        start = (start[0], start[1] - 1)
                elif event.key == pygame.K_DOWN:
                    if start[1] < ROWS - 1 and is_wall(start[0],start[1]+1,maze):
                        start = (start[0], start[1] + 1)
                elif event.key == pygame.K_LEFT:
                    if start[0] > 0 and is_wall(start[0]-1,start[1],maze):  
                        start = (start[0] - 1, start[1])
                elif event.key == pygame.K_RIGHT:
                    if start[0] < COLS - 1 and is_wall(start[0]+1,start[1],maze):
                        start = (start[0] + 1, start[1])
                

        screen.fill(BLACK)
        draw_maze(screen, maze)
        start_x, start_y = start
        end_x, end_y = end
        pygame.draw.rect(screen, GREEN, (start_x * CELL_SIZE, start_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (end_x * CELL_SIZE, end_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        if draw_path_BFS:
            path_BFS = BFS(start,end,maze)
            if path_BFS:
                for x,y in path_BFS:
                    if (x,y) != start and (x,y) != end:
                        pygame.draw.rect(screen,(0,0,225),(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
                # Tính độ dài đường đi BFS và hiển thị lên cửa sổ
                length_BFS = len(path_BFS)
                text_surface_BFS = font.render(f'BFS Path Length: {length_BFS}', True,RED)
                screen.blit(text_surface_BFS, (450, 10))  # Hiển thị văn bản
        if draw_path_DFS:
            path_DFS = DFS(start,end,maze)
            if path_DFS:
                for x,y in path_DFS:
                    if (x,y) != start and (x,y) != end:
                        pygame.draw.rect(screen,(225,165,0),(x*CELL_SIZE,y*CELL_SIZE,CELL_SIZE,CELL_SIZE))
                # Tính độ dài đường đi DFS và hiển thị lên cửa sổ
                length_DFS = len(path_DFS)
                text_surface_DFS = font.render(f'DFS Path Length: {length_DFS}', True, RED)
                screen.blit(text_surface_DFS, (450, 50))  # Hiển thị văn bản
        if start == end:
            end = choose_end(maze,start)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

main()
