import pygame

class UI(pygame.sprite.Sprite):
    def __init__(self, display_height):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.pos = (40, display_height - 80)
        self.letters = ""

    def letter_caught(self, new_letter):
        if len(self.letters) <= 16:
            self.letters += new_letter.char
        else:
            self.letters = ""

    def draw(self, screen):
        self.word = pygame.font.Font.render((pygame.font.SysFont("Arial", 40, bold=False)), self.letters, 0, "green")
        screen.blit((self.word), self.pos)

    def update():
        pass