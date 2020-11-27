#Adrien Varricchione -- TP03 - ex02

import math as m

a = int(input("Entrez la valeur A "))
b = int(input("Entrez la valeur B "))
c = int(input("Entrez la valeur C "))

print("Voici votre équation: " + "A =", a,",","B =", b,",","C =", c,)

delta= b**2 - 4 * (a * c)

if delta < 0:
    print("Aucune valeur disponible")

if delta == 0 :
    s = -b / (2 * a)
    print("Il existe une solution double" , s )
    
if delta > 0 :
    s1 = (-b - m.sqrt(delta)) / 2 * a
    s2 = (-b + m.sqrt(delta)) / 2 * a
    print("Il existe deux solutions" , s1 ,"et", s2 )