import pygame
from wygenerowanie_terenu import generator_terenu_A
from settings import ROZMIAR_BLOKU, KOLORY, PRZYPISANIE_KLAWISZY, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU


def hotbar_minecraft_mace(ekran):
    shtm = 736
    khtm = shtm / 9

    punkt_Maciejax = (shtm - SZEROKOSC_EKRANU) // -2
    punkt_Maciejay = WYSOKOSC_EKRANU - khtm
    obramowanie = 3
    hotbar_pasek = pygame.Rect(punkt_Maciejax - obramowanie, punkt_Maciejay - obramowanie, shtm + obramowanie * 2, khtm + obramowanie * 2)
    przezroczystosc_lol_pl = 150
    tlo = pygame.Surface()
    pygame.draw.rect(ekran, (58, 58, 58, 50), hotbar_pasek)

