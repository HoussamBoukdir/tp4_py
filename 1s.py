def  estPaire(N):
     if N % 2==0:
          ok=True
     else:
          ok=False
     return ok
def afficher():
     A=int(input("taper le nombre de depart:"))
     B=int(input("taper le nombre d'arrivee:"))
     for i in range(A,B+1):
          if estPaire(i)==False:
               print(i,end='\t')
afficher()