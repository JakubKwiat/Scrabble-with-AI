import random
import enchant
import sys

def losowanie_litery(worek_z_literami):
    ilosc_liter_w_worku = len(worek_z_literami)
    x = random.randint(0, ilosc_liter_w_worku - 1)
    wylosowana_litera = worek_z_literami[x]
    worek_z_literami.pop(x)
    return wylosowana_litera

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
def dobieranie_7_liter_na_start(worek_z_literami, lista_liter_gracz):
    for i in range(7):
        lista_liter_gracz.append(losowanie_litery(worek_z_literami))
    return lista_liter_gracz

def dobieranie_liter(worek_z_literami,lista_liter_gracz):
    ilosc_liter_do_wylosowania = 7 - len(lista_liter_gracz)
    for i in range(ilosc_liter_do_wylosowania):
        lista_liter_gracz.append(losowanie_litery(worek_z_literami))
    return lista_liter_gracz

def odrzucenie_losowych(worek_z_literami,lista_liter_gracz):
    lista_liter_do_odrzucenia=[]
    ilosc_liter_do_odrzucenia = random.randint(1, 7)
    for i in range(ilosc_liter_do_odrzucenia):
        litera_do_odrzucenia = lista_liter_gracz[random.randint(0, len(lista_liter_gracz) - 1)]
        lista_liter_do_odrzucenia.append(litera_do_odrzucenia)
        lista_liter_gracz.remove(litera_do_odrzucenia)
    ilosc_liter_do_wylosowania=ilosc_liter_do_odrzucenia
    for i in range(ilosc_liter_do_wylosowania):
        lista_liter_gracz.append(losowanie_litery(worek_z_literami))
    for i in range(ilosc_liter_do_odrzucenia):
        worek_z_literami.append(lista_liter_do_odrzucenia[i])
    return lista_liter_gracz

def punktacja_slow(slowo):
    punkty_za_litery = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                        'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                        'y': 4, 'z': 10}
    punkty = 0
    for litera in slowo:
        punkty += punkty_za_litery[litera]
    return punkty

