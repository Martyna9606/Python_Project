from scipy.optimize import linprog
import re


Z = []
Z = input('Wprowadź równanie funkcji każdy element zapisuj oddzielajac go spacją: ')

def isfloat(value):
   try:
      float(value)
      return True
   except:
      return False

Z = Z.split()
Z_var = []
for i in Z:
   var = isfloat(i)
   if var == True:
       i = float(i)
       Z_var.append(i)
print(Z_var)
wybór = input('Czy chcesz: 1. Max , 2.Min: ')
if wybór == '1':
   for i in range(len(Z_var)):
      Z_var[i] = Z_var[i] * -1
bounds_l = []
bounds_r = []
equal_l = []
equal_r = []
while True:
   choose = input('Czy chcesz dodać nowe ograniczenie? 1.Tak - 2.Nie: ')
   if choose == '1':

      bound = []
      for i in range(len(Z_var)):
         print('Podaj współczynnik dla X', i+1)
         współczynnik = float(input(''))
         bound.append(współczynnik)
      print(bound)
      ineq = ['=', '>', '<', '>=', '<=']
      print('Podaj znak nierówności: ',ineq)
      ind = input('')
      right = float(input('Podaj wartość prawostronną ograniczenia: '))


      if ind == '>=' or ind == '>':
         for i in range(len(bound)):
            bound[i] = bound[i] * -1
         right = right * -1
         bounds_l.append(bound)
         bounds_r.append(right)
      elif ind == '=':
         equal_l.append(bound)
         equal_r.append(right)

      else:
         bounds_l.append(bound)
         bounds_r.append(right)

   else:
      break
      

print(Z_var)
print(bounds_l)
print(bounds_r)


bnd = []
for i in range(len(Z_var)):
   print('Wprowadź ograniczenie X', [i+1], 'jeżeli to nieskończoność wpisz inf')
   ogr1 = input('Początek: ')
   ogr2 = input('Koniec: ')
   if ogr1 == 'inf':
      ogr1 = float('inf')
   if ogr2 == 'inf':
      ogr2 = float('inf')
   ogr = (ogr1, ogr2)

   bnd.append(ogr)
print(bnd)

if wybór == '1':
   opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, A_eq = equal_l, b_eq = equal_r, bounds = bnd, method = 'revised simplex')
else:
   opt = linprog(c = Z_var, A_ub = bounds_l, b_ub = bounds_r, A_eq = equal_l, b_eq = equal_r, bounds = bnd, method = 'simplex')
   
print('Punkty X i Y: ',opt.x)
if wybór == '1':
   wynik = opt.fun * -1
else:
   wynik = opt.fun
print('Wynik optymalny: ', wynik)
