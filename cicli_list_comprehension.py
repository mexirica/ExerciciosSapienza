'''
Usando la list comprehension definite le seguenti funzioni:

1. Definite la funzione triangolo(N) che torna una matrice triangolare di N*N/2 elementi,
   contenente solo la parte in basso a sinistra della matrice dei prodotti (tabelline).
   Il risultato quindi dev'essere una lista di N liste di lunghezza crescente da 1 a N.
   Esempio:
triangolo(4)
[[1],
 [2, 4],
 [3, 6, 9],
 [4, 8, 12, 16]]

2. Definite la funzione potenze_crescenti(lista) che produce come risultato una lista
   in cui ciascun elemento è ottenuto come la potenza i-esima del corrispondente elemento
   in posizione i della lista passata come argomento.
   Esempio:
 potenze_crescenti([2, 3, 4, 5, 6])
[1, 3, 16, 125, 1296]

3. Definite la funzione non_divisibili(N, divisori) che trova tutti i numeri tra 1 e N (compresi)
   che non sono divisibili per nessuno dei valori presenti nella lista di divisori (interi).
   Esempio:
non_divisibili(10, [2, 3])
[1, 5, 7]


4.  Definite la funzione doppio_dado() che stampa una successione di estrazioni casuali di due dadi a 6 facce
    e che conta e torna come risultato quante ne sono state necessarie prima di ottenere un doppio 6.
    Esempio:
 doppio_dado()
3 5
2 2
1 6
6 4
3 1
5 4
6 6
7
'''
import random


def triangolo(n):
    lst = []
    z = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            x = (i * j)
            z.append(x)
        lst.append(z)
        z = []
    lst = '\n'.join(map(str, lst))
    print(lst)


def potenze_crescenti(lista):
    i = 0
    lst = []
    for n in lista:
        lst.append(n ** i)
        i += 1
    return lst


def non_divisibili(N, divisori):
    lst = []
    result = []
    for j in range(N):
        for i in divisori:
            if j % i != 0:
                lst.append(j)
    for i in lst:
        if lst.count(i) == len(divisori):
            result.append(i)
    return list(set(result))


def doppio_dado():
    i = 0
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    while a and b != 6:
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(a, b)
        i += 1
    print(i)
