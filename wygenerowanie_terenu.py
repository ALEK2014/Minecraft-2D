from settings import BLOKI_X, BLOKI_Y, POZIOM_TERENU
import random
def stworzenie_pustego_swiata():
    swiat = [] 
    #BLOKI_X = SZEROKOSC_EKRANU // ROZMIAR_BLOKU
    #BLOKI_Y = WYSOKOSC_EKRANU // ROZMIAR_BLOKU
    for y in range(BLOKI_Y):
        wiersz = []
        for x in range(BLOKI_X):
            wiersz.append("powietrze")
        swiat.append(wiersz)

    return swiat


def generator_terenu_A(swiat):

    KROK = 4

    liczba_losowan = BLOKI_X // KROK + 2

    punkty = [POZIOM_TERENU + random.randint(-3, 3) for losowanie in range(liczba_losowan)]
#interpolacja
    for x in range(BLOKI_X):
        segment = x // KROK
        essa = (x % KROK) / KROK
        essa_plynne = essa*essa*(3 - 2*essa)
        p1 = punkty[segment]
        p2 = punkty[segment + 1]
        wysokosc = round(p1 + essa_plynne*(p2 - p1))
        for y in range(BLOKI_Y):
            if y < wysokosc:
                swiat[y][x] = "powietrze"
            elif y == wysokosc:
                swiat[y][x] = "trawa"
            elif y <= wysokosc + 3:
                swiat[y][x] = "ziemia"
            else:
                swiat[y][x] = "kamien"
            
    return swiat

def nudne_generowanie_drzewa(swiat, x, y):
    for pien in range(1, 4):
        ny_blokow = y - pien
        if 0 <= ny_blokow < BLOKI_Y:
            swiat[ny_blokow][x] = "drewno"
    for dy, szerokosc in [(-5, 1), (-4, 2), (-3, 3)]:
        for dx in range(-szerokosc, szerokosc + 1):
            ny_blokow = y + dy
            nx_blokow = x + dx
            if 0 <= ny_blokow < BLOKI_Y:
                if swiat[ny_blokow][nx_blokow] != "drewno":
                    swiat[ny_blokow][nx_blokow] = "liscie"

def nudne_osadzenie_drzewa(swiat):
    for y in range(BLOKI_Y):
        for x in range(4 , BLOKI_X - 4):
            if swiat[y][x] == "trawa":
               nudne_generowanie_drzewa(swiat, x, y)
               break
    return swiat

def generuj_swiat_minecraft():
    swiat = stworzenie_pustego_swiata()
    swiat = generator_terenu_A(swiat)
    swiat = nudne_osadzenie_drzewa(swiat)
    return swiat


if __name__ == "__main__":
    generuj_swiat_minecraft()
#     swiat = generuj_swiat_minecraft()

# SYMBOLE = {
#     "powietrze": ".",
#     "trawa": "#",
#     "ziemia":"=",
#    nt(liczba_losowan) "kamien":"@"       
#     }

# for wiersz in swiat:
#     linia = ""
#     for blok in wiersz:
#         linia += SYMBOLE[blok]
#     print(linia)

