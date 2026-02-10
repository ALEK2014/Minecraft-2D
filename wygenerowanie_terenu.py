from settings import BLOKI_X, BLOKI_Y, POZIOM_TERENU

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
    for y in range(BLOKI_Y):
        for x in range(BLOKI_X):
            if y < POZIOM_TERENU:
                swiat[y][x] = "powietrze"
            elif y == POZIOM_TERENU:
                swiat[y][x] = "trawa"
            elif y <= POZIOM_TERENU + 3:
                swiat[y][x] = "ziemia"
            else:
                swiat[y][x] = "kamien"
    return swiat




def generuj_swiat_minecraft():
    swiat = stworzenie_pustego_swiata()
    swiat = generator_terenu_A(swiat)
    return swiat


# if __name__ == "__main__":
#     swiat = generuj_swiat_minecraft()

# SYMBOLE = {
#     "powietrze": ".",
#     "trawa": "#",
#     "ziemia":"=",
#     "kamien":"@"       
#     }

# for wiersz in swiat:
#     linia = ""
#     for blok in wiersz:
#         linia += SYMBOLE[blok]
#     print(linia)