def generowanie_slow(litery):
    slownik = enchant.Dict("en_US")
    dwu_literowe = []
    for i in range(len(litery)):
        for j in range(len(litery)):
            wyraz = litery[i] + litery[j]
            if i != j and wyraz not in dwu_literowe and slownik.check(wyraz):
                dwu_literowe.append(wyraz)

    # print(len(dwu_literowe))
    # for wyraz in dwu_literowe:
    #     print(wyraz, end=' ')
    # print()

    trzy_literowe = []
    for i in range(len(litery)):
        for j in range(len(litery)):
            for k in range(len(litery)):
                iterators = []
                iterators.append(i)
                if j in iterators:
                    continue
                iterators.append(j)
                if k in iterators:
                    continue
                wyraz = litery[i] + litery[j] + litery[k]
                if wyraz not in trzy_literowe and slownik.check(wyraz):
                    trzy_literowe.append(wyraz)

    # print(len(trzy_literowe))
    # for wyraz in trzy_literowe:
    #     print(wyraz, end=' ')
    # print()

    cztero_literowe = []
    for i in range(len(litery)):
        for j in range(len(litery)):
            for k in range(len(litery)):
                for l in range(len(litery)):
                    iterators = []
                    iterators.append(i)
                    if j in iterators:
                        continue
                    iterators.append(j)
                    if k in iterators:
                        continue
                    iterators.append(k)
                    if l in iterators:
                        continue
                    wyraz = litery[i] + litery[j] + litery[k] + litery[l]
                    if wyraz not in cztero_literowe and slownik.check(wyraz):
                        cztero_literowe.append(wyraz)

    # print(len(cztero_literowe))
    # for wyraz in cztero_literowe:
    #     print(wyraz, end=' ')
    # print()

    piecio_literowe = []
    for i in range(len(litery)):
        for j in range(len(litery)):
            for k in range(len(litery)):
                for l in range(len(litery)):
                    for m in range(len(litery)):
                        iterators = []
                        iterators.append(i)
                        if j in iterators:
                            continue
                        iterators.append(j)
                        if k in iterators:
                            continue
                        iterators.append(k)
                        if l in iterators:
                            continue
                        iterators.append(l)
                        if m in iterators:
                            continue
                        wyraz = litery[i] + litery[j] + litery[k] + litery[l] + litery[m]
                        if wyraz not in piecio_literowe and slownik.check(wyraz):
                            piecio_literowe.append(wyraz)

    # print(len(piecio_literowe))
    # for wyraz in piecio_literowe:
    #     print(wyraz, end=' ')
    # print()

    szescio_literowe = []
    for i in range(len(litery)):
        for j in range(len(litery)):
            for k in range(len(litery)):
                for l in range(len(litery)):
                    for m in range(len(litery)):
                        for n in range(len(litery)):
                            iterators = []
                            iterators.append(i)
                            if j in iterators:
                                continue
                            iterators.append(j)
                            if k in iterators:
                                continue
                            iterators.append(k)
                            if l in iterators:
                                continue
                            iterators.append(l)
                            if m in iterators:
                                continue
                            iterators.append(m)
                            if n in iterators:
                                continue
                            wyraz = litery[i] + litery[j] + litery[k] + litery[l] + litery[m] + litery[n]
                            if wyraz not in szescio_literowe and slownik.check(wyraz):
                                szescio_literowe.append(wyraz)

    # print(len(szescio_literowe))
    # for wyraz in szescio_literowe:
    #     print(wyraz, end=' ')
    # print()

    siedmio_literowe = []
    # for i in range(len(litery)):
    #     for j in range(len(litery)):
    #         for k in range(len(litery)):
    #             for l in range(len(litery)):
    #                 for m in range(len(litery)):
    #                     for n in range(len(litery)):
    #                         for o in range(len(litery)):
    #                             iterators = []
    #                             iterators.append(i)
    #                             if j in iterators:
    #                                 continue
    #                             iterators.append(j)
    #                             if k in iterators:
    #                                 continue
    #                             iterators.append(k)
    #                             if l in iterators:
    #                                 continue
    #                             iterators.append(l)
    #                             if m in iterators:
    #                                 continue
    #                             iterators.append(m)
    #                             if n in iterators:
    #                                 continue
    #                             iterators.append(n)
    #                             if o in iterators:
    #                                 continue
    #                             wyraz = litery[i] + litery[j] + litery[k] + litery[l] + litery[m] + litery[n] + litery[
    #                                 o]
    #                             if wyraz not in siedmio_literowe and slownik.check(wyraz):
    #                                 siedmio_literowe.append(wyraz)

    # print(len(siedmio_literowe))
    # for wyraz in siedmio_literowe:
    #     print(wyraz, end=' ')
    # print()

    wyrazy = siedmio_literowe + szescio_literowe + piecio_literowe + cztero_literowe + trzy_literowe + dwu_literowe
    return wyrazy

def najlepsze_slowo(slowa):
    najlepsze = ""
    max = 0
    for slowo in slowa:
        punktacja = punktacja_slow(slowo)
        if punktacja > max:
            max = punktacja
            najlepsze = slowo
    return najlepsze

def odczyt_z_pliku(nazwa_pliku,wymiar_planszy_x,wymiar_planszy_y):
    f = open(nazwa_pliku)
    plansza_z_pliku = f.read()
    plansza_z_pliku = plansza_z_pliku.split('\n')
    plansza_z_pliku = [l.split(',') for l in plansza_z_pliku]
    f.close()
    # for i in range(wymiar_planszy_x):
    #     print()
    #     for j in range(wymiar_planszy_y):
    #         sys.stdout.write(str(plansza_z_pliku[i][j]))
    #         sys.stdout.write(' ')
    return plansza_z_pliku

def sprawdzenie_miejsca_na_slowo(plansza, poziom, pion, orientacja, slowo):
    flag = False
    for i in range(len(slowo)):
        if orientacja == 'pionowo':
            if poziom - 1 >= 0:
                if plansza[poziom - 1][pion] != '0' and \
                    plansza[poziom - 1][pion] != '3W' and \
                    plansza[poziom - 1][pion] != '2W' and \
                    plansza[poziom - 1][pion] != '3L' and \
                    plansza[poziom - 1][pion] != '2L':
                    return False
            if poziom + i >= len(plansza):
                return False
            pole = plansza[poziom + i][pion]
        elif orientacja == 'poziomo':
            if pion - 1 >= 0:
                if plansza[poziom][pion - 1] != '0' and \
                    plansza[poziom][pion - 1] != '3W' and \
                    plansza[poziom][pion - 1] != '2W' and \
                    plansza[poziom][pion - 1] != '3L' and \
                    plansza[poziom][pion - 1] != '2L':
                    return False
            if pion + i >= len(plansza):
                return False
            pole = plansza[poziom][pion + i]

        if (pole == slowo[i]) or (pole == '#'):
            flag = True
            continue
        if (pole == '0') or (pole == '3W') or (pole == '2W') or (pole == '3L') or (pole == '2L'):
            continue
        else:
            return False
    return flag

