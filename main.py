from settings import KOLORY, ROZMIAR_BLOKU, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU
from wygenerowanie_terenu import generuj_swiat_minecraft
import pygame

def main_minecraft():
    pygame.init()
    screen = pygame.display.set_mode((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))
    ikona = pygame.image.load("grafiki/1770744660_b833e63dfda26aefeb986083bc106177_1.png")
    pygame.display.set_icon(ikona)
    pygame.display.set_caption('Minecraft 2D')
    gra = True
    while gra:
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_ESCAPE:
                    gra = False
            if zdarzenie.type == pygame.QUIT:
                gra = False


if __name__ == "__main__":
    main_minecraft()



























