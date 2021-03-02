import numpy as np

cena_jednostkowa = int(input('Wprowadź cenę jednostkową: '))
stopa_roczna = int(input('Wprowadź stopę magazynowania (roczną): '))
koszt_zlecenia = int(input('Wprowadź koszt zlecenia: '))
ilość_miesięcy = int(input('Ilość miesięcy, dla których obliczamy zapotrzebowanie: '))

zapotrzebowanie = []
decyzje = []
magazynowanie = stopa_roczna/12

for i in range(ilość_miesięcy):
    print('Zapotrzebowanie na miesiąc ', i+1)
    miesiąc = int(input(''))
    zapotrzebowanie.append(miesiąc)
    decyzje.append(0)


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
            cij[i][j] = poprzedni
        else:
            cij[i][j] = poprzedni + cena_jednostkowa * zapotrzebowanie[j] * (magazynowanie*m/100)
            m = m + 1
        poprzedni = cij[i][j]
    
print('')
print('')

print(cij)
minimum = []    
k = ilość_miesięcy - 1

while k > 0:
    for i in range(ilość_miesięcy):
        if cij[i][k] != 0:
            minimum.append(cij[i][k])
        
        
    minimalny = min(minimum)
    pozycjax, pozycjay = np.where(cij == minimalny)
    pozycjax = int(pozycjax)
    pozycjay = int(pozycjay)

    minimum = []
    decyzja = 0
    while cij[pozycjax][pozycjay] != 0 and pozycjax >= 0 and pozycjay >=0:
        decyzja = decyzja + cij[pozycjax][pozycjay]
        pozycjay -= 1

    decyzje[pozycjax] = int(decyzja)

    k = pozycjay


print('')    
for i in range(len(decyzje)):
    print('Miesiąc', i + 1, ' = ',decyzje[i], 'szt.')
