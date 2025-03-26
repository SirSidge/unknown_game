import pygame
from src.get_random import *
from src.constants import star_count, screen_height, screen_width, screen
from src.letters import letter
from src.player import Player

pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0
star_pos = []
border = [screen_height, 0, 0, screen_width] #[top, bottom, left, right]

player = Player()

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
    pygame.draw.circle(screen, player.color, player.pos, player.size)

    pygame.draw.rect(screen, "green", letter)

    keys = pygame.key.get_pressed()
    #To get mouse position
    #pygame.mouse.get_pos()

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        running = False

    # Calculate movement direction
    dx = 0
    dy = 0

    # Horizontal movement
    if keys[pygame.K_a]:
        dx -= player.speed
    elif keys[pygame.K_d]:
        dx += player.speed

    # Vertical movement
    if keys[pygame.K_w]:
        dy -= player.speed
    elif keys[pygame.K_s]:
        dy += player.speed

    # Adjust speed for diagonal movement
    if dx != 0 and dy != 0:
        speed = player.diagonal_speed
    else:
        speed = player.speed

    # Apply movement
    player.pos.x += dx * dt * (speed / player.speed)
    player.pos.y += dy * dt * (speed / player.speed)

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

