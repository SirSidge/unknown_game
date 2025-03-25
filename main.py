import pygame
from src.get_random import *
from src.constants import player_speed, player_diagonal_speed, star_count

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0

screen_width = screen.get_width()
screen_height = screen.get_height()
player_pos = pygame.Vector2(screen_width / 2, screen_height / 2)
star_pos = []
border = [screen_height, 0, 0, screen_width] #[top, bottom, left, right]

for i in range(star_count):
        star_pos.append((get_random(0, screen_width), get_random(0, screen_height)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("#210541")

    #Render game here
    
    for star in star_pos:
        pygame.draw.circle(screen, "white", star, 4)
    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        running = False

    # Calculate movement direction
    dx = 0
    dy = 0

    # Horizontal movement
    if keys[pygame.K_a]:
        dx -= player_speed
    elif keys[pygame.K_d]:
        dx += player_speed

    # Vertical movement
    if keys[pygame.K_w]:
        dy -= player_speed
    elif keys[pygame.K_s]:
        dy += player_speed

    # Adjust speed for diagonal movement
    if dx != 0 and dy != 0:
        speed = player_diagonal_speed
    else:
        speed = player_speed

    # Apply movement
    player_pos.x += dx * dt * (speed / player_speed)
    player_pos.y += dy * dt * (speed / player_speed)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

