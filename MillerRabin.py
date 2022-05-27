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

n=int(input("Primos de cuantos digitos quieres generar:"))
s=int(input("Ingresa s (presición):"))
l=0
for i2 in range(pow(10,n-1),pow(10,n)):
    k = MillerRabin(i2,s)
    if k == True:
        print(i2)
        l=l+1
print("Total de primos: ",l)