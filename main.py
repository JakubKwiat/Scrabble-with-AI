import random
import sys
import Scrabble
from Gra_z_botem import *
import enchant
import pygame
def losowanie_litery(worek_z_literami):
     ilosc_liter_w_worku=len(worek_z_literami)
     x=random.randint(0,ilosc_liter_w_worku-1)
     wylosowana_litera=worek_z_literami[x]
     worek_z_literami.pop(x)
     return wylosowana_litera

def ukladanie_planszy():
    g = Scrabble.Scrable()

    pop_pocz = g.losowanie_populacji_poczatkowej()
    wyniki = []

    for i in range(0, 5):
        if i == 0:
            sel = g.selekcja(pop_pocz, 100)
        else:
            sel = g.selekcja(krz, 100)
        krz = g.krzyzowanie(sel, 100)
        wynik = g.znajdz_najlepszy_wynik(krz)
        wyniki.append(wynik)
        if i == 4:
            najlepsza_plansza = g.znajdz_najlepsza_plansze(krz)
            g.delsam(najlepsza_plansza)
        print("ukonczono iteracje")
        print(i)
        print("najlepszy wynik")
        print(wynik)

    print("tablica wynikow")
    print(wyniki)
    print("najlepsza plansza")
    print(najlepsza_plansza)

    return najlepsza_plansza

def dobieranie_7_liter_na_start(worek_z_literami,lista_liter_gracz):
    for i in range(7):
        lista_liter_gracz.append(losowanie_litery(worek_z_literami))
    return lista_liter_gracz

def dobieranie_liter_po_odrzuceniu(worek_z_literami,lista_liter_gracz,ilosc_liter_do_odrzucenia):
    lista_liter_do_odrzucenia=[]
    for i in range(ilosc_liter_do_odrzucenia):
        litera_do_odrzucenia=input("podaj litera jaka chcesz odrzucic: ")
        lista_liter_do_odrzucenia.append(litera_do_odrzucenia)
        lista_liter_gracz.remove(litera_do_odrzucenia)
    ilosc_liter_do_wylosowania=ilosc_liter_do_odrzucenia
    for i in range(ilosc_liter_do_wylosowania):
        lista_liter_gracz.append(losowanie_litery(worek_z_literami))
    for i in range(ilosc_liter_do_odrzucenia):
        worek_z_literami.append(lista_liter_do_odrzucenia[i])
    return lista_liter_gracz

def odczyt_z_pliku(nazwa_pliku,wymiar_planszy_x,wymiar_planszy_y):
    f = open(nazwa_pliku)
    plansza_z_pliku = f.read()
    plansza_z_pliku = plansza_z_pliku.split('\n')
    plansza_z_pliku = [l.split(',') for l in plansza_z_pliku]
    f.close()
    for i in range(wymiar_planszy_x):
        print()
        for j in range(wymiar_planszy_y):
            sys.stdout.write(str(plansza_z_pliku[i][j]))
            sys.stdout.write(' ')
    return plansza_z_pliku

def zapis_do_pliku(nazwa_pliku,wymiar_planszy_x,wymiar_planszy_y,plansza):
    plik = open(nazwa_pliku, 'w')
    for i in range(wymiar_planszy_x):
        for j in range(wymiar_planszy_y):
            plik.write(str(plansza[i][j]))
            if (j != wymiar_planszy_y - 1):
                plik.write(',')
        plik.write('\n')
    plik.close()
