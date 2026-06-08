import pygame
from wygenerowanie_terenu import generator_terenu_A
from settings import ROZMIAR_BLOKU, KOLORY, PRZYPISANIE_KLAWISZY, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU


def hotbar_minecraft_mace(ekran):
    shtm = 736
    khtm = shtm / 9

    punkt_Maciejax = (shtm - SZEROKOSC_EKRANU) // 2
    punkt_Maciejay = WYSOKOSC_EKRANU - khtm