'''
Scrivere le funzioni seguenti.
1. prec(g1, m1, a1, g2, m2, a2) ritornTruea  se la data g1, m1, a1 (giorno, mese, anno) è precedente
   o uguale alla data g2, m2, a2 .
   Esempi
   prec(13, 11, 2012,  2,  3, 2013)	ritornTruea
   prec(13, 11, 2012, 27, 12, 2011)	ritorna	False
   prec( 1, 10, 2013,  1, 11, 2013)	ritornTruea

2. l2d(lst) che, presa in input una lista lst i cui elementi sono numeri da 0 a 9 espressi in lettere
   ( 'zero' , 'uno' , …, 'nove' ), ritorna una nuova lista i cui elementi sono la traduzione in numeri degli
   elementi di lst . Esempio
   l2d(['nove','due','due','tre'])	ritorna	[9,2,2,3]

3. distinct(lst) ritorna una nuova lista che contiene gli stessi elementi di lst ma senza le eventuali
   ripetizioni.
   Esempi
   distinct([3,1,3,2,6,6])		ritorna	[3, 1, 2, 6]
   distinct(['a','ab','a','ab'])	ritorna	['a', 'ab']
'''

def prec(g1, m1, a1, g2, m2, a2):
    if a1<=a2:
        if a1<=a2 and m1<m2 or m1<=m2:
            if m1<=m2 and g1<g2:
                return True
    else: return False



def l2d(lst):
    ret=[]
    for n in lst:
        if n == "zero":
            ret.append(0)
        elif n== "uno":
            ret.append(1)
        elif n=="due":
            ret.append(2)
        elif n=="tre":
            ret.append(3)
        elif n=="quattro":
            ret.append(4)
        elif n=="cinque":
            ret.append(5)
        elif n=="sei":
            ret.append(6)
        elif n=="sette":
            ret.append(7)
        elif n=="otto":
            ret.append(8)
        elif n=="nove":
            ret.append(9)
    return ret

def distinct(lst):
    for n in lst:
        for j in lst[1:]:
            if n==j:
                lst.remove(j)
                break
    lst.sort()
    return lst
