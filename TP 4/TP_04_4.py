N=0;
P= 0.05;

Mst=input("Merci de saisir une épaisseur en mètres: ")
M=int(Mst)
M=M*1000

while P<M :
    P=P*2
    N=N+1
print ("Le nombre de plis à éffectuer sera de", N ,"fois.")