import pygame
import sys
import subprocess

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 790
SCREEN_HEIGHT = 680
TILE_SIZE = 50                                                                                              

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images
wall_image = pygame.image.load("wall.png")
player_image = pygame.image.load("girl.png")
goal_image = pygame.image.load("door.png")
enemy_image = pygame.image.load("enime.png")

# Load music
pygame.mixer.music.load("red.mp3")

# Set up screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Game")

# Set up clock
clock = pygame.time.Clock()

# Define the maze
maze = [
    "WWWWWWWWWWWWWWWWWWWW",
    "W                  W",
    "W  WWW WWW WWWW    W",
    "W  W   W   W   W   W",
    "W  W W W WWW WWW W W",
    "W  W W W       W W W",
    "W  WWW WWWWWWW WWW W",
    "W                  W",
    "W WWW W WWWWWWWWW  W",
    "W W   W   W   W W  W",
    "W WWW WWW W W W WWWW",
    "W       W W W W W  W",
    "W WWWWWWW WWWWW WWWW",
    "W   W   W   W   W  W",
    "W WWW WWWWWWWWWWW  W",
    "W                  W",
    "WWWWWWWWWWWWWWWWWWWW"
]

# Define the player
player_pos = [1, 1]

# Define the goal
goal_pos = [18, 15]

# Define the enemy
enemy_pos = [10, 10]
enemy_speed = 0.08  # Slower enemy speed

# Function to draw the maze
def draw_maze():
    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col == "W":
                screen.blit(wall_image, (x * 40, y * 40))

# Function to draw the player
def draw_player():
    screen.blit(player_image, (player_pos[0] * 40, player_pos[1] * 40))

# Function to draw the goal
def draw_goal():
    screen.blit(goal_image, (goal_pos[0] * 40, goal_pos[1] * 40))

# Function to draw the enemy
def draw_enemy():
    screen.blit(enemy_image, (enemy_pos[0] * 40, enemy_pos[1] * 40))

# Function to move the enemy
def move_enemy():
    dx = dy = 0
    if enemy_pos[0] < player_pos[0]:
        dx = enemy_speed
    elif enemy_pos[0] > player_pos[0]:
        dx = -enemy_speed
    if enemy_pos[1] < player_pos[1]:
        dy = enemy_speed
    elif enemy_pos[1] > player_pos[1]:
        dy = -enemy_speed

    # Check for wall collision
    if maze[int(enemy_pos[1] + dy)][int(enemy_pos[0])] != "W":
        enemy_pos[1] += dy
    if maze[int(enemy_pos[1])][int(enemy_pos[0] + dx)] != "W":
        enemy_pos[0] += dx

# Function to show the game over screen
def game_over():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 55)
    text = font.render("Game Over!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Buttons to connect to other Python programs
    button1 = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
    button3 = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 110, 200, 50)
    pygame.draw.rect(screen, WHITE, button1)
    pygame.draw.rect(screen, WHITE, button3)
    font = pygame.font.SysFont(None, 35)
    text1 = font.render("Retry", True, BLACK)
    text3 = font.render("Exit", True, BLACK)
    screen.blit(text1, (button1.x + 10, button1.y + 10))
    screen.blit(text3, (button3.x + 10, button3.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(["python", "set3.py"])
                    sys.exit()
                elif button3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Function to show the victory screen
def victory():
    screen.fill(BLACK)
    font = pygame.font.SysFont(None, 55)
    text = font.render("You Win!", True, WHITE)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

    # Buttons to connect to other Python programs
    button2 = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 50)
    button3 = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 110, 200, 50)
    pygame.draw.rect(screen, WHITE, button2)
    pygame.draw.rect(screen, WHITE, button3)
    font = pygame.font.SysFont(None, 35)
    text2 = font.render("Restart", True, BLACK)
    text3 = font.render("Exit", True, BLACK)
    screen.blit(text2, (button2.x + 10, button2.y + 10))
    screen.blit(text3, (button3.x + 10, button3.y + 10))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button2.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(["python", "set3.py"])
                    sys.exit()
                elif button3.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

# Start the background music
pygame.mixer.music.play(-1)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and maze[player_pos[1]][player_pos[0] - 1] != "W":
                player_pos[0] -= 1
            elif event.key == pygame.K_RIGHT and maze[player_pos[1]][player_pos[0] + 1] != "W":
                player_pos[0] += 1
            elif event.key == pygame.K_UP and maze[player_pos[1] - 1][player_pos[0]] != "W":
                player_pos[1] -= 1
            elif event.key == pygame.K_DOWN and maze[player_pos[1] + 1][player_pos[0]] != "W":
                player_pos[1] += 1

    # Move the enemy
    move_enemy()

    # Check for collision with enemy
    if round(player_pos[0]) == round(enemy_pos[0]) and round(player_pos[1]) == round(enemy_pos[1]):
        game_over()
        running = False

    # Check for reaching the goal
    if player_pos == goal_pos:
        victory()
        running = False

    # Draw everything
    screen.fill(BLACK)
    draw_maze()
    draw_player()
    draw_goal()
    draw_enemy()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()