def sprawdzenie_punktacji_z_premiami(plansza, poziom, pion, orientacja, slowo):
    mnoznik = 1
    premie_za_literowe = 0
    for i in range(len(slowo)):
        if orientacja == 'pionowo':
            pole = plansza[poziom + i][pion]
        elif orientacja == 'poziomo':
            pole = plansza[poziom][pion + i]

        if pole == '3W':
            mnoznik *= 3;
        if pole == '2W':
            mnoznik *= 2;
        if pole == '3L':
            premie_za_literowe += punktacja_slow(slowo[i]) * 2 # 2*punkty + 1*punkty
        if pole == '2L':
            premie_za_literowe += punktacja_slow(slowo[i])     # 1*punkty + 1*punkty

    punktacja = (punktacja_slow(slowo) + premie_za_literowe) * mnoznik
    return punktacja

def ulozenie_slowa(plansza, poziom, pion, orientacja, slowo):
    for i in range(len(slowo)):
        if orientacja == 'pionowo':
            plansza[poziom + i][pion] = slowo[i]
        elif orientacja == 'poziomo':
            plansza[poziom][pion + i] = slowo[i]
    return plansza

def ulozenie_slowa_miejsce(plansza, miejsce, slowo):
    ulozenie_slowa(plansza, miejsce[0], miejsce[1], miejsce[2], slowo)

def plansza_w_konsoli(plansza):
    for i in range(len(plansza)):
        for j in range(len(plansza)):
            if (plansza[i][j] == '0'):
                print('_', end='  ') #  _ - puste
            elif (plansza[i][j] == '3W'):
                print('T', end='  ') # T - potrójna premia słowna
            elif (plansza[i][j] == '2W'):
                print('D', end='  ') # D - podwójna premia słowna
            elif (plansza[i][j] == '3L'):
                print('t', end='  ') # t - potrójna premia literowa
            elif (plansza[i][j] == '2L'):
                print('d', end='  ') # d - podwójna premia literowa
            elif (plansza[i][j] == '#'):
                print('#', end='  ') # # - start
            else:
                print(plansza[i][j], end='  ') # litery
        print(end='\n')

def szukanie_miejsc_na_slowo(plansza, slowo):
    miejsca = []
    for i in range(len(plansza)):
        for j in range(len(plansza)):
            if sprawdzenie_miejsca_na_slowo(plansza, i, j, 'poziomo', slowo):
                # print(i, j, 'poziomo')
                miejsca.append((i, j, 'poziomo'))
            if sprawdzenie_miejsca_na_slowo(plansza, i, j, 'pionowo', slowo):
                # print(i, j, 'pionowo')
                miejsca.append((i, j, 'pionowo'))
    return miejsca # [(poziom, pion, orientacja)]

def najlepsze_miejsce(plansza, slowo, miejsca):
    max = 0
    najlepsze = ()
    for miejsce in miejsca:
        poziom = miejsce[0]
        pion = miejsce[1]
        orientacja = miejsce[2]
        punktacja = sprawdzenie_punktacji_z_premiami(plansza, poziom, pion, orientacja, slowo)
        # print("punktacja", punktacja, miejsce)
        if punktacja > max:
            max = punktacja
            najlepsze = miejsce
    return (najlepsze, max)

def tura_bota(plansza, litery_bota, punkty_bota, worek_z_literami):
    najlepsze_slowa = []
    for i in range(len(plansza)):
        for j in range(len(plansza)):
            if plansza[i][j] != '0' and \
                    plansza[i][j] != '3W' and \
                    plansza[i][j] != '2W' and \
                    plansza[i][j] != '3L' and \
                    plansza[i][j] != '2L':
                print(plansza[i][j], litery_bota + list(plansza[i][j]))
                slowa = generowanie_slow(litery_bota + list(plansza[i][j]))
                najlepsze = najlepsze_slowo(slowa)
                if najlepsze not in najlepsze_slowa:
                    najlepsze_slowa.append(najlepsze)
                print(najlepsze, punktacja_slow(najlepsze))

    najlepsze_opcje = []
    for slowo in najlepsze_slowa:
        miejsca = szukanie_miejsc_na_slowo(plansza, slowo)
        print(slowo, najlepsze_miejsce(plansza, slowo, miejsca))
        najlepsze_opcje.append((slowo, najlepsze_miejsce(plansza, slowo, miejsca)))

    max = 0
    for opcja in najlepsze_opcje:
        if opcja[1][1] > max:
            max = opcja[1][1]
            najlepsza_opcja = opcja
    print(najlepsza_opcja)
    for litera in najlepsza_opcja[0]:
        if litera in litery_bota:
            litery_bota.remove(litera)
    dobieranie_liter(worek_z_literami, litery_bota)

    punkty_bota += najlepsza_opcja[1][1]
    if najlepsza_opcja[1][1] > 0:
        ulozenie_slowa_miejsce(plansza, najlepsza_opcja[1][0], najlepsza_opcja[0])
    else:
        odrzucenie_losowych(worek_z_literami, litery_bota)
        dobieranie_liter(worek_z_literami, litery_bota)

    return punkty_bota