if __name__ == '__main__':
    slownik = enchant.Dict("en_US")
    # worek_z_literami=['a','a','a','a','a','a','a','a','a','b','b','c','c','d','d','d','d','e','e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','g','h','h','i','i','i','i','i','i','i','i','i','j','k','l','l','l','l','m','m','n','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r','r','r','r','r','r','s','s','s','s','t','t','t','t','t','t','u','u','u','u','v','v','w','w','x','y','y','z']
    # lista_liter_gracz=[]
    # dobieranie_7_liter_na_start(worek_z_literami,lista_liter_gracz)
    # print(lista_liter_gracz)
    # ilosc_liter_do_odrzucenia=int(input("ilosc liter jaka chcesz odrzucic: "))
    # dobieranie_liter_po_odrzuceniu(worek_z_literami,lista_liter_gracz,ilosc_liter_do_odrzucenia)
    # print(lista_liter_gracz)
    wymiar_planszy_x=wymiar_planszy_y=15
    # plansza=[['3W',0,0,'2L',0,0,0,'3W',0,0,0,'2L',0,0,'3W'],
    #           [0,'2W',0,0,0,'3L',0,0,0,'3L',0,0,0,'2W',0],
    #           [0,0,'2W',0,0,0,'2L',0,'2L',0,0,0,'2W',0,0],
    #           ['2L',0,0,'2W',0,0,0,'2L',0,0,0,'2W',0,0,'2L'],
    #           [0,0,0,0,'2W',0,0,0,0,0,'2W',0,0,0,0],
    #           [0,'3L',0,0,0,'3L',0,0,0,'3L',0,0,0,'3L',0],
    #           [0,0,'2L',0,0,0,'2L',0,'2L',0,0,0,'2L',0,0],
    #           ['3W',0,0,'2L',0,0,0,'ST',0,0,0,'2L',0,0,'3W'],
    #           [0,0,'2L',0,0,0,'2L',0,'2L',0,0,0,'2L',0,0],
    #           [0, '3L', 0, 0, 0, '3L', 0, 0, 0, '3L', 0, 0, 0, '3L', 0],
    #           [0, 0, 0, 0, '2W', 0, 0, 0, 0, 0, '2W', 0, 0, 0, 0],
    #           ['2L', 0, 0, '2W', 0, 0, 0, '2L', 0, 0, 0, '2W', 0, 0, '2L'],
    #           [0, 0, '2W', 0, 0, 0, '2L', 0, '2L', 0, 0, 0, '2W', 0, 0],
    #           [0, '2W', 0, 0, 0, '3L', 0, 0, 0, '3L', 0, 0, 0, '2W', 0],
    #           ['3W', 0, 0, '2L', 0, 0, 0, '3W', 0, 0, 0, '2L', 0, 0, '3W'],]
    #nazwa_pliku_do_odczytu=input("Podaj nazwe pliku, z którego chcesz odczytać plansze: ")
    nazwa_pliku_do_odczytu="plansza.txt"
    plansza=odczyt_z_pliku(nazwa_pliku_do_odczytu,wymiar_planszy_x,wymiar_planszy_y)
    # print()
    # nazwa_pliku_do_zapisu=input("Podaj nazwe pliku do jakiego chcesz zapisac: ")
    # zapis_do_pliku(nazwa_pliku_do_zapisu)
    pygame.init()
    screen=pygame.display.set_mode((1024,768))
    pygame.display.set_caption("Scrabble")
    icon=pygame.image.load("scrabble.png")
    pygame.display.set_icon(icon)
    f = open('alfabet.txt')
    alfabet = f.read()
    alfabet = alfabet.split(',')
    f.close()
    png1_x=270
    png1_y=250
    png1=pygame.image.load('BOT.png')
    png2_x=270
    png2_y=350
    png2=pygame.image.load('GRA_Z_BOTEM.png')
    png3_x=270
    png3_y=450
    png3=pygame.image.load('WYJSCIE.png')
    logo_x=140
    logo_y=50
    logo=pygame.image.load('Scrabble_logo.png')
    puste_pole=pygame.image.load('puste_pole.png')
    potrojne_slowo=pygame.image.load('potrojne_slowo.png')
    potrojna_litera=pygame.image.load('potrojna_litera.png')
    podwojne_slowo=pygame.image.load('podwojne_slowo.png')
    podwojna_litera=pygame.image.load('podwojna_litera.png')
    start=pygame.image.load('start.png')
    A_png=pygame.image.load('literki/A.png')
    B_png=pygame.image.load('literki/B.png')
    C_png=pygame.image.load('literki/C.png')
    D_png=pygame.image.load('literki/D.png')
    E_png=pygame.image.load('literki/E.png')
    F_png=pygame.image.load('literki/F.png')
    G_png=pygame.image.load('literki/G.png')
    H_png=pygame.image.load('literki/H.png')
    I_png=pygame.image.load('literki/I.png')
    J_png=pygame.image.load('literki/J.png')
    K_png=pygame.image.load('literki/K.png')
    L_png=pygame.image.load('literki/L.png')
    M_png=pygame.image.load('literki/M.png')
    N_png=pygame.image.load('literki/N.png')
    O_png=pygame.image.load('literki/O.png')
    P_png=pygame.image.load('literki/P.png')
    R_png=pygame.image.load('literki/R.png')
    S_png=pygame.image.load('literki/S.png')
    T_png=pygame.image.load('literki/T.png')
    U_png=pygame.image.load('literki/U.png')
    W_png=pygame.image.load('literki/W.png')
    V_png=pygame.image.load('literki/V.png')
    X_png=pygame.image.load('literki/X.png')
    Y_png=pygame.image.load('literki/Y.png')
    Z_png=pygame.image.load('literki/Z.png')
    Q_png=pygame.image.load('literki/Q.png')
    worek_z_literami=['a','a','a','a','a','a','a','a','a','b','b','c','c','d','d','d','d','e','e','e','e','e','e','e','e','e','e','e','e','f','f','g','g','g','h','h','i','i','i','i','i','i','i','i','i','j','k','l','l','l','l','m','m','n','n','n','n','n','n','o','o','o','o','o','o','o','o','p','p','q','r','r','r','r','r','r','s','s','s','s','t','t','t','t','t','t','u','u','u','u','v','v','w','w','x','y','y','z']
    lista_liter_gracz=[]
    lista_liter_bot=[]
    ilosc_liter_do_odrzucenia=0
    base_font=pygame.font.Font(None,32)
    base_font1 = pygame.font.Font(None, 24)
    user_text=''
    input_rect = pygame.Rect(750,600,150,30)
    color=pygame.Color('lightskyblue3')
    podpowiedz='Litera do wymiany w formacie: litera,miejsce'
    score1='Wynik bota: '
    score2='Twój wynik: '
    score1_int=0
    score2_int=0
    running=True
    while running:
        for event in pygame.event.get():
            screen.fill((0, 128, 0))
            screen.blit(png1, (png1_x, png1_y))
            screen.blit(png2, (png2_x, png2_y))
            screen.blit(png3, (png3_x, png3_y))
            screen.blit(logo, (logo_x, logo_y))
            pygame.display.update()
            skonczone = 0

            if(event.type==pygame.QUIT):
                running=False
            elif(event.type==pygame.MOUSEBUTTONDOWN):
                if event.pos[0]>270 and event.pos[0]<738 and event.pos[1]>450 and event.pos[1]<518:#WYJSCIE
                            running=False
                elif event.pos[0]>270 and event.pos[0]<728 and event.pos[1]>250 and event.pos[1]<317: #BOT
                            while running:
                                if (skonczone == 0):
                                    multiplikatory = [[7, 1, 2, 3, 2, 1, 7],
                                                      [1, 6, 1, 1, 1, 6, 1],
                                                      [2, 1, 6, 1, 6, 1, 2],
                                                      [3, 1, 1, 6, 1, 1, 3],
                                                      [2, 1, 6, 1, 6, 1, 2],
                                                      [1, 6, 1, 1, 1, 6, 1],
                                                      [7, 1, 2, 3, 2, 1, 7]]
                                    plansza = ukladanie_planszy()
                                    skonczone = 1
                                for event in pygame.event.get():
                                    screen.fill((200, 230, 0))
                                    for i in range(7):   #wymiar_planszy_x
                                        for j in range(7):  #wymiar_planszy_y
                                            if(plansza[i][j]=='-'):
                                                screen.blit(puste_pole,(50+40*i,50+40*j))
                                            elif (plansza[i][j] == '-' and multiplikatory[i][j] == 7):
                                                screen.blit(potrojne_slowo, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == '-' and multiplikatory[i][j] == 6):
                                                screen.blit(podwojne_slowo, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == '-' and multiplikatory[i][j] == 3):
                                                screen.blit(potrojna_litera, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == '-' and multiplikatory[i][j] == 2):
                                                screen.blit(podwojna_litera, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'ST'):
                                                screen.blit(start, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'a'):
                                                screen.blit(A_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'b'):
                                                screen.blit(B_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'c'):
                                                screen.blit(C_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'd'):
                                                screen.blit(D_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'e'):
                                                screen.blit(E_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'f'):
                                                screen.blit(F_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'g'):
                                                screen.blit(G_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'h'):
                                                screen.blit(H_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'i'):
                                                screen.blit(I_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'j'):
                                                screen.blit(J_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'k'):
                                                screen.blit(K_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'l'):
                                                screen.blit(L_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'm'):
                                                screen.blit(M_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'n'):
                                                screen.blit(N_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'o'):
                                                screen.blit(O_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'p'):
                                                screen.blit(P_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'r'):
                                                screen.blit(R_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 's'):
                                                screen.blit(S_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 't'):
                                                screen.blit(T_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'u'):
                                                screen.blit(U_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'w'):
                                                screen.blit(W_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'v'):
                                                screen.blit(V_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'q'):
                                                screen.blit(Q_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'x'):
                                                screen.blit(X_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'y'):
                                                screen.blit(Y_png, (50 + 40 * i, 50 + 40 * j))
                                            elif (plansza[i][j] == 'z'):
                                                screen.blit(Z_png, (50 + 40 * i, 50 + 40 * j))
                                    pygame.display.update()
                                    if (event.type == pygame.QUIT):
                                        running = False
                elif event.pos[0] > 270 and event.pos[0] < 733 and event.pos[1] > 350 and event.pos[1] < 500:#GRA Z BOTEM
                    plansza[7][7] = "#"
                    dobieranie_7_liter_na_start(worek_z_literami, lista_liter_gracz)
                    dobieranie_7_liter_na_start(worek_z_literami, lista_liter_bot)
                    tura = 0
                    punkty_gracza = 0
                    punkty_bota = 0
                    while running:
                        for event in pygame.event.get():
                            screen.fill((200, 230, 0))
                            for i in range(wymiar_planszy_x):
                                literka_przy_planszy=alfabet[i]
                                text_surface_planszax = base_font1.render(literka_przy_planszy, True, (0, 0, 0))
                                screen.blit(text_surface_planszax, (35, 55 + 40*i))
                            for i in range(wymiar_planszy_y):
                                cyferka_przy_planszy=i
                                text_surface_planszay = base_font1.render(str(cyferka_przy_planszy), True, (0, 0, 0))
                                screen.blit(text_surface_planszay, (55+40*i,35))
                            for i in range(wymiar_planszy_x):
                                for j in range(wymiar_planszy_y):
                                    if (plansza[i][j] == '0'):
                                        screen.blit(puste_pole, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == '3W'):
                                        screen.blit(potrojne_slowo, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == '2W'):
                                        screen.blit(podwojne_slowo, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == '3L'):
                                        screen.blit(potrojna_litera, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == '2L'):
                                        screen.blit(podwojna_litera, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'ST'):
                                        screen.blit(start, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'a'):
                                        screen.blit(A_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'b'):
                                        screen.blit(B_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'c'):
                                        screen.blit(C_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'd'):
                                        screen.blit(D_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'e'):
                                        screen.blit(E_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'f'):
                                        screen.blit(F_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'g'):
                                        screen.blit(G_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'h'):
                                        screen.blit(H_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'i'):
                                        screen.blit(I_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'j'):
                                        screen.blit(J_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'k'):
                                        screen.blit(K_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'l'):
                                        screen.blit(L_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'm'):
                                        screen.blit(M_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'n'):
                                        screen.blit(N_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'o'):
                                        screen.blit(O_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'p'):
                                        screen.blit(P_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'r'):
                                        screen.blit(R_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 's'):
                                        screen.blit(S_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 't'):
                                        screen.blit(T_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'u'):
                                        screen.blit(U_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'w'):
                                        screen.blit(W_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'v'):
                                        screen.blit(V_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'q'):
                                        screen.blit(Q_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'x'):
                                        screen.blit(X_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'y'):
                                        screen.blit(Y_png, (50 + 40 * i, 50 + 40 * j))
                                    elif (plansza[i][j] == 'z'):
                                        screen.blit(Z_png, (50 + 40 * i, 50 + 40 * j))
                            for i in range(len(lista_liter_gracz)):
                                if (lista_liter_gracz[i] == 'a'):
                                    screen.blit(A_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'b'):
                                    screen.blit(B_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'c'):
                                    screen.blit(C_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'd'):
                                    screen.blit(D_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'e'):
                                    screen.blit(E_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'f'):
                                    screen.blit(F_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'g'):
                                    screen.blit(G_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'h'):
                                    screen.blit(H_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'i'):
                                    screen.blit(I_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'j'):
                                    screen.blit(J_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'k'):
                                    screen.blit(K_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'l'):
                                    screen.blit(L_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'm'):
                                    screen.blit(M_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'n'):
                                    screen.blit(N_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'o'):
                                    screen.blit(O_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'p'):
                                    screen.blit(P_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'r'):
                                    screen.blit(R_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 's'):
                                    screen.blit(S_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 't'):
                                    screen.blit(T_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'u'):
                                    screen.blit(U_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'w'):
                                    screen.blit(W_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'v'):
                                    screen.blit(V_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'x'):
                                    screen.blit(X_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'y'):
                                    screen.blit(Y_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'z'):
                                    screen.blit(Z_png, (750, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'q'):
                                    screen.blit(Q_png, (750, 40 + 50 * i))
                            for i in range(len(lista_liter_bot)):
                                if (lista_liter_bot[i] == 'a'):
                                    screen.blit(A_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'b'):
                                    screen.blit(B_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'c'):
                                    screen.blit(C_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'd'):
                                    screen.blit(D_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'e'):
                                    screen.blit(E_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'f'):
                                    screen.blit(F_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'g'):
                                    screen.blit(G_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'h'):
                                    screen.blit(H_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'i'):
                                    screen.blit(I_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'j'):
                                    screen.blit(J_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'k'):
                                    screen.blit(K_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'l'):
                                    screen.blit(L_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'm'):
                                    screen.blit(M_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'n'):
                                    screen.blit(N_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'o'):
                                    screen.blit(O_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'p'):
                                    screen.blit(P_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'r'):
                                    screen.blit(R_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 's'):
                                    screen.blit(S_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 't'):
                                    screen.blit(T_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'u'):
                                    screen.blit(U_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'w'):
                                    screen.blit(W_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'v'):
                                    screen.blit(V_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'x'):
                                    screen.blit(X_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'y'):
                                    screen.blit(Y_png, (820, 40 + 50 * i))
                                elif (lista_liter_bot[i] == 'z'):
                                    screen.blit(Z_png, (820, 40 + 50 * i))
                                elif (lista_liter_gracz[i] == 'q'):
                                    screen.blit(Q_png, (820, 40 + 50 * i))
                            if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_BACKSPACE:
                                    user_text=''
                                elif event.key==pygame.K_RETURN:
                                    nowa_litera_do_polozenia=user_text;
                                    i = nowa_litera_do_polozenia[2]
                                    if (i == 'a'):
                                        i = 0
                                    elif (i == 'b'):
                                        i = 1
                                    elif (i == 'c'):
                                        i = 2
                                    elif (i == 'd'):
                                        i = 3
                                    elif (i == 'e'):
                                        i = 4
                                    elif (i == 'f'):
                                        i = 5
                                    elif (i == 'g'):
                                        i = 6
                                    elif (i == 'h'):
                                        i = 7
                                    elif (i == 'i'):
                                        i = 8
                                    elif (i == 'j'):
                                        i = 9
                                    elif (i == 'k'):
                                        i = 10
                                    elif (i == 'l'):
                                        i = 11
                                    elif (i == 'm'):
                                        i = 12
                                    elif (i == 'n'):
                                        i = 13
                                    elif (i == 'o'):
                                        i = 14
                                    j = int(nowa_litera_do_polozenia[3])
                                    litera_do_polozenia_gracz = nowa_litera_do_polozenia[0]
                                    plansza[j][i]=litera_do_polozenia_gracz
                                    user_text=''
                                else:
                                    user_text+=event.unicode
                            #pygame.draw.rect(screen,color,input_rect,0)
                            #text_surface=base_font.render(user_text,True,(255,255,255))
                            #text_surface1=base_font1.render(podpowiedz,True,(0,0,0))
                            text_surface2 = base_font1.render(score1, True, (0, 0, 0))
                            text_surface3 = base_font1.render(score2, True, (0, 0, 0))
                            text_surface4 = base_font1.render(str(punkty_bota), True, (0, 0, 0))
                            text_surface5 = base_font1.render(str(punkty_gracza), True, (0, 0, 0))
                            #screen.blit(text_surface,(750,600))
                            #screen.blit(text_surface1,(650,570))
                            screen.blit(text_surface2,(700,480))
                            screen.blit(text_surface3,(700,520))
                            screen.blit(text_surface4,(830,480))
                            screen.blit(text_surface5,(830,520))
                            pygame.display.update()

                            if tura == 0:
                                punkty_gracza = tura_gracza(plansza, lista_liter_gracz, punkty_gracza, worek_z_literami)
                                tura = 1
                            else:
                                punkty_bota = tura_bota(plansza, lista_liter_bot, punkty_bota, worek_z_literami)
                                print("Punkty bota", punkty_bota)
                                tura = 0

                            if (event.type == pygame.QUIT):
                                running = False