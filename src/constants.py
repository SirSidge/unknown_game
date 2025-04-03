import pygame

display_height = 1080
display_width = 1920
screen = pygame.display.set_mode((display_width, display_height))
screen_width = screen.get_width()
screen_height = screen.get_height()

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

PLAYER_RADIUS = 40
PLAYER_TURN_SPEED = 200
PLAYER_SPEED = 350