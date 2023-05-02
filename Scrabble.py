import random
import time
import numpy as np
import main
from copy import deepcopy
import copy
from datetime import datetime

import nltk
import enchant
from nltk.corpus import words

nltk.download('words')
random.seed(time.process_time())

class Scrable:

    def wylosuj_litery_start(self):
        worek_z_literami = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'e',
                            'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'f', 'f', 'g', 'g', 'g', 'h', 'h',
                            'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'j', 'k', 'l', 'l', 'l', 'l', 'm', 'm', 'n',
                            'n', 'n', 'n', 'n', 'n', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'p', 'p', 'q', 'r', 'r',
                            'r', 'r', 'r', 'r', 's', 's', 's', 's', 't', 't', 't', 't', 't', 't', 'u', 'u', 'u', 'u',
                            'v', 'v', 'w', 'w', 'x', 'y', 'y', 'z']
        litery = []
        for i in range(35):
            litery.append(main.losowanie_litery(worek_z_literami))

        return litery

    def __init__(self):
        self.plansza = [['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-'],
                        ['-', '-', '-', '-', '-', '-', '-']]  # plansza pusta 7x7
        self.multiplikatory = [[7, 1, 2, 3, 2, 1, 7],
                               [1, 6, 1, 1, 1, 6, 1],
                               [2, 1, 6, 1, 6, 1, 2],
                               [3, 1, 1, 6, 1, 1, 3],
                               [2, 1, 6, 1, 6, 1, 2],
                               [1, 6, 1, 1, 1, 6, 1],
                               [7, 1, 2, 3, 2, 1, 7]]  # multiplikatory planszy
        # self.litery = losujLitery(25)

        self.slowa = enchant.Dict("en_US")  # angielski słownik
        self.litery = self.wylosuj_litery_start() # wylosowane litery (26)
        self.punktacja = {
            'q': 10,
            'w': 4,
            'e': 1,
            'r': 1,
            't': 1,
            'y': 4,
            'u': 1,
            'i': 3,
            'o': 1,
            'p': 3,
            'a': 1,
            's': 1,
            'd': 2,
            'f': 4,
            'g': 2,
            'h': 4,
            'j': 8,
            'k': 5,
            'l': 1,
            'z': 10,
            'x': 8,
            'c': 3,
            'v': 4,
            'b': 3,
            'n': 1,
            'm': 3,
        }

    def split(self, word):
        return [char for char in word]

    def zliczPkt(self, plansza):
        punkty = 0

        planszatest = [['-' for x in range(len(plansza) + 1)] for y in range(len(plansza) + 1)]
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                planszatest[i][j] = plansza[i][j]

        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                if planszatest[i][j] != '-':
                    if planszatest[i + 1][j] != '-' and planszatest[i - 1][j] == '-':   #znaleziono słowo
                        multiplikator = 1
                        punktySlowo = 0
                        o = i
                        while planszatest[o][j] != '-' and o < len(plansza):
                            if self.multiplikatory[o][j] == 1:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                            if self.multiplikatory[o][j] == 2:
                                punktySlowo = punktySlowo + (2*self.punktacja[planszatest[o][j]])
                            if self.multiplikatory[o][j] == 3:
                                punktySlowo = punktySlowo + (3*self.punktacja[planszatest[o][j]])
                            if self.multiplikatory[o][j] == 6:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                                multiplikator = multiplikator * 2
                            if self.multiplikatory[o][j] == 7:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                                multiplikator = multiplikator * 3
                            o = o + 1
                        punktySlowo = punktySlowo * multiplikator
                        punkty = punkty + punktySlowo
                    if planszatest[i][j + 1] != '-' and planszatest[i][j - 1] == '-':   #znaleziono słowo
                        multiplikator = 1
                        punktySlowo = 0
                        o = j
                        while planszatest[i][o] != '-' and o < len(plansza):
                            if self.multiplikatory[i][o] == 1:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                            if self.multiplikatory[i][o] == 2:
                                punktySlowo = punktySlowo + (2*self.punktacja[planszatest[i][o]])
                            if self.multiplikatory[i][o] == 3:
                                punktySlowo = punktySlowo + (3*self.punktacja[planszatest[i][o]])
                            if self.multiplikatory[i][o] == 6:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                                multiplikator = multiplikator * 2
                            if self.multiplikatory[o][j] == 7:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                                multiplikator = multiplikator * 3
                            o = o + 1
                        punktySlowo = punktySlowo * multiplikator
                        punkty = punkty + punktySlowo
        return punkty



    def usunNieSlowa(self, plansza):
        czescSlowa = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], ]  # plansza pusta 7x7
        planszatest = [['-' for x in range(len(plansza) + 1)] for y in range(len(plansza) + 1)]
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                planszatest[i][j] = plansza[i][j]

        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                if planszatest[i][j] != '-':
                    if planszatest[i + 1][j] != '-' and planszatest[i - 1][j] == '-':
                        sprawdzane = ''
                        o = i
                        while planszatest[o][j] != '-' and o < len(plansza):
                            czescSlowa[o][j] = 1
                            o = o + 1

                    if planszatest[i][j + 1] != '-' and planszatest[i][j - 1] == '-':
                        sprawdzane = ''
                        o = j
                        while planszatest[i][o] != '-' and o < len(plansza):
                            czescSlowa[i][o] = 1
                            o = o + 1
        planszaCP=plansza.copy()
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                if czescSlowa[i][j] == 0:
                    planszaCP[i][j] = '-'
        return planszaCP


    def oblicz_ile_slow(self, plansza):
        planszatest = [['-' for x in range(len(plansza) + 1)] for y in range(len(plansza) + 1)]
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                planszatest[i][j] = plansza[i][j]
        slowa1 = 0
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                if planszatest[i][j] != '-':
                    if planszatest[i + 1][j] != '-' and planszatest[i - 1][j] == '-':
                        sprawdzane = ''
                        o = i
                        while planszatest[o][j] != '-' and o < len(plansza):
                            sprawdzane = sprawdzane + planszatest[o][j]
                            o = o + 1
                        if self.slowa.check(sprawdzane):
                            slowa1 = slowa1 + 1

                    if planszatest[i][j + 1] != '-' and planszatest[i][j - 1] == '-':
                        sprawdzane = ''
                        o = j
                        while planszatest[i][o] != '-' and o < len(plansza):
                            sprawdzane = sprawdzane + planszatest[i][o]
                            o = o + 1

                        if self.slowa.check(sprawdzane):
                            slowa1 = slowa1 + 1
        return slowa1

    def losowanie_planszy(self, litery):
        plansza = [['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-']]
        literki = litery.copy()
        planszaprzedruchem = plansza.copy()
        planszaporuchu = plansza.copy()
        ileslow = 0
        while len(literki) != 0:
            dorzucono = False
            for i in range(0, len(plansza)):  # czy mogę dorzucić słowo
                for j in range(0, len(plansza)):
                    if planszaporuchu[i][j] == '-':  # sprawdzam dla każdego pola czy moge dorzucić slowo
                        pion = False
                        poziom = False
                        if i > 0 and i < len(plansza) - 1:
                            if planszaporuchu[i - 1][j] != '-' or planszaporuchu[i + 1][j] != '-':
                                poziom = True
                        if i==0 and planszaporuchu[i+1][j] != '-':
                            poziom = True
                        if i== len(plansza)-1 and planszaporuchu[i-1][j] != '-':
                            poziom = True

                        if j > 0 and j < len(plansza) - 1:
                            if planszaporuchu[i][j - 1] != '-' or planszaporuchu[i][j + 1] != '-':
                                pion = True
                        if j == 0 and planszaporuchu[i][j+1] != '-':
                            pion = True
                        if j == len(plansza) - 1 and planszaporuchu[i][j-1] != '-':
                            pion = True
                        if poziom == True and pion == True:
                            break


                        for l in range(0, len(literki)):

                            planszaporuchu[i][j] = literki[l]



                            if self.oblicz_ile_slow(planszaporuchu) > ileslow:  # dorzucamy słowo
                                planszaprzedruchem = planszaporuchu.copy()
                                literki.remove(literki[l])
                                dorzucono = True
                                ileslow = ileslow + 1
                                break
                            else:
                                planszaporuchu[i][j] = '-'

                            planszaporuchu = planszaprzedruchem.copy()
            if not dorzucono:
                for i in range(1, len(plansza) - 1):
                    for j in range(1, len(plansza) - 1):
                        if planszaporuchu[i][j] == '-' and planszaporuchu[i - 1][j] == '-' and planszaporuchu[i + 1][
                            j] == '-' and planszaporuchu[i][j - 1] == '-' and planszaporuchu[i][j + 1] == '-':
                            if len(literki) != 0:
                                r = random.randint(0, len(literki) - 1)
                                planszaporuchu[i][j] = literki[r]
                                planszaprzedruchem = planszaporuchu.copy()
                                literki.remove(literki[r])
                                dorzucono = True
            if not dorzucono:
                break
        planszaprzedruchem = self.usunNieSlowa(planszaprzedruchem)
        return planszaprzedruchem

    def losowanie_populacji_poczatkowej(self):
        plansza = [['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-'],
                   ['-', '-', '-', '-', '-', '-', '-']]
        # litery = losujLitery(25)
        pojemnosc_populacji = 100
        populacja = []
        for i in range(0, pojemnosc_populacji):
            populacja.append(self.losowanie_planszy(self.litery))
        #print(populacja)
        return populacja
        # Losowanie pierwszej populacji (100 różnych plansz, złożonych ze słów 2 literowych)

    def selekcja(self, populacja, pojemnosc_populacji):
        #fitness = []
        #for i in range(0,pojemnosc_populacji):
         #   fitness.append(self.zliczPkt(populacja(i)))
        population_fitness = {}
        for i in range(0, pojemnosc_populacji):
            population_fitness[i]=self.zliczPkt(tuple(populacja[i]))
        probability = {}
        sum_fitness = 0
        for i in range(0, pojemnosc_populacji):
            sum_fitness = sum(population_fitness)
        probability_previous = 0

        for key,value in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True):
            probability[key]=probability_previous + value/sum_fitness
            probability_previous = probability[key]

        selekcja = []

        n = 0
        for key, value in sorted(population_fitness.items(), key=lambda item: item[1], reverse=True):
            if n >= 15:
                break
            selekcja.append(populacja[key])
            n += 1
        #print("elita")
        #for i in range (0,len(selekcja)):
        #    print(self.zliczPkt(selekcja[i]))
        #print("nie elita")
        for i in range (0, pojemnosc_populacji-15):
            for key, value in probability.items():
                rand = np.random.random()
                if rand <= value:
                    #print(self.zliczPkt(populacja[key]))
                    selekcja.append(populacja[key])
                    break
        return selekcja

    def najlepsze_slowo(self, plansza, ktore):

        planszatest = [['-' for x in range(len(plansza) + 1)] for y in range(len(plansza) + 1)]
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                planszatest[i][j] = plansza[i][j]
        slowa = {}
        for i in range(0, len(plansza)):
            for j in range(0, len(plansza)):
                if planszatest[i][j] != '-':
                    if planszatest[i + 1][j] != '-' and planszatest[i - 1][j] == '-':  # znaleziono słowo
                        sprawdzane = ''
                        multiplikator = 1
                        punktySlowo = 0
                        jSlowa = j
                        poczSlowa = i
                        o = i
                        while planszatest[o][j] != '-' and o < len(plansza):
                            if self.multiplikatory[o][j] == 1:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                            if self.multiplikatory[o][j] == 2:
                                punktySlowo = punktySlowo + (2 * self.punktacja[planszatest[o][j]])
                            if self.multiplikatory[o][j] == 5:
                                punktySlowo = punktySlowo + (5 * self.punktacja[planszatest[o][j]])
                            if self.multiplikatory[o][j] == 6:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                                multiplikator = multiplikator * 2
                            if self.multiplikatory[o][j] == 7:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[o][j]]
                                multiplikator = multiplikator * 5
                            koniecSlowa = o
                            sprawdzane = sprawdzane + planszatest[o][j]
                            o = o + 1
                        punktySlowo = punktySlowo * multiplikator
                        slowa[(poczSlowa, koniecSlowa, jSlowa, "j", sprawdzane)] = punktySlowo
                    if planszatest[i][j + 1] != '-' and planszatest[i][j - 1] == '-':  # znaleziono słowo
                        sprawdzane = ''
                        multiplikator = 1
                        punktySlowo = 0
                        o = j
                        iSlowa = i
                        poczSlowa = j
                        while planszatest[i][o] != '-' and o < len(plansza):
                            if self.multiplikatory[i][o] == 1:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                            if self.multiplikatory[i][o] == 2:
                                punktySlowo = punktySlowo + (2 * self.punktacja[planszatest[i][o]])
                            if self.multiplikatory[i][o] == 5:
                                punktySlowo = punktySlowo + (5 * self.punktacja[planszatest[i][o]])
                            if self.multiplikatory[i][o] == 6:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                                multiplikator = multiplikator * 2
                            if self.multiplikatory[o][j] == 7:
                                punktySlowo = punktySlowo + self.punktacja[planszatest[i][o]]
                                multiplikator = multiplikator * 5
                            koniecSlowa = o
                            sprawdzane = sprawdzane + planszatest[i][o]
                            o = o + 1
                        punktySlowo = punktySlowo * multiplikator
                        slowa[(poczSlowa, koniecSlowa, iSlowa, "i", sprawdzane)] = punktySlowo

        posortowane = sorted(slowa.items(),reverse=True, key=lambda item: item[1])


        if ktore >= len(slowa):
            #print(ktore)
            #print(len(slowa))
            #print(slowa)
            #print(len(list(posortowane)))
            #print(list(posortowane))
            return list(posortowane)[ktore-1]
        #print(posortowane)
        return list(posortowane)[ktore]

    def nachodzenie(self, slw1, slw2, litery):
        lit = litery.copy()
        slowo1 = slw1[0]
        slowo2 = slw2[0]
        pol1 = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], ]

        pol2 = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0], ]

        if slowo1[3] == "i":
            for j in range(slowo1[0],slowo1[1]+1):
                pol1[slowo1[2]][j] = 1
        if slowo1[3] == "j":
            for i in range(slowo1[0],slowo1[1]+1):
                pol1[i][slowo1[2]] = 1

        if slowo2[3] == "i":
            for j in range(slowo2[0],slowo2[1]+1):
                pol2[slowo2[2]][j] = 1
        if slowo2[3] == "j":
            for i in range(slowo2[0],slowo2[1]+1):
                pol2[i][slowo2[2]] = 1

        for i in range(0, len(pol1)):                           #nachodza sie
            for j in range(0, len(pol1)):
                if pol1[i][j] == 1 and pol2[i][j] == 1:
                    return True

        t1 = slowo1[4]
        t2 = slowo2[4]
        tresc1 = self.split(t1)
        tresc2 = self.split(t2)

        for letter in tresc1:
            lit.remove(letter)

        for letter in tresc2:
            if letter not in lit:
                return True

        return False

    def delsam(self, plansza):
        for i in range(1,7):
            for j in range(1,7):
                if plansza[i][j] != '-' and plansza[i+1][j] == '-' and plansza[i-1][j] == '-' and plansza[i][j+1] == '-' and plansza[i][j-1] == '-':
                    plansza[i][j]='-'

    def wygeneruj_dziecko(self, parent1, parent2, litery):
        lit = litery.copy()
        child = [['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-']]

        slw1 = self.najlepsze_slowo(parent1, 0)
        #print(slw1)
        slw2 = self.najlepsze_slowo(parent2, 0)
        i = 0
        p = 0
        while self.nachodzenie(slw1, slw2, litery) == True:
            i = i + 1
            if i>=self.oblicz_ile_slow(parent2):
                i=0
                p=p+1
                slw1 = self.najlepsze_slowo(parent1, p)
            slw2 = self.najlepsze_slowo(parent2, i)

        slowo1 = slw1[0]
        slowo2 = slw2[0]
        t1 = slowo1[4]
        t2 = slowo2[4]
        tresc1 = self.split(t1)
        tresc2 = self.split(t2)
        licznik1 = 0
        licznik2 = 0

        if slowo1[3] == "i":
            for j in range(slowo1[0], slowo1[1] + 1):
                child[slowo1[2]][j] = tresc1[licznik1]
                licznik1 = licznik1 + 1
        if slowo1[3] == "j":
            for i in range(slowo1[0], slowo1[1] + 1):
                child[i][slowo1[2]] = tresc1[licznik1]
                licznik1 = licznik1 + 1

        if slowo2[3] == "i":
            for j in range(slowo2[0], slowo2[1] + 1):
                child[slowo2[2]][j] = tresc2[licznik2]
                licznik2 = licznik2 + 1
        if slowo2[3] == "j":
            for i in range(slowo2[0], slowo2[1] + 1):
                child[i][slowo2[2]] = tresc2[licznik2]
                licznik2 = licznik2 + 1  # ułożenie dwóch najlepszych słów rodziców na plansze (nie nachodzących się)

        for litera in tresc1:
            lit.remove(litera)
        for litera in tresc2:
            lit.remove(litera)  # usuwanie użytych liter

        litBackup = lit.copy()
        losowe = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], ]

        for l in range(0,int(len(lit)/2)):
            randomletter = lit[random.randint(0,int(len(lit)/2))]
            randi = random.randint(0,len(child)-1)
            randj = random.randint(0,len(child)-1)

            if child[randi][randj] == '-':
                child[randi][randj] = randomletter
                losowe[randi][randj] = 1
                lit.remove(randomletter)

        planszaprzedruchem = copy.deepcopy(child)
        planszaporuchu = copy.deepcopy(child)

        for i in range(0, len(child)):  # czy mogę dorzucić słowo
            for j in range(0, len(child)):
                if planszaporuchu[i][j] == '-':  # sprawdzam dla każdego pola czy moge dorzucić slowo
                    pion = False
                    poziom = False
                    if i > 0 and i < len(child) - 1:
                        if planszaporuchu[i - 1][j] != '-' or planszaporuchu[i + 1][j] != '-':
                            poziom = True
                    if i == 0 and planszaporuchu[i + 1][j] != '-':
                        poziom = True
                    if i == len(child) - 1 and planszaporuchu[i - 1][j] != '-':
                        poziom = True

                    if j > 0 and j < len(child) - 1:
                        if planszaporuchu[i][j - 1] != '-' or planszaporuchu[i][j + 1] != '-':
                            pion = True
                    if j == 0 and planszaporuchu[i][j + 1] != '-':
                        pion = True
                    if j == len(child) - 1 and planszaporuchu[i][j - 1] != '-':
                        pion = True
                    if poziom == True and pion == True:
                        break

                    for l in range(0, len(lit)):
                        wczesniej = self.oblicz_ile_slow(planszaporuchu)
                        planszaporuchu[i][j] = lit[l]

                        if self.oblicz_ile_slow(planszaporuchu) > wczesniej:  # dorzucamy słowo
                            #print("dokladam")
                            if poziom == True:
                                if j != 0:
                                    losowe[i][j - 1] = 0
                                if j != len(planszaprzedruchem) - 1:  # może nie -1
                                    losowe[i][j + 1] = 0
                            if pion == True:
                                if i!= 0:
                                    losowe[i-1][j] = 0
                                if i!= len(planszaprzedruchem)-1:       #może nie -1
                                    losowe[i+1][j]=0


                            planszaprzedruchem = planszaporuchu.copy()
                            lit.remove(lit[l])
                            break
                        else:
                            planszaporuchu[i][j] = '-'

                        planszaporuchu = planszaprzedruchem.copy()

        for i in range(0,len(planszaporuchu)):
            for j in range(0,len(planszaporuchu)):
                if losowe[i][j] == 1:
                    planszaporuchu[i][j] = '-'

        return planszaporuchu







    def krzyzowanie(self,populacja, pojemnosc_populacji):
        children = []
        #print("poprzednia elita")
        for i in range(0,15):
            children.append(populacja[i])
            #print(self.zliczPkt(populacja[i]))

        for i in range(0, pojemnosc_populacji-15):
            parent1 = np.random.randint(0, 99)
            parent2 = np.random.randint(0, 99)
            p1 = populacja[parent1]
            p2 = populacja[parent2]
            child = self.wygeneruj_dziecko(p1,p2,self.litery)
            children.append(child)

        return children


    def znajdz_najlepszy_wynik(self, populacja):
        best = 0
        for i in range(0,100):
            wynik = self.zliczPkt(populacja[i])
            if wynik > best:
                best = wynik
        return best

    def znajdz_najlepsza_plansze(self, populacja):
        best = 0
        for i in range(0,100):
            wynik = self.zliczPkt(populacja[i])
            if wynik > best:
                best = wynik
                bestpop = populacja[i]
        return bestpop

