import pygame
from src.constants import screen_width, screen_height

class Player:
    def __init__(self):
        self.pos = pygame.Vector2(screen_width / 2, screen_height / 2)
        self.color = "red"
        self.size = 40
        self.speed = 400
        self.diagonal_speed = self.speed * 0.72