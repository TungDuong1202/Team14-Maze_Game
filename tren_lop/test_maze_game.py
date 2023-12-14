import pygame
import random

# Kích thước cửa sổ
WIDTH, HEIGHT = 600, 600
WALL = 0
EMPTY = 1
# Kích thước lưới
ROWS, COLS = 15 , 15 
CELL_SIZE = WIDTH // ROWS

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#Tạo mê cung bằng thuật toán Recursive Backtracking
def recursive_backtracking(maze, x, y):
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy   
        if 0 <= new_x < COLS and 0 <= new_y < ROWS and maze[new_y][new_x] == WALL:
            maze[y + dy // 2][x + dx // 2] = EMPTY
            maze[new_y][new_x] = EMPTY
            recursive_backtracking(maze, new_x, new_y)

# Tạo mê cung
def create_maze():
    maze = [[WALL for _ in range(COLS)] for _ in range(ROWS)]
    maze[0][0] = EMPTY
    recursive_backtracking(maze, 0, 0)
    return maze

# Vẽ mê cung lên cửa sổ
def draw_maze(screen, maze):
    for row in range(ROWS):
        for col in range(COLS):
            color = BLACK if maze[row][col] == 0 else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Hàm chính của trò chơi
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Maze Game')
    clock = pygame.time.Clock()

    maze = create_maze()
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if start[1] > 0:  
                        start = (start[0], start[1] - 1)
                elif event.key == pygame.K_DOWN:
                    if start[1] < ROWS - 1:
                        start = (start[0], start[1] + 1)
                elif event.key == pygame.K_LEFT:
                    if start[0] > 0:  
                        start = (start[0] - 1, start[1])
                elif event.key == pygame.K_RIGHT:
                    if start[0] < COLS - 1:
                        start = (start[0] + 1, start[1])

        screen.fill(BLACK)
        draw_maze(screen, maze)
        pygame.draw.rect(screen, GREEN, (start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()


main()
