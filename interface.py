import pygame
from wygenerowanie_terenu import generator_terenu_A
from settings import ROZMIAR_BLOKU, KOLORY, PRZYPISANIE_KLAWISZY, WYSOKOSC_EKRANU, SZEROKOSC_EKRANU

def hotbar_minecraft_mace(ekran, bloczki, aha_czyli_to_ty):
    shtm = 736
    khtm = shtm / 9

    punkt_Maciejax = (shtm - SZEROKOSC_EKRANU) // -2
    punkt_Maciejay = WYSOKOSC_EKRANU - khtm
    obramowanie = 3
    hotbar_pasek = pygame.Rect(punkt_Maciejax - obramowanie, punkt_Maciejay - obramowanie, shtm + obramowanie * 2, khtm + obramowanie * 2)
    przezroczystosc_lol_pl = 200
    tlo = pygame.Surface(hotbar_pasek.size)
    tlo.fill((55,55,55))
    tlo.set_alpha(przezroczystosc_lol_pl)
    ekran.blit(tlo, hotbar_pasek.topleft)
    pygame.draw.rect(ekran, (0,0,0), hotbar_pasek, obramowanie)

    for minecraft_og in range(9): 
        kratka_z_blokiem_sadzonym = pygame.Rect(punkt_Maciejax, punkt_Maciejay, khtm, khtm)
        punkt_Maciejax = punkt_Maciejax + khtm
        obramowanie = 8
        pygame.draw.rect(ekran, (150,150,150), kratka_z_blokiem_sadzonym, obramowanie)
        if len(bloczki) > minecraft_og:
            lokory = KOLORY[bloczki[minecraft_og]]
            blok_sadzony = kratka_z_blokiem_sadzonym.inflate(-40, -40)
            pygame.draw.rect(ekran, lokory, blok_sadzony)

    nununummerek = bloczki.index(aha_czyli_to_ty)
    the_decision_of_your_life = pygame.Rect(punkt_Maciejax - khtm*9 - khtm * -nununummerek, punkt_Maciejay , khtm, khtm)
    pygame.draw.rect(ekran, (200, 200, 200), the_decision_of_your_life, obramowanie + 4)