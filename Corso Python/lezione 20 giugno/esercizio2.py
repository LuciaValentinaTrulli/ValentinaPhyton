#punto 1
#chiedo all'utente di inserire un numero
numero_inserito = float(input("Inserisci un numero: "))

resto = numero_inserito % 2

if resto == 0:
    print("Pari")
else:
    print ("Dispari")


#punto 2
controllo = True

while controllo:
    n = int(input("Inserisci un numero intero positivo: "))
    
    #controllo se positivo
    if n>0:

        #stampo ciclando sugli elementi
        for i in range(n, -1, -1):
            print(i)

        scelta = input("Vuoi ripetere? (si o no): ")
        if scelta.lower() == "no":
            controllo = False
    else:
        print("Il numero non è positivo")


#punto 3
#creazione della lista
lista=[]
controllo = True
while controllo:
    numero_inserito = float(input("Inserisci un numero: "))
    lista.append(numero_inserito)

    scelta = input("Vuoi inserire un altro numero? (si o no): ")
    if scelta.lower() == "no":
        controllo = False

#calcolo e stampa del quadrato
for n in lista:
    quadrato = n * n
    print (quadrato)


#punto 4
#creazione della lista
lista=[]
controllo = True
while controllo:
    numero_inserito = int(input("Inserisci un numero intero: "))
    lista.append(numero_inserito)

    scelta = input("Vuoi inserire un altro numero? (si o no): ")
    if scelta.lower() == "no":
        controllo = False

#verifico che la lista non sia vuota
if  len(lista) == 0:
    print("Lista vuota")
    
else:
    #trovare numero massimo della lista
    # lista_ordinata = lista.sort()
    # lunghezza_lista = len(lista)
    # indice = lunghezza_lista - 1
    # massimo = lista_ordinata[indice]
    massimo = max(lista)
    print("Il numero massimo tra quelli inseriti è: ")
    print(massimo)

    #contare i numeri presenti nella lista
    controllo = True
    contatore = 0
    while controllo:
        for n in lista:
            contatore+=1
        print ("I numeri inseriti sono in totale: " )
        print (contatore)
        controllo = False    
