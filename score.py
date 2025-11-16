import pygame
import os

class Score:
    SAVE_FILE = os.path.join(os.path.dirname(__file__), "highscore.txt")

    def __init__(self, font_name=None, size=24, color=(255,255,255), pos=(10,10)):
        pygame.font.init()
        self.font = pygame.font.SysFont(font_name, size)
        self.color = color
        self.pos = pos
        self.value = 0
        self.high = self._load_high()

    def add(self, points):
        self.value += points
        if self.value > self.high:
            self.high = self.value

    def draw(self, screen):
        txt = f"Score: {self.value}  High: {self.high}"
        surf = self.font.render(txt, True, self.color)
        screen.blit(surf, self.pos)

    def save(self):
        try:
            with open(self.SAVE_FILE, "w") as f:
                f.write(str(self.high))
        except Exception:
            pass

    def _load_high(self):
        try:
            with open(self.SAVE_FILE, "r") as f:
                return int(f.read().strip() or 0)
        except Exception:
            return 0