import random
def EsCompuesto(a,n,t,u):
    x= pow(a,u,n)
    if x == 1 or x == n - 1:
        return False
    for i in range(t-1):
        x=pow(x, 2,n)
        if x == n - 1:
            return False
    return True
        

def MillerRabin(n,s):
    t=0
    u=n-1
    while u % 2 == 0:
        u = u // 2
        t = t +1
    for i in range(s):
        a = random.randrange(2, n - 1)
        if EsCompuesto(a,n,t,u) == True:
            return False
    return True

s=int(input("Ingresa s (presición):"))
i=0
list=[]
while i<=9:
    r=random.randrange(2,65535)
    aux=MillerRabin(r,s)
    if aux==True:
        list.append(r)
        i=i+1
    else:
        continue
i=0
while i<=9:
    r=random.randrange(2,4294967295)
    aux=MillerRabin(r,s)
    if aux==True:
        list.append(r)
        i=i+1
    else:
        continue
i=0
while i<=9:
    r=random.randrange(2,9223372036854775807)
    aux=MillerRabin(r,s)
    if aux==True:
        list.append(r)
        i=i+1
    else:
        continue
for i in list:
    print(i)