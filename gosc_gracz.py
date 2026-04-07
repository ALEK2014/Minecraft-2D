import pygame
from settings import SZEROKOSC_EKRANU, WYSOKOSC_EKRANU, ROZMIAR_BLOKU, POZIOM_TERENU

class Gracz:
    def __init__(self):
        self.szerokosc = 24
        self.wysokosc = 40
        self.x = SZEROKOSC_EKRANU // 2
        self.y = (POZIOM_TERENU - 2) * ROZMIAR_BLOKU - self.wysokosc

    def ruch(self):
        