def tura_gracza(plansza, litery_gracza, punkty_gracza, worek_z_literami):
    print("Punkty gracza", punkty_gracza)
    print("Litery gracza", litery_gracza)
    slowo = input("podaj slowo ")
    slownik = enchant.Dict("en_US")
    while (slownik.check(slowo) == 0):
        slowo = input("podaj slowo ")
    for litera in slowo:
        if litera not in litery_gracza:
            slowo = input("podaj slowo")
    orientacja = input("pionowo / poziomo ")
    if orientacja == "pionowo":
        orientacja = "poziomo"
    else:
        orientacja = "pionowo"
    poziom_litera = input("podaj poziom ")
    poziom = 0
    if poziom_litera == 'a':
        poziom = 0
    elif poziom_litera == 'b':
        poziom = 1
    elif poziom_litera == 'c':
        poziom = 2
    elif poziom_litera == 'd':
        poziom = 3
    elif poziom_litera == 'e':
        poziom = 4
    elif poziom_litera == 'f':
        poziom = 5
    elif poziom_litera == 'g':
        poziom = 6
    elif poziom_litera == 'h':
        poziom = 7
    elif poziom_litera == 'i':
        poziom = 8
    elif poziom_litera == 'j':
        poziom = 9
    elif poziom_litera == 'k':
        poziom = 10
    elif poziom_litera == 'l':
        poziom = 11
    elif poziom_litera == 'm':
        poziom = 12
    elif poziom_litera == 'n':
        poziom = 13
    elif poziom_litera == 'o':
        poziom = 14

    pion = int(input("podaj pion "))
    # punkty_gracza += sprawdzenie_punktacji_z_premiami(plansza, poziom, pion, orientacja, slowo)
    punkty_gracza += sprawdzenie_punktacji_z_premiami(plansza, pion, poziom, orientacja, slowo)
    # ulozenie_slowa(plansza, poziom, pion, orientacja, slowo)
    ulozenie_slowa(plansza, pion, poziom, orientacja, slowo)
    for litera in slowo:
        if litera in litery_gracza:
            litery_gracza.remove(litera)
    dobieranie_liter(worek_z_literami, litery_gracza)
    return punkty_gracza

if __name__ == '__main__':

    worek_z_literami = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'e', 'e',
                        'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'h', 'h', 'i', 'i',
                        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'l', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'n',
                        'n', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'q', 'r', 'r', 'r', 'r', 'r', 'r',
                        's', 's', 's', 's', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u', 'v', 'v', 'w', 'w', 'x',
                        'y', 'y', 'z']

    wymiar_planszy_x = wymiar_planszy_y = 15
    nazwa_pliku_do_odczytu = "plansza.txt"
    plansza = odczyt_z_pliku(nazwa_pliku_do_odczytu, wymiar_planszy_x, wymiar_planszy_y)
    plansza_w_konsoli(plansza)
    print()

    litery_bota = []
    punkty_bota = 0
    dobieranie_7_liter_na_start(worek_z_literami, litery_bota)

    litery_gracza = []
    punkty_gracza = 0
    dobieranie_7_liter_na_start(worek_z_literami, litery_gracza)

    ilosc_tur = 3
    for _ in range(ilosc_tur):
        punkty_gracza = tura_gracza(plansza, litery_gracza, punkty_gracza, worek_z_literami)
        plansza_w_konsoli(plansza)
        print("Punkty gracza", punkty_gracza)
        print("Litery gracza", litery_gracza)

        punkty_bota = tura_bota(plansza, litery_bota, punkty_bota, worek_z_literami)
        plansza_w_konsoli(plansza)
        print("Punkty bota", punkty_bota)
        print("Litery bota", litery_bota)

