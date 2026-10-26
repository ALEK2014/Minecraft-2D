from settings import KOLORY, ROZMIAR_BLOKU, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU, GRAWITACJA, PRZYPISANIE_KLAWISZY, BLOKI_X
from wygenerowanie_terenu import generuj_swiat_minecraft
import pygame
from gosc_gracz import Gracz
from interface import hotbar_minecraft_mace

def rysuj_swiat_minecraft(swiat_minecraft, screen, monimeraX):
    pierwsza_starozytna_kolumna_ekranu = monimeraX // ROZMIAR_BLOKU 
    ostatnia_wspolczesna_kolumna_ekranu = min(pierwsza_starozytna_kolumna_ekranu + BLOKI_X + 1 , len(swiat_minecraft[0]) - 1)
    for y, wiersz in enumerate(swiat_minecraft):
        for x in range(pierwsza_starozytna_kolumna_ekranu, ostatnia_wspolczesna_kolumna_ekranu + 1):
            blok = wiersz[x]
            pozycja_x = x*ROZMIAR_BLOKU - monimeraX
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
    patelnia_blokow = [nazwa for nazwa in KOLORY if nazwa != "powietrze"]
    wybrany_bloczek = patelnia_blokow[0]
    gra = True
    while gra:
        monimeraX = int(gracz.x) + gracz.szerokosc // 2 - SZEROKOSC_EKRANU // 2
        for zdarzenie in pygame.event.get():
            if zdarzenie.type == pygame.KEYDOWN:
                if zdarzenie.key == pygame.K_ESCAPE:
                    gra = False
                if zdarzenie.key in PRZYPISANIE_KLAWISZY:
                    numerek = PRZYPISANIE_KLAWISZY[zdarzenie.key]
                    if numerek < len(patelnia_blokow):
                        wybrany_bloczek = patelnia_blokow[numerek]
            if zdarzenie.type == pygame.QUIT:
                gra = False
            if zdarzenie.type == pygame.MOUSEBUTTONDOWN:
                if zdarzenie.button == 1:
                    myszka_x, myszka_y = pygame.mouse.get_pos()
                    #print(f"Lewy przycisk myszy kliknięty na pozycji: {myszka_y}, {myszka_x}")

                    mbx = myszka_x // ROZMIAR_BLOKU 
                    mby = myszka_y // ROZMIAR_BLOKU
                    #print(f"Lewy przycisk myszy kliknięty na pozycji: {mby}, {mbx}")

                    if 0 <= mby < len(swiat) and 0 <= mbx < len(swiat[0]):
                        swiat[mby][mbx] = "powietrze"

            
                if zdarzenie.button == 3:
                    myszka_x, myszka_y = pygame.mouse.get_pos()
                    #print(f"Lewy przycisk myszy kliknięty na pozycji: {myszka_y}, {myszka_x}")

                    mbx = myszka_x // ROZMIAR_BLOKU
                    mby = myszka_y // ROZMIAR_BLOKU
                    #print(f"Lewy przycisk myszy kliknięty na pozycji: {mby}, {mbx}")                    
                    

                    if 0 <= mby < len(swiat) and 0 <= mbx < len(swiat[0]) and swiat[mby][mbx] == "powietrze":

                        # blok_x = mbx * ROZMIAR_BLOKU
                        # blok_y = mby * ROZMIAR_BLOKU
                        
                        swiat[mby][mbx] = wybrany_bloczek

                        
                            

        
        rysuj_swiat_minecraft(swiat_minecraft=swiat, screen=ekran, monimeraX= monimeraX)
        gracz.jestem(ekran, monimeraX)
        gracz.ruch(swiat)
        hotbar_minecraft_mace(ekran, bloczki= patelnia_blokow, aha_czyli_to_ty= wybrany_bloczek)
        pygame.display.flip()
        zegarek_GARMIN.tick(60)
        
        
        
        
    

if __name__ == "__main__":
    main_minecraft()

    





























