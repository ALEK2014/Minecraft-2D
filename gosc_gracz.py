import pygame
from settings import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU, ROZMIAR_BLOKU, POZIOM_TERENU, PRENDKOSC, GRAWITACJA, SILA_SKOKU

class Gracz:
    def __init__(self):
        self.szerokosc = 32
        self.wysokosc = 60
        self.x = SZEROKOSC_EKRANU // 2
        self.y = (POZIOM_TERENU - 2) * ROZMIAR_BLOKU - self.wysokosc
        self.prendkosc_y = 0
        self.na_ziemi_ksienzyca = False

    def ruch(self, swiat):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            self.x -= PRENDKOSC
        if klawisze[pygame.K_RIGHT]:
            self.x += PRENDKOSC
        if klawisze[pygame.K_SPACE]:
            if self.na_ziemi_ksienzyca == True:
                self.prendkosc_y = SILA_SKOKU

#grawitacja mario
        self.prendkosc_y += GRAWITACJA
        self.y += int(self.prendkosc_y)
#kolizja z ziemią mario 
        dotykanie_y = (self.y + self.wysokosc) // ROZMIAR_BLOKU
        dotykanie_x = self.x // ROZMIAR_BLOKU
        if dotykanie_y < len(swiat):
            blok = swiat[dotykanie_y][min(dotykanie_x, len(swiat[0]), -1)]
            if blok != "powietrze":
                self.na_ziemi_ksienzyca = True
                self.prendkosc_y = 0
            else:
                self.na_ziemi_ksienzyca = False
    
    def jestem(self, screen):
        pygame.draw.rect(screen, (0, 196, 224), (self.x + 5, self.y + 12, self.szerokosc - 10, self.wysokosc - 18))
        pygame.draw.rect(screen, (0, 0, 156), (self.x + 5, self.y + 40, self.szerokosc - 10, self.wysokosc //2 - 10))
        pygame.draw.rect(screen, (0, 196, 224), (self.x - 3, self.y + 12, self.szerokosc - 24 , self.wysokosc - 36))
        pygame.draw.rect(screen, (0, 196, 224), (self.x + 27, self.y + 12, self.szerokosc - 24 , self.wysokosc - 36))
        pygame.draw.rect(screen, (245, 224, 209), (self.x + 5, self.y - 8, self.szerokosc - 10, self.wysokosc - 40))

