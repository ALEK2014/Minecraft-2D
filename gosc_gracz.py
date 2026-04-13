import pygame
from settings import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU, ROZMIAR_BLOKU, POZIOM_TERENU, PRENDKOSC

class Gracz:
    def __init__(self):
        self.szerokosc = 24
        self.wysokosc = 40
        self.x = SZEROKOSC_EKRANU // 2
        self.y = (POZIOM_TERENU - 2) * ROZMIAR_BLOKU - self.wysokosc

    def ruch(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            self.x -= PRENDKOSC
        if klawisze[pygame.K_RIGHT]:
            self.x += PRENDKOSC
    
    def jestem(self, screen):
        pygame.draw.rect((0, 0, 0))




