import pygame

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
ERASER_SIZE = 40
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

# Create grid
rows = HEIGHT // CELL_SIZE
cols = WIDTH // CELL_SIZE

grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

def draw_grid():
    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col], 
                             (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def erase(x, y):
    for row in range(rows):
        for col in range(cols):
            cell_x = col * CELL_SIZE
            cell_y = row * CELL_SIZE
            if (x < cell_x + CELL_SIZE and x + ERASER_SIZE > cell_x and
                y < cell_y + CELL_SIZE and y + ERASER_SIZE > cell_y):
                grid[row][col] = WHITE

def main():
    running = True
    erasing = False
    
    while running:
        screen.fill(WHITE)
        draw_grid()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                erasing = True
            if event.type == pygame.MOUSEBUTTONUP:
                erasing = False
        
        if erasing:
            x, y = pygame.mouse.get_pos()
            erase(x, y)
            pygame.draw.rect(screen, WHITE, (x, y, ERASER_SIZE, ERASER_SIZE))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
