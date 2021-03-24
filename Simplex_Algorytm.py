from scipy.optimize import linprog
import re
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Funkcja Simplex')
root.geometry('600x650')

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
   Z = równanie.get()
   funkcja = str(Z)
   Z = Z.split()
   global Z_var
   Z_var = []
   for i in Z:
      var = isfloat(i)
      if var == True:
          i = float(i)
          Z_var.append(i)   
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
   nierownosc = nierownosc.split()
   print(nierownosc)
   ineq = ['=', '>', '<', '>=', '<=']
   ind = 0
   for i in nierownosc:
      if i in ineq:
         ind = i
         break
   lewa_strona = []
   left_bnd = []
   right_bnd = []
   for i in nierownosc[:nierownosc.index(ind)]:
      lewa_strona.append(i)
   print(ind)
   print(lewa_strona)
   for i in lewa_strona:
      var = isfloat(i)
      if var == True:
         left_bnd.append(float(i))
   print(left_bnd)
   for i in nierownosc[nierownosc.index(ind)+1:]:
      right_bnd.append(float(i))
   print(right_bnd)
   if ind == '>=' or ind == '>':
      for i in range(len(left_bnd)):
         left_bnd[i] = left_bnd[i] * -1
      for i in range(len(right_bnd)):
         right_bnd[i] = right_bnd[i] * -1
   print(left_bnd)
   if ind == '=':
      equal_l.append(left_bnd)
      equal_r.append(right_bnd)
   else:
      bounds_l.append(left_bnd)
      bounds_r.append(right_bnd)

   print(bounds_l)
   print(bounds_r)
   label4 = Label(root, text = nierownosc)
   label4.pack()
   T.delete('1.0', END)
      

zatwierdz_nierownosc = Button(root, text = 'Zatwierdź nierówność', command = dodaj_nierownosc)
zatwierdz_nierownosc.pack()


label5 = Label(root, text = 'Wprowadź nierówność dla każdego x - dla nieskończoności wpisz inf', width = 200)
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
   print(Z_var)
   print(bounds_l)
   print(bounds_r)
   print(equal_l)
   print(equal_r)
   print(bnd)
   print(wybór)

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
   xy = opt.x
   x = str(xy[0])
   y = str(xy[1])
   wynik = str(wynik)
   label7 = Label(root, text = 'Wynik optymalny: ' + wynik)
   label7.pack()
   for i in range(len(opt.x)):
      label8 = Label(root, text = 'X' + str(i+1) +': '+ str(opt.x[i]))
      label8.pack()
btn2 = Button(root, text = 'Oblicz', command = oblicz)
btn2.pack()


root.mainloop()

