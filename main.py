from settings import KOLORY, ROZMIAR_BLOKU, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU, GRAWITACJA
from wygenerowanie_terenu import generuj_swiat_minecraft
import pygame
from gosc_gracz import Gracz

def rysuj_swiat_minecraft(swiat_minecraft, screen):
    for y, wiersz in enumerate(swiat_minecraft):
        for x, blok in enumerate(wiersz):
            pozycja_x = x*ROZMIAR_BLOKU
            pozycja_y = y*ROZMIAR_BLOKU

            kolor = KOLORY[blok]
            blok1 = pygame.Rect(pozycja_x, pozycja_y, ROZMIAR_BLOKU, ROZMIAR_BLOKU)
            pygame.draw.rect(screen, kolor, blok1)

def main_minecraft():
    pygame.init()
    ekran = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
    ikona = pygame.image.load("grafiki/1770744660_b833e63dfda26aefeb986083bc106177_1.png")
    pygame.display.set_icon(ikona)
    pygame.display.set_caption('Minecraft 2D')

    zegarek_GARMIN = pygame.time.Clock()

    swiat = generuj_swiat_minecraft()
    gracz = Gracz()
    gra = True
    while gra:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_ESCAPE:
                    gra = False
            if zdarzenie.type == pygame.QUIT:
                gra = False
        
        rysuj_swiat_minecraft(swiat_minecraft=swiat, screen=ekran)
        gracz.jestem(ekran)
        gracz.ruch(swiat)
        pygame.display.flip()
        zegarek_GARMIN.tick(60)
        
        
        
    

if __name__ == "__main__":
    main_minecraft()

    





























