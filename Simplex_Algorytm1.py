from scipy.optimize import linprog
import re
from tkinter import *
from tkinter.ttk import *
import decimal
from re import search

root = Tk()
root.title('Funkcja Simplex')
root.geometry('750x300')

main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill = BOTH, expand = 1)

scrollbar = Scrollbar(main_frame, orient = VERTICAL, command = canvas.yview)
scrollbar.pack(side=RIGHT, fill = Y)

canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind('<Configure>',  lambda e: canvas.configure(scrollregion = canvas.bbox('all')))

second_frame = Frame(canvas)

canvas.create_window((0,0), window = second_frame, anchor = 'nw' )



global keys
keys = []



etykieta1 = Label(second_frame, text = 'Wprowadź równanie funkcji celu: ')
etykieta1.grid(row = 1, column = 1)
równanie = Entry(second_frame, width = 50)
równanie.grid(row = 1, column = 2)

def isfloat(value):
   try:
      float(value)
      return True
   except:
      return False

r = StringVar()
v = IntVar()

def get_function():
   global Z
   global Z1
   Z1 = []
   Z = równanie.get()
   func = Z
   Z = Z.replace(' ', '')
   Z = Z.split('+')
   for i in Z:
      j = i
      j = j.split('*')
      Z[Z.index(i)] = j
   for i in Z:
      j = i
      if len(j) == 2:
         var = isfloat(j[0])
         if var == True:
            Z1.append(float(j[0]))
            keys.append(j[1])
         else:
            Z1.append(float(j[1]))
            keys.append(j[0])
      else:
         if '-' in j[0]:
            r = j[0].replace('-', '')
            Z1.append(-1.0)
            keys.append(r)
         else:
            Z1.append(1.0)
            keys.append(j[0])
            
   funkcja = str(func)
   print(Z1)
   print(keys)
   global Z_var
   Z_var = []
   
   for i in range(len(Z1)):
      Z_var.append(float(Z1[i]))

   print(keys)
   Z_var = Z1
   print(Z_var)
   lbl = Label(second_frame, text = 'Z = '+ funkcja)
   lbl.grid(row = 2, column = 2)
   global bnd
   bnd = [(0.0, float('inf'))] * len(keys)
   print(bnd)
   

btn = Button(second_frame, text = 'Zatwierdź', command = get_function)
btn.grid(row = 2, column = 1)

def selection():
   global wybór
   wybór = v.get()
   print(wybór)
   if wybór == 1:
      for i in range(len(Z_var)):
         Z_var[i] = Z_var[i] * -1
   print(Z_var)

   
r1 = Radiobutton(second_frame, text='Max', variable = v, value = 1, command = selection)
r1.grid(row = 3, column = 1)
r2 = Radiobutton(second_frame, text='Min', variable = v, value = 2, command = selection)
r2.grid(row = 3, column = 2)

   

y1 = 200
x1 = 10


global bounds_l 
global bounds_r
global equal_l
global equal_r
bounds_l = []
bounds_r = []
equal_l = []
equal_r = []



