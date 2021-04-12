import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import sys
from numpy import array



#funkcja sprawdzająca czy dana liczba, jest liczbą całkowitą większą od 0
def is_int(inputs):
    try:
        inputs = int(inputs)
        if inputs >= 0:
            return True
        else:
            return False

    except:
        return False


#klasa tworząca Graf
class make_graph:
    def __init__(self, node, node_list):
        self.node = node
        self.node_list = node_list
        self.G = nx.Graph()
        self.G.add_nodes_from(node_list)

    def edge(self):
        for i in range(len(self.node_list)-1):
            for j in range(i+1, len(self.node_list)):
                print('Waga z punktu', self.node_list[i])
                print('Do punktu', self.node_list[j])
                waga = int(input(''))
                self.G.add_edge(self.node_list[i], self.node_list[j], weight = waga)
   
                   

    def draw(self, T, D, w, l):
        self.T = T
        self.D = D
        self.w = w
        path = []
        for i in range(len(self.T)-1):
            point = (self.node_list[T[i]], self.node_list[T[i+1]])
            path.append(point)
        pos=nx.spring_layout(self.G)
        nx.draw_networkx(self.G,pos)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edges(self.G,pos,path, edge_color = 'r', width = 3, arrows = True, label = 'S')
        nx.draw_networkx_edge_labels(self.G,pos, edge_labels)
        sciezka = []
        for i in T:
            sciezka.append(self.node_list[i])
        if l == 2:
            Label_Text = 'Abram Martyna 62508 - Algorytm wyboru najbliższego sąsiada - Ścieżka: ' + str(sciezka) + ' Droga: ' + str(D)
        else:
            Label_Text = 'Abram Martyna 62508 - Algorytm sukcesywne dołączanie węzłów - Ścieżka: ' + str(sciezka) + ' Droga: ' + str(D)
        plt.xlabel(Label_Text)
        plt.show()

    def make_matrix(self):
        self.A = nx.to_numpy_matrix(self.G)
        return self.A
        
def nearest_node(node_amount, A):
    k = 0
    r = 0
    T = [0]
    D = 0
    w = []

    while(k < node_amount):
        d = [x for x in array(A[r]).flat]
        print(d)
        l = d.copy()
        for i in T:
            l[i] = 99999
        print(l)
        minimum = min(l)
        print(minimum)
        row = l.index(minimum)
        T.append(row)
        r = row
        k += 1
        D = D + minimum
        w.append(minimum)
    w[-1] = d[0]
    return T, D - minimum + d[0], w

def sucess_node(node_amount, A):
    k = 1
    r = 0
    T = [0,0]
    D = 0
    w = []
    while(k<node_amount-1):
        loaded_array = []
        min_array = []
        for i in range(node_amount):
            data = [x for x in array(A[i]).flat]
            new_array = []
            for j in T[0:len(T)-1]:
                new_array.append(data[j])
            loaded_array.append(new_array)
        for i in loaded_array:
            min_array.append(min(i))
        max_value = max(min_array)
        print(loaded_array)
        print(min_array)
        print(max_value)
        ind_min = min_array.index(max_value)
        indx = min(loaded_array[ind_min])
        print(ind_min)
        if len(T) == 2:
            T.insert(1, ind_min)
            B = [x for x in array(A[0]).flat]
            D = 2 * B[ind_min]
        else:
            min_array_t = []
            new_t = ind_min
            B = [x for x in array(A[new_t]).flat]
            for i in range(len(T)-1):
                C = [x for x in array(A[T[i]]).flat]
                new_index = B[T[i]] + B[T[i+1]] - C[T[i+1]]
                min_array_t.append(new_index)
            print(min_array_t)
            min_new_t = min_array_t.index(min(min_array_t))
            print(min_new_t)
            T.insert(min_new_t+1, ind_min)
            print(T)
            D += min(min_array_t)
            k += 1
        print(D)
    Z = []
    for i in range(node_amount):
        z = [x for x in array(A[i]).flat]
        Z.append(z)
    for i in range(len(T)-1):
        w.append(Z[T[i]][T[i+1]])
    print(w)
    return T, D, w
        
        
    
def menu():

    while True:
        print('Co chcesz zrobić?')
        print('1. Wczytaj nowe dane.')
        print('2. Rozwiąż graf metodą najkrótszego sąsiada.')
        print('3. Rozwiąż graf metodą sukcesywnego wyboru węzłów.')
        print('4. Koniec.')
        choose = input('Co chcesz zrobić?: ')

        if is_int(choose) == True:
            choose = int(choose)
            if choose == 1:
                while True:
                    node = input('Podaj ilość węzłów: ')
                    if is_int(node) == True:
                        print('udało się')
                        break
                    else:
                        continue
                node_amount = int(node)
                node_list = []
                for i in range(node_amount):
                    print('Podaj nazwę węzła nr ', i)
                    node = input(': ')
                    node_list.append(node)
                print(node_list)
                g = make_graph(node_amount, node_list)
                g.edge()
                A = g.make_matrix()
                print(A)
                
            elif choose == 2:
                if 'A' in locals():
                    T, D, w = nearest_node(node_amount, A)
                    print(T)
                    print(D)
                    print(w)
                    g.draw(T, D, w, choose)
                    continue
                else:
                    print('Brak uzupełnionej tablicy')
                    continue
            elif choose == 3:
                if 'A' in locals():
                    T, D, w = sucess_node(node_amount, A)
                    g.draw(T, D, w, choose)
                    continue
            elif choose == 4:
                break
                sys.exit
            else:
                print('Nie ma takiego wyboru, proszę podać liczbę między 1-4.')
                continue
                
        else:
            print('Proszę podać liczbę między 1-4.')
            continue


menu()
