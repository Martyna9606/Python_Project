import sys
import matplotlib.pyplot as plt
import random
from matplotlib.widgets import Button


def dane():
    while(True):
        try:
            global ilość_zadań
            ilość_zadań = int(input('Podaj ilość zadań:'))
            if ilość_zadań > 0:
                break
            else:
                print('Proszę podać wartość większą od zera')
                continue
        except:
            print('Proszę wprowadzić liczbę całkowitą!')
            continue
    global z
    z = []
    for i in range(ilość_zadań):
        z.append('Z' + format(i+1))
    print(z)

        
def zadania():
    global m1
    global m2 
    m1 = []
    m2 = []
    h = 0
    
    while(True):
        try:
            for i in range(len(z)):
                rbh = int(input('Podaj Z' + format(i+1) + ' dla M1:' ))
                m1.append(rbh)
                rbh = int(input('Podaj Z' + format(i+1) + ' dla M2:' ))
                m2.append(rbh)
                print('')
            break
        except:
            print('Proszę wprowadzać wartości całkowitoliczbowe!')
            continue
    print('   ', 'M1', 'M2')
    for i in range(len(m1)):
        print(z[i],'',m1[i], '', m2[i])


def uszeregowanie():
    global m11
    global m22
    global s1
    global s2
    global s
    global z1
    s1 = []
    s2 = []
    

    m11 = m1.copy()
    m22 = m2.copy()
    z1 = z.copy()

    while(len(m11)>0):
        min1 = min(m11)
        min2 = min(m22)
        if min1 <= min2:
            s1.append(z1[m11.index(min1)])
            del z1[m11.index(min1)]
            del m22[m11.index(min1)]
            del m11[m11.index(min1)]
        else:
            s2.insert(0, (z1[m22.index(min2)]))
            del z1[m22.index(min2)]
            del m11[m22.index(min2)]
            del m22[m22.index(min2)]
            
        
    s = s1 + s2
    print('Uporządkowana lista zadań: ', s)

def lista_zadań():
    global maszyna1
    global maszyna2

    maszyna1 = []
    maszyna2 = []

    for i in s:
        maszyna1.append(m1[z.index(i)])
        maszyna2.append(m2[z.index(i)])


def czas_pracy():
    global d1
    global d2
    d1 = 0
    d2 = 0
    V1 = []
    V2 = []
    

    for i in range(len(maszyna1)):
        d1 = d1 + maszyna1[i]
        item = (d1 - maszyna1[i], d1)
        V1.append(item)
        if d1 > d2:
            d2 = d1 + maszyna2[i]
            item = (d2 - maszyna2[i], d2)
            V2.append(item)
        else:
            d2 = d2 + maszyna2[i]
            item = (d2 - maszyna2[i], d2)
            V2.append(item)
    print('Długość procesu wyniesie: ', d2, ' rbh.')
    print('Wyższa Szkoła Bankowa we Wrocławiu - Abram Martyna 62508.')
    print('')


    number_of_colors = len(V1)

    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
    for i in range(len(V1)):

        c1 = random.choice(colors)
        
        plt.plot([V1[i][0], V1[i][1]], [1,1], c=colors[i], marker = 'o', label = s[i])
        plt.plot([V2[i][0], V2[i][1]], [2,2], c=colors[i],  marker = 'o')
        plt.legend()

    plt.xticks(range(0, d2+2))
    plt.yticks([1, 2], ['M1', 'M2'])
    plt.title('Wyższa Szkoła Bankowa - Abram Martyna 62508')
    plt.xlabel('Rbh')
    plt.grid()
    plt.figtext(.2, .6, ('M1: ', m1))
    plt.figtext(.2, .5, ('M2: ',m2))
    plt.figtext(.2, .7, ('Wprowadzone zadania:', z))
    plt.figtext(.2, .4, ('Uporządkowane zadania: ', s))
    plt.figtext(.2, .3, ('Czas trwania procesu: ', d2, 'rbh'))
    plt.show()
    plt.close()
        

def main():
    while(True):
        print('Co chcesz zrobić?')
        print('1. Wprowadź dane.')
        print('2. Koniec')
        try:
            c = int(input('Podaj liczbę 1 lub 2:'))

            if c == 1:
                print('Liczymy')
                dane()
                zadania()
                uszeregowanie()
                lista_zadań()
                czas_pracy()
                break
                sys.exit
            elif c == 2:
                print('Koniec')
                break
                sys.exit
        except:
            print('Proszę podać wartośc 1 lub 2')
            continue
            
            
        
main()
        
    
