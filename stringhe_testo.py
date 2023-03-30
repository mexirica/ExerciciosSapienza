'''
1. firstline(t, s) ritorna la prima linea della stringa t che contiene la stringa s , mentre se s non occorre in t ritorna None .
	Esempio
t = Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.
	firstline(t, 'non')		ritorna		'del doman non c’è certezza.'

2. countw(t, w) ritorna il numero di occorrenze della parola w nella stringa t .
	Esempio
	t = 'le cose non sono solo cose, ma anche cosette'
	countw(t, 'cose') 		ritorna		2

3. digits(t) ritorna la lista delle sequenze numeriche contenute nella stringa t .
   Per sequenza numerica intendiamo una sequenza di cifre (caratteri 0 , 1 ,…, 9 ) di lunghezza massimale.
	Esempio
	t = 'via Po n.23, tel. 06 7867555 - cell. 345 675665676 (cc 34565)'
	digits(t) 			ritorna 	['23', '06', '7867555', '345', '675665676', '34565']
'''

def digits(t):
    text=''
    resp=[]
    for idx,value in enumerate(t):
        if value in ['0''1','2','3','4','5','6','7','8','9']:
            text+=value
            if t[idx+1] not in ['0''1','2','3','4','5','6','7','8','9']:
                resp.append(text)
                text=''
    return resp

def countw(t, w):
    i=0
    t=t.split()
    for n in t:
        n=n.strip(',')
        if w==n:
            i+=1
    return i
t = '''Quant’è bella giovinezza
che si fugge tuttavia!
Chi vuol esser lieto, sia:
del doman non c’è certezza.'''

def firstline(t, s):
    t=t.split('\n')
    for n in t:
        if s in n:
            return n

