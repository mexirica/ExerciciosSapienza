'''
Scrivere le funzioni seguenti.

1. wset(fname) ritorna un insieme contenente le parole (distinte) del file fname . Le parole sono ridotte
   alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
 wset('alice.txt') ritorna un insieme di cardinalità 3007

2. wsub(fn1, fn2) ritorna un insieme contenente le parole (distinte) che appaiono nel file fn1 e che non
   appaiono nel file fn2 . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
 wsub('alice.txt', 'holmes.txt') ritorna un insieme di cardinalità 710

3. wdict(fname) ritorna un dizionario che ad ogni parola del file fname associa il numero di occorrenze
   della parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
 d = wdict('alice.txt')
 d['alice'] --> 403
 d['rabbit'] --> 51
 d['queen'] --> 75

4. nextw(fname) ritorna un dizionario che ad ogni parola del file fname associa l'insieme delle parole che
   seguono la parola nel file. Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempio
 d = nextw('alice.txt')
 d['go']
{'and', 'among', 'splashing', 'back', 'down', 'through', 'at', 'in', 'nearer', 'said', 'from', 'for',
'no', 'there', 'to', 'his', 'after', 'let', 'with', 'by', 'on', 'alice', 'near', 'anywhere', 'round'}
 d['write']
{'that', 'this', 'it', 'one', 'with', 'out'}

5. mostf(fname, l) ritorna un insieme contenente le parole di lunghezza l di massima frequenza nel file
   fname . Le parole sono ridotte alle minuscole e il file è decodificato con UTF-8-SIG.
   Esempi
 mostf('holmes.txt', 7)
{'nothing', 'however'}
mostf('holmes.txt', 8)
{'sherlock'}
mostf('frankenstein.txt', 16)
{'unenforceability', 'impracticability', 'perpendicularity', 'indiscriminately', 'inextinguishable'}
'''


def wset(fname):
    f=open(fname,'r',encoding='utf-8-sig')
    w=f.read().lower().split()
    return set(w)

def wsub(fn1,fn2):
    words1=wset(fn1)
    words2=wset(fn2)
    return words1.difference(words2)

def wdict(fname):
    f=open(fname,'r',encoding='utf-8-sig')
    dic={}
    for key in f.read().lower().split():
        if key not in dic:
            key=key.strip('(.)')
            dic[key]=1
        else:
            dic[key]+=1
    return dic


def nextw(fname):
    pass

def mostf(fname, l):
    f=open(fname,'r',encoding='UTF-8-SIG')
    result=[]
    for word in f.read().split():
        if l == len(word):
            result.append(word)
    return result




