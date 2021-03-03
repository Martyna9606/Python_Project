import numpy as np
import sys

def liczymy():
    while(True):
        
        try:
            cena_jednostkowa = int(input('Wprowadź cenę jednostkową: '))
            stopa_roczna = int(input('Wprowadź stopę magazynowania (roczną): '))
            koszt_zlecenia = int(input('Wprowadź koszt zlecenia: '))
            ilość_miesięcy = int(input('Ilość miesięcy, dla których obliczamy zapotrzebowanie: '))
            
            if cena_jednostkowa<=0 or stopa_roczna<=0 or koszt_zlecenia<=0 or ilość_miesięcy<=0:
                print('Nie podajemy wartości zerowych! ')
                continue
            break
        except:
            print('Proszę wprowadzić liczbę całkowitą :)! ')
            continue

    zapotrzebowanie = []
    decyzje = []
    magazynowanie = stopa_roczna/12
    w = 0
    while(w < ilość_miesięcy):
        for i in range(ilość_miesięcy):
            try:
                print('Zapotrzebowanie na miesiąc ', i+1)
                miesiąc = int(input(''))            
            except:
                print('Proszę wprowadzić liczby całkowite :)!')
                continue
            if miesiąc < 0:
                    break
            else:
                zapotrzebowanie.append(miesiąc)
                decyzje.append(0)
                w = w+1



    cij = np.zeros(ilość_miesięcy**2).reshape(ilość_miesięcy, ilość_miesięcy)


    for i in range(ilość_miesięcy):
        if i == 0:
            poprzedni = koszt_zlecenia
        else:
            minimum = []
            for n in range(0, i):
                minimum.append(cij[n][i-1])
            poprzedni = koszt_zlecenia + (min(minimum))
        m = 1
        for j in range(i, ilość_miesięcy):
            if i == j :
                cij[i][j] = round(poprzedni)
            else:
                cij[i][j] = round(poprzedni + cena_jednostkowa * zapotrzebowanie[j] * (magazynowanie*m/100))
                m = m + 1
            poprzedni = cij[i][j]
        
    print('')
    print('')

    print(cij)
    minimum = []    
    k = ilość_miesięcy - 1

    while k >= 0:
        for i in range(ilość_miesięcy):
            if cij[i][k] != 0:
                minimum.append(cij[i][k])

        minimalny = min(minimum)
        for m in range(ilość_miesięcy):
            if cij[m][k] == minimalny:
                pozycjax = m
                pozycjay = k
        pozycjax = int(pozycjax)
        pozycjay = int(pozycjay)

        minimum = []
        decyzja = 0
        while cij[pozycjax][pozycjay] != 0 and pozycjax >= 0 and pozycjay >=0:
            decyzja = decyzja + zapotrzebowanie[pozycjay]
            pozycjay -= 1

        decyzje[pozycjax] = int(decyzja)

        k = pozycjay


    print('')    
    for i in range(len(decyzje)):
        print('Miesiąc', i + 1, ' = ',decyzje[i], 'szt.')

    print('')
    print('Wyższa Szkoła Bankowa we Wrocławiu - Abram Martyna - 62508')

def menu():
    while(True):
        print('Algorytm Withina Wagnera - Abram Martyna 62508')
        print('Co chcesz zrobić? ')
        print('1. Wprowadź dane.')
        print('2. Koniec')
        try:
            dec = int(input('1/2?'))
            print(dec)
            if dec == 1:
                print('Liczymy!')
                liczymy()
                
            elif dec == 2:
                break
                sys.exit
        except:
            print('Proszę wybrać wartość 1 lub 2.')
            continue

menu()
        
