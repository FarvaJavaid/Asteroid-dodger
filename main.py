import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroid Dodger")

# Colors
WHITE = (255, 255, 255)
RED = (255, 80, 80)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 70
player_speed = 7

# Asteroids
asteroid_size = 50
asteroids = []
asteroid_speed = 6

# Score
score = 0
font = pygame.font.SysFont("arial", 32)

def draw_player(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, player_size, player_size))

def draw_asteroid(x, y):
    pygame.draw.rect(screen, RED, (x, y, asteroid_size, asteroid_size))

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - 100, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Spawn asteroids
    if random.randint(1, 30) == 1:
        x_pos = random.randint(0, WIDTH - asteroid_size)
        asteroids.append([x_pos, 0])

    # Move asteroids
    for asteroid in asteroids[:]:
        asteroid[1] += asteroid_speed
        draw_asteroid(asteroid[0], asteroid[1])

        # Collision
        if (
            player_x < asteroid[0] + asteroid_size and
            player_x + player_size > asteroid[0] and
            player_y < asteroid[1] + asteroid_size and
            player_y + player_size > asteroid[1]
        ):
            game_over()

        # Remove asteroid
        if asteroid[1] > HEIGHT:
            asteroids.remove(asteroid)
            score += 1

    # Draw player & score
    draw_player(player_x, player_y)
    show_score(score)

    pygame.display.update()

pygame.quit()
