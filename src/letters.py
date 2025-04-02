import pygame

from get_random import get_random
from constants import screen_width, screen_height

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_size = 40

class Letter(pygame.sprite.Sprite):
    def __init__(self, color):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.letter = self.get_letter()
        self.color = color
        self.pos = [get_random(0, screen_width), get_random(0, screen_height)]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], letter_size, letter_size)
    
    def get_letter(self):
        return alphabet[get_random(0, len(alphabet) - 1)]
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def collision(self):
        #print("Collision detected")
        self.kill()

    def update(self):
        self.col_left = self.pos[0] - (letter_size / 2)
        self.col_right = self.pos[0] + (letter_size / 2)
        self.col_top = self.pos[1] - (letter_size / 2)
        self.col_bot = self.pos[1] + (letter_size / 2)