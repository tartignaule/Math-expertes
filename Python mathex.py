import math

def div(n):
    l=[]
    for d in range (1,n+1):
        if n%d==0:
            l.append(d)
    return l

def div2():
    l2=[]
    for i in range (1,10000):
        if len(div(i)) == 13:
            l2.append(i)
    return l2

def parf():
    l3=[]
    for i in range (1,10000):
        x=div(i)
        x.pop()
        if sum(x) == i:
            l3.append(i)
    return l3