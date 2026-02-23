import pygame
import sys
import subprocess

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 820
TILE_SIZE = 40
FPS = 30
ENEMY_MOVE_DELAY = 10 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Maze layout (1 represents walls, 0 represents paths)
MAZE = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

player_img = pygame.image.load('girl.png')
enemy_img = pygame.image.load('enime.png')
goal_img = pygame.image.load('door.png')
wall_img = pygame.image.load('wall.png')
background_img = pygame.image.load('background.png')
speed_powerup_img = pygame.image.load('boots.png')  # Add your speed power-up image
bow_powerup_img = pygame.image.load('bow.png')  # Add your bow power-up image

# Scale images to fit the tiles
player_img = pygame.transform.scale(player_img, (TILE_SIZE, TILE_SIZE))
enemy_img = pygame.transform.scale(enemy_img, (TILE_SIZE, TILE_SIZE))
goal_img = pygame.transform.scale(goal_img, (TILE_SIZE, TILE_SIZE))
wall_img = pygame.transform.scale(wall_img, (TILE_SIZE, TILE_SIZE))
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
speed_powerup_img = pygame.transform.scale(speed_powerup_img, (TILE_SIZE, TILE_SIZE))
bow_powerup_img = pygame.transform.scale(bow_powerup_img, (TILE_SIZE, TILE_SIZE))

# Player settings
player_start_pos = [1, 1]
player_pos = player_start_pos.copy()
player_speed = 1

# Goal settings
goal_pos = [18, 9]

# Enemy settings
enemies_start_pos = [
    [10, 8],
    [10, 7],
    [12,9],
    [15, 4]
]
enemies = enemies_start_pos.copy()

# Power-up settings
speed_powerup_pos = [5, 5]
#bow_powerup_pos = [14, 14]
#as_bow = False

# Clock
clock = pygame.time.Clock()
enemy_move_counter = 0

def draw_maze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                screen.blit(wall_img, (col * TILE_SIZE, row * TILE_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

def draw_player():
    screen.blit(player_img, (player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE))

def draw_goal():
    screen.blit(goal_img, (goal_pos[0] * TILE_SIZE, goal_pos[1] * TILE_SIZE))

def draw_enemies():
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0] * TILE_SIZE, enemy[1] * TILE_SIZE))

def draw_powerups():
    screen.blit(speed_powerup_img, (speed_powerup_pos[0] * TILE_SIZE, speed_powerup_pos[1] * TILE_SIZE))
    #screen.blit(bow_powerup_img, (bow_powerup_pos[0] * TILE_SIZE, bow_powerup_pos[1] * TILE_SIZE))

def move_player(dx, dy):
    new_x = player_pos[0] + dx * player_speed
    new_y = player_pos[1] + dy * player_speed
    if MAZE[new_y][new_x] == 0:
        player_pos[0] = new_x
        player_pos[1] = new_y

def move_enemy(enemy):
    if player_pos[0] > enemy[0] and MAZE[enemy[1]][enemy[0] + 1] == 0:
        enemy[0] += 1
    elif player_pos[0] < enemy[0] and MAZE[enemy[1]][enemy[0] - 1] == 0:
        enemy[0] -= 1
    if player_pos[1] > enemy[1] and MAZE[enemy[1] + 1][enemy[0]] == 0:
        enemy[1] += 1
    elif player_pos[1] < enemy[1] and MAZE[enemy[1] - 1][enemy[0]] == 0:
        enemy[1] -= 1

def reset_positions():
    global player_pos, enemies, player_speed, has_bow
    player_pos = player_start_pos.copy()
    enemies = enemies_start_pos.copy()
    player_speed = 1
    has_bow = False

def game_over_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 55)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    button_retry = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
    button_exit = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 110, 200, 50)
    pygame.draw.rect(screen, WHITE, button_retry)
    pygame.draw.rect(screen, WHITE, button_exit)
    font = pygame.font.SysFont(None, 35)
    text_retry = font.render("Retry", True, BLACK)
    text_exit = font.render("Exit", True, BLACK)
    screen.blit(text_retry, (button_retry.x + 10, button_retry.y + 10))
    screen.blit(text_exit, (button_exit.x + 10, button_exit.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_retry.collidepoint(event.pos):
                    reset_positions()
                    return
                elif button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

def level_complete_screen():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 55)
    text = font.render("Level Complete!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    button_next = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
    button_exit = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 110, 200, 50)
    pygame.draw.rect(screen, WHITE, button_next)
    pygame.draw.rect(screen, WHITE, button_exit)
    font = pygame.font.SysFont(None, 35)
    text_next = font.render("Next", True, BLACK)
    text_exit = font.render("Exit", True, BLACK)
    screen.blit(text_next, (button_next.x + 10, button_next.y + 10))
    screen.blit(text_exit, (button_exit.x + 10, button_exit.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_next.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(["python", "d3.py"])
                    sys.exit()
                elif button_exit.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                move_player(1, 0)
            elif event.key == pygame.K_UP:
                move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                move_player(0, 1)
    
    # Move enemies at a slower rate
    enemy_move_counter += 1
    if enemy_move_counter >= ENEMY_MOVE_DELAY:
        for enemy in enemies:
            move_enemy(enemy)
        enemy_move_counter = 3
    
    # Check if player reached goal
    if player_pos == goal_pos:
        level_complete_screen()

    # Check if an enemy caught the player
    if player_pos in enemies:
        game_over_screen()

    # Check if player picked up speed power-up
    if player_pos == speed_powerup_pos:
        player_speed = 2
        speed_powerup_pos = [-1, -1]  # Remove the power-up from the maze

    # Check if player picked up bow power-up
   # if player_pos == bow_powerup_pos:
    #    has_bow = True
     #   bow_powerup_pos = [-1, -1]  # Remove the power-up from the maze

    # Draw everything
    screen.blit(background_img, (0, 0))
    draw_maze(MAZE)
    draw_player()
    draw_goal()
    draw_enemies()
    draw_powerups()
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
sys.exit()