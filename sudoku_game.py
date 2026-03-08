import pygame
import sys

pygame.init()

WIDTH = 540
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Game")

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 30)

# Example puzzle (0 = empty)
board = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],

    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],

    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]

selected = None

def draw_grid():
    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(screen, (0,0,0), (0, i*60), (540, i*60), thickness)
        pygame.draw.line(screen, (0,0,0), (i*60, 0), (i*60, 540), thickness)

def draw_numbers():
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                text = font.render(str(board[row][col]), True, (0,0,0))
                screen.blit(text, (col*60 + 20, row*60 + 10))

def is_valid(num, pos):
    row, col = pos

    # Check row
    for i in range(9):
        if board[row][i] == num and i != col:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    # Check box
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            selected = (y // 60, x // 60)

        if event.type == pygame.KEYDOWN and selected:
            row, col = selected
            if board[row][col] == 0:
                if event.unicode.isdigit():
                    num = int(event.unicode)
                    if 1 <= num <= 9:
                        if is_valid(num, (row, col)):
                            board[row][col] = num

    if selected:
        pygame.draw.rect(screen, (200,200,255),
                         (selected[1]*60, selected[0]*60, 60, 60))

    draw_numbers()
    draw_grid()

    pygame.display.flip()

pygame.quit()
sys.exit()
