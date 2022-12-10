import math


            ###     EXERCICE 1     ###

    # Fonction donnant les diviseurs de n
def div(n):
    l=[]
    for d in range (1,n+1):
        if n%d==0:
            l.append(d)
    return l

    # Fonction donnant l'entier qui possède 13 diviseurs entre 1 et 10000
def div2():
    l2=[]
    for i in range (1,10000):
        if len(div(i)) == 13:
            l2.append(i)
    return l2


            ###     EXERCICE 2     ###

    # Fonction donnant la liste des nombres parfaits compris entre 1 et 10000
def parf():
    l3=[]
    for i in range (1,10000):
        x=div(i)
        x.pop()
        if sum(x) == i:
            l3.append(i)
    return l3


            ###     EXERCICE 3     ###

    # Fonction donnant la liste des nombres premiers compris entre 0 et 100
def prem():
    l4=[]
    for i in range (0,100):
        if div(i) == [1,i]:
            l4.append(i)
    return l4

    # Fonction déterminant si un nombre est premier où non.
def prem2(p):
    if div(p)==[1,p]:
        print("Le nombre ",p," est premier.")
    else:
        print("Le nombre ",p," n'est pas premier")

def prem3(p):
    L=list(range(1,p))
    for i in range (1,p):
        for d in range (2,i):
            if i%d==0:
                L.remove(i)
                break
    fichier = open("nombres premier.txt", "w")
    L2=str(L)
    fichier.write(L2)
    fichier.close
    print(len(L))
    return L