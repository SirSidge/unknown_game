import pygame
from src.get_random import get_random
from src.constants import display_height, display_width

letter_height = 50
letter_width = 50
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

letter = pygame.Rect(get_random(0, display_width - letter_width), get_random(0, display_height - letter_height), letter_width, letter_height)

class Letter():
    def __init__(self):
        self.letter = alphabet[get_random(0, len(alphabet) - 1)]
        self.pos = (letter.x, letter.y)
        self.size = 60
        self.radius = self.size / 2
        self.img = pygame.font.SysFont("Arial", self.size).render(self.letter, True, "blue")
