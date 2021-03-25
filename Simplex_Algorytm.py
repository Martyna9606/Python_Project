from scipy.optimize import linprog
import re
from tkinter import *
from tkinter.ttk import *
import decimal
from re import search

root = Tk()
root.title('Funkcja Simplex')
root.geometry('600x650')

global keys
keys = []

etykieta1 = Label(root, text = 'Wprowadź równanie funkcji celu: ')
etykieta1.pack()
równanie = Entry(root, width = '50')
równanie.pack()

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
   lbl = Label(root, text = 'Z = '+ funkcja)
   lbl.pack()

btn = Button(root, text = 'Zatwierdź', command = get_function)
btn.pack()

def selection():
   global wybór
   wybór = v.get()
   print(wybór)
   if wybór == 1:
      for i in range(len(Z_var)):
         Z_var[i] = Z_var[i] * -1
   print(Z_var)

   
r1 = Radiobutton(root, text='Max', variable = v, value = 1, command = selection)
r1.pack()
r2 = Radiobutton(root, text='Min', variable = v, value = 2, command = selection)
r2.pack()

   

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
global bnd
bnd = []



label2 = Label(root, text = 'Wprowadź ograniczenia nierówności')
label2.pack()
T = Text(root, height = 5, width = 50, bg = 'light blue')
T.pack()

def dodaj_nierownosc():
   nierownosc = T.get('1.0', 'end')
   print(nierownosc)
   nier = nierownosc
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
   label4 = Label(root, text = nierownosc)
   label4.pack()
   T.delete('1.0', END)

      

zatwierdz_nierownosc = Button(root, text = 'Zatwierdź nierówność', command = dodaj_nierownosc)
zatwierdz_nierownosc.pack()


label5 = Label(root, text = 'Wprowadź ograniczenie dla każdego x - dla nieskończoności wpisz inf', width = 200)
label5.pack()
T1 = Text(root, height = 5, width = 50, bg = 'light yellow')
T1.pack()


def ograniczenia():
   bnd1 = []
   ogr = []
   ogr = T1.get('1.0', 'end')
   ogr = ogr.split()
   ogr[0] = float(ogr[0])
   ogr[1] = float(ogr[1])               
   bnd1 = (ogr[0], ogr[1])
   print(bnd1)
   bnd.append(bnd1)
   label6 = Label(root, text = bnd)
   label6.pack()
   T.delete('1.0', END)
btn1 = Button(root, text = 'Zatwierdź ograniczenie dla X', command = ograniczenia)
btn1.pack()

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
   wynik = str(wynik)
   label7 = Label(root, text = 'Wynik optymalny: ' + wynik)
   label7.pack()
   for i in range(len(opt.x)):
      x = decimal.Decimal(opt.x[i])
      x = "%.2f" % x
      #x = str(x)
      label8 = Label(root, text = 'X' + str(i+1) +': '+ x)
      label8.pack()
   label9 = Label(root, text = 'Wyższa Szkoła Bankowa Abram Martyna 62508')
   label9.pack()
btn2 = Button(root, text = 'Oblicz', command = oblicz)
btn2.pack()


root.mainloop()

