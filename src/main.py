import pygame
from get_random import *
from constants import screen_height, screen_width, screen, ALPHABET
from player import Player
from letters import Letter
from ui import UI

pygame.init()
clock = pygame.time.Clock()
running = True
dt = 0

updatable_player = pygame.sprite.Group()
drawable_player = pygame.sprite.Group()
updatable_obj = pygame.sprite.Group()
drawable_obj = pygame.sprite.Group()

Player.containers = (updatable_player, drawable_player)
Letter.containers = (updatable_obj, drawable_obj)
UI.containers = (drawable_player)

player = Player(screen_width / 2, screen_height / 2)
ui = UI(screen_height)

#Letter spawning info
SPAWN_INTERVAL = 1000 # 1sec
last_spawn_time = 0
#letter = Letter("blue")

background = pygame.image.load('./assets/space_wallpaper.png').convert()

def new_letter():
    Letter("blue")

TIMER_EVENT = pygame.event.custom_type()
pygame.time.set_timer(TIMER_EVENT, 50)

def check_collision(self, obj2):
    if (self.col_left <= obj2.col_right 
        and self.col_right >= obj2.col_left
        and self.col_top <= obj2.col_bot
        and self.col_bot >= obj2.col_top):
        ui.letter_caught(obj2)
        obj2.collision()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    updatable_player.update(dt)
    updatable_obj.update()

    screen.fill("#210541")
    screen.blit(background, (0, 0))

    #Render game here
    
    for obj in drawable_obj:
        check_collision(player, obj)

    for obj in drawable_player:
        obj.draw(screen)

    for obj in drawable_obj:
        obj.draw(screen)

    #This is where we spawn in more letters
    current_time = pygame.time.get_ticks()
    if current_time - last_spawn_time >= SPAWN_INTERVAL:
        new_letter = Letter("blue", ALPHABET[get_random(0, len(ALPHABET) - 1)])
        updatable_obj.add(new_letter)
        drawable_obj.add(new_letter)
        last_spawn_time = current_time

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        pygame.QUIT
        running = False

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()

