import pygame
from settings import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU, ROZMIAR_BLOKU, POZIOM_TERENU, PRENDKOSC

class Gracz:
    def __init__(self):
        self.szerokosc = 32
        self.wysokosc = 60
        self.x = SZEROKOSC_EKRANU // 2
        self.y = (POZIOM_TERENU - 2) * ROZMIAR_BLOKU - self.wysokosc

    def ruch(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            self.x -= PRENDKOSC
        if klawisze[pygame.K_RIGHT]:
            self.x += PRENDKOSC
    
    def jestem(self, screen):
        pygame.draw.rect(screen, (236, 204, 196), (self.x, self.y, self.szerokosc, self.wysokosc))
        pygame.draw.rect(screen, (0, 0, 156), (self.x, self.y + 30, self.szerokosc, self.wysokosc //2))
        pygame.draw.rect(screen, (0, 196, 224), (self.x - 8, self.y + 12, self.szerokosc - 24 , self.wysokosc - 30))
        pygame.draw.rect(screen, (0, 196, 224), (self.x + 32, self.y + 12, self.szerokosc - 24 , self.wysokosc - 30))

