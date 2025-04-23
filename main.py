import pygame, sys, random
from pygame.locals import *

# Initialize pyagame and sound stuff
pygame.init()
pygame.mixer.init()

# Screen constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Snake Game'

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Game variables and constants
CELL_SIZE = 10
direction = 1 # 1 is up, 2 is right, 3 is down, 4 is left
update_snake = 0
score = 0

snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # Head of snake
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE]) # Body segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3])

BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (255, 0 ,0)

# Define apple position
apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

# Font for score
font = pygame.font.SysFont(None, 25)

# Load and play music
pygame.mixer.music.load('bg_music.mp3')

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play(-1)

def draw_screen():
    screen.fill(BG)

def draw_apple():
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score ():
    score_text = font.render(f'SCore: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

running = True
while running:
    draw_screen()
    draw_apple()
    draw_score()

    # Loop through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3: # Up
                direction = 1
            elif event.key == pygame.K_RIGHT and direction != 4: # RIGHT
                direction = 2
            elif event.key == pygame.K_DOWN and direction != 1: # Down
                direction = 3
            elif event.key == pygame.K_LEFT and direction != 2: #Left
                direction = 4

    if update_snake > 99:
        update_snake = 0
    
        # Move the snake
        head_x, head_y = snake_pos[0]

        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y += CELL_SIZE
        elif direction == 4:
            head_x -= CELL_SIZE
        
        # Update the snake's Position
        snake_pos.insert(0, [head_x, head_y]) # Add a new head
        snake_pos.pop() # Remove the last segment

        # Apple collision check
        if snake_pos[0] == apple_pos:
            apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
            snake_pos.append(snake_pos[-1]) # Create a new segment
            score += 1
        
        # Collision check with screen boundaries
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y  < 0 or head_y >= SCREEN_HEIGHT:
            running = False
        
    # Draw the snake
    for i in range(len(snake_pos)):
        segment = snake_pos[i]
        if i == 0: # The head
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else: # The body
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        
    
    pygame.display.flip()

    update_snake += 1


pygame.quit()
sys.exit()