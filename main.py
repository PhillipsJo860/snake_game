import pygame, sys, random
from pygame.locals import *

# Initialize pyagame and sound stuff
pygame.init()
pygame.mixer.init()

# Game variables and constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = 'Snake Game'
FPS = 10
BG = (255, 200, 150)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BODY_INNER = (50, 175, 25)
BODY_OUTER = (100, 100, 200)
APPLE_COLOR = (255, 0 ,0)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)


CELL_SIZE = 10

update_snake = 0


snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # Head of snake
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE]) # Body segment
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 2])
snake_pos.append([int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * 3])

def draw_snake(screen, snake_pos):
    index = 0
    for segment in snake_pos:
        pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        if index == 0:
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else:
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        
        index += 1

def draw_apple(screen, apple_pos):
    pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))

def draw_score (screen, score, font):
    score_text = font.render(f'SCore: {score}', True, BLACK)
    screen.blit(score_text, [10, 10])

def run_snake_game():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock()

    direction = 1 # 1 is up, 2 is right, 3 is down, 4 is left
    score = 0
    snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]]
    snake_pos.extend([[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * i] for i in range(1, 4)])
    apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
    
    font = pygame.font.SysFont(None, 25)

    try:
        pygame.mixer.music.load('bg_music.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f'Error loading or playing music: {e}')
    
    running_game = True
    while running_game:
        screen.fill(BG)
        draw_apple(screen, apple_pos)
        draw_score(screen, score, font)
        draw_snake(screen, snake_pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.KEYDOWN:
                new_direction = direction
                if event.key == pygame.K_UP and direction != 3: # Up
                    new_direction = 1
                elif event.key == pygame.K_RIGHT and direction != 4: # RIGHT
                    new_direction = 2
                elif event.key == pygame.K_DOWN and direction != 1: # Down
                    new_direction = 3
                elif event.key == pygame.K_LEFT and direction != 2: #Left
                    new_direction = 4
                direction = new_direction
        
        head_x, head_y = snake_pos[0]
        if direction == 1:
            head_y -= CELL_SIZE
        elif direction == 2:
            head_x += CELL_SIZE
        elif direction == 3:
            head_y += CELL_SIZE
        elif direction == 4:
            head_x -= CELL_SIZE
        
        snake_pos.insert(0, [head_x, head_y])

        if snake_pos[0] == apple_pos:
            while apple_pos in snake_pos:
                apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE, random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]
                score += 1
        else:
            snake_pos.pop()
            
        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y  < 0 or head_y >= SCREEN_HEIGHT or snake_pos[0] in snake_pos[1:]:
            running_game = False

        pygame.display.flip()
        clock.tick(FPS)
    pygame.mixer.music.stop()

def main_menu():
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Main Menu')
    font = pygame.font.SysFont('Arial', 40)


running = True
while running:
    draw_screen()
    

    # Loop through events
    

    if update_snake > 99:
        update_snake = 0
    
        # Move the snake
        head_x, head_y = snake_pos[0]

        
        
        # Update the snake's Position
        snake_pos.insert(0, [head_x, head_y]) # Add a new head
        snake_pos.pop() # Remove the last segment

        # Apple collision check
        
        
        # Collision check with screen boundaries
        
        
    # Draw the snake
    for i in range(len(snake_pos)):
        segment = snake_pos[i]
        if i == 0: # The head
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        else: # The body
            pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
        
    
    

    update_snake += 1


pygame.quit()
sys.exit()