label2 = Label(second_frame, text = 'Wprowadź ograniczenia nierówności')
label2.grid(row=4, column = 1)
T = Entry(second_frame, width = 50)
T.grid(row = 4, column =  2)
roww = 6
def dodaj_nierownosc():
   nierownosc = T.get()
   print(nierownosc)
   nier = nierownosc.replace(' ', '')
   nierownosc = nierownosc.split()
   print(nierownosc)
   ineq = ['=', '>', '<', '>=', '<=']
   ind = 0

   for i in ineq:
      if search(i, nier):
         print(i)
         ind = i
      
   left_side = nier[:nier.index(ind)]
   right_side = nier[nier.index(ind)+1:]
   if '=' in right_side:
      right_side = right_side.replace('=', '')
   
   print(left_side)
   print(right_side)

   left_side = left_side.split('+')
   print(left_side)

   for i in left_side:
      j = i
      j = j.split('*')
      left_side[left_side.index(i)] = j

   print(left_side)
   l = [0.0] * len(Z_var)
   r = [0.0]
   print(l)
   for i in left_side:
      j = i
      if len(j)==2:
         var = isfloat(j[0])
         if var == True:
            l[keys.index(j[1])] = float(j[0])
         else:
               l[keys.index(j[0])] = float(j[1])
      else:
         if '-' in j[0]:
            r = j[0].replace('-', '')
            l[keys.index(r)] = -1.0
         else: 
            l[keys.index(j[0])] = 1.0
   print(l)
   r = float(right_side)
   print(r)

   if ind == '>=' or ind == '>':
      for i in range(len(l)):
         l[i] = l[i] * -1
      r = r * -1

   if ind == '=':
      equal_l.append(l)
      equal_r.append(r)
      
   else:
      bounds_l.append(l)
      bounds_r.append(r)

   print(bounds_l)
   print(bounds_r)
   global roww
   label4 = Label(second_frame, text = nierownosc)
   label4.grid(row = roww, column = 2)
   roww = roww + 1

      

zatwierdz_nierownosc = Button(second_frame, text = 'Zatwierdź nierówność', command = dodaj_nierownosc)
zatwierdz_nierownosc.grid(row = 5, column = 2)


label5 = Label(second_frame, text = 'Wprowadź ograniczenie dla konkretnej zmiennej')
label5.grid(row = 6, column = 1)
T1 = Entry(second_frame, width = 20)
T1.grid(row = 7, column = 1)


def ograniczenia():
   bnd1 = []
   ogr = []
   ogr = T1.get()
   ogr = ogr.replace(' ', '')
   ogr = ogr.split('=')
   index1 = keys.index(ogr[0])
   val = ogr[1].split(',')            
   bnd1 = (float(val[0]), float(val[1]))
   bnd[index1] = bnd1
   print(bnd1)
   #bnd.append(bnd1)
   label6 = Label(second_frame, text = bnd)
   label6.grid(row = 8, column = 1)
   
btn1 = Button(second_frame, text = 'Zatwierdź ograniczenie dla X', command = ograniczenia)
btn1.grid(row = 9, column = 1)

def oblicz():

   if wybór == 1:
      if len(equal_l) > 0:
         opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, A_eq = equal_l, b_eq = equal_r, bounds = bnd, method = 'revised simplex')
         print('1')
      else:
         print('2')
         opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, bounds = bnd, method = 'revised simplex')
         print(opt)
   else:
      if len(equal_l) > 0:
         print('3')
         opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, A_eq = equal_l, b_eq = equal_r, bounds = bnd, method = 'simplex')
      else:
         print('4')
         opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, bounds = bnd, method = 'simplex')
   global wynik
   global xy 
   print('Punkty X i Y: ',opt.x)
   if wybór == 1:
      wynik = opt.fun * -1
   else:
      wynik = opt.fun
   print('Wynik optymalny: ', wynik)
   wynik = decimal.Decimal(wynik)
   wynik = "%.2f" % wynik
   #wynik = str(wynik)
   label7 = Label(second_frame, text = 'Wynik optymalny: ' + wynik)
   label7.grid(row = 11, column = 1)
   row1 = 12
   for i in range(len(opt.x)):
      x = decimal.Decimal(opt.x[i])
      x = "%.2f" % x
      #x = str(x)
      label8 = Label(second_frame, text = keys[i] +': '+ x)
      label8.grid(row = row1, column = 1)
      row1 += 1
   label9 = Label(second_frame, text = 'Wyższa Szkoła Bankowa Abram Martyna 62508')
   label9.grid(row = row1, column = 1)
btn2 = Button(second_frame, text = 'Oblicz', command = oblicz)
btn2.grid(row = 10, column = 1)



root.mainloop()

