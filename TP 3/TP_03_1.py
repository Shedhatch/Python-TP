#Adrien Varricchione -- TP03 - ex01

Z = 0
A = input('Saisir A :')
print(A)
B = input('Saisir B :')
print(B)
C = input('Saisir C : ')
print(C)

if(A > B):
    Z=A
    A=B
    B=Z
if( C < A):
    Z=C
    C=B
    B=A
    A=Z
elif(C < B):
    Z=C
    C=B
    B=Z
print('' +A + '|' +B + '|' +C )