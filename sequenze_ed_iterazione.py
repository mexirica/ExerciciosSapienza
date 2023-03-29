'''
1. Scrivere una funzione media(vals) che prende in input una lista vals (i cui valori si assume siano
   numeri) e ritorna la media dei suoi valori.

2. Scrivere una funzione space(s, k) che prende in input una stringa s e un intero k e ritorna una nuova
   stringa che ha i caratteri di s separati da k spazi. Ad esempio
   space('ciao ciao', 1) ritorna la stringa

    'c i a o   c i a o'

3. Scrivere una funzione crossing_over(m, f) che prese in input due liste m e f (che si assume abbiano
   la stessa lunghezza), ritorna una nuova lista che contiene l'incrocio delle due liste come illustrato dal
   seguente esempio (prendendo alternativamente un elemento dalla prima lista, poi dalla seconda, poi dalla prima ...):
   crossing_over([1, 3, 5], [2, 4, 6])
   ritorna la lista [1, 2, 3, 4, 5, 6]'
'''



def media(vals):
 return ((sum(vals))/len(vals))

def spaces(s,k):
   frase=""
   for letter in s:
      if letter == s[-1]:
         frase+= letter
      else:
         frase += letter + " "*k

   return (frase)

def crossing_over(m, f):
   x=[*m,*f]
   x.sort()
   return x

crossing_over([1,3,4],[2,5])