# Miller-Rabin
Nombre: Emmanuel del Piero Martinez Salcedo

El presente código en python permite encontrar los números primos de una cantidad dada de cifras con una precisión dada y además permite hallar 10 primos aleatorios de 16, 32 y 64 bits

### Test de primalidad de Miller-Rabin
El test de primalidad de Miller-Rabin es un algoritmo para determinar si un número dado es primo, similar al test de primalidad de Fermat. Su versión original fue propuesta por G. L. Miller, se trataba de un algoritmo determinista, pero basado en la no demostrada hipótesis generalizada de Riemann; Michael Oser Rabin modificó la propuesta de Miller para obtener un algoritmo probabilístico que no utiliza resultados no probados.

## Funcionamiento "Hallar primos de n cifras"
El programa pide ingresar n y s siendo n la cantidad de cifras de los números primos a hallar y s la presición que querramos usar, entre mayor sea la presición se conseguira mejores resultados pero usara mas tiempo computacional, finalmente el programa retorna todos los primos encontrados y la cantidad de primos que existen.

## Funcionamiento "Hallar primos aleatorios de 16, 32 y 64 bits"
El programa solo pide ingresar s (Presición) y retorna los elementos de una lista donde se almacenaran los 30 primos (10 primos de cada cantidad de bits)

## "S" (presición) usado en los experimentos

Para los experimentos se uso una presición de 3, usando presición de 2 se podía llegar a obtener valores erroneos variando en 1 o 2 primos mas o menos. Con varias pruebas hechos con presición 3 no retorno valores erroneos pero esto no significa que no pudiera pasar, solo es improbable. Incluso probando con presición 100 usando el compilador integrado en el IDE VScode no se noto una diferencia de tiempo considerable por lo que este incluso podria ser un candidato a la presición, pero si de ahorrar tiempo se trata considero que la presición s=3 es ideal.

## Código

```python
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
```

```python
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
```
