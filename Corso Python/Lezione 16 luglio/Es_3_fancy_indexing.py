""" Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.

Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).

Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array (considerando la numerazione delle righe che parte da 0).

Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore. """

import numpy as np

def crea_arr_casuale():
    #Creo un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50
    arr_random = np.random.randint(10, 50, size=(4, 4))
    print("Array 4 x 4 contenente numeri casuali interi tra 10 e 50")
    print(arr_random)
    return arr_random

def seleziono_righe(arr_random):
    #fancy indexing per selezionare e stampare righe agli indici (0, 1), (1, 3), (2, 2) e (3, 0)
    indici = np.array([(0, 1), (1, 3), (2, 2) , (3, 0)])
    print("\nSeleziono righe:")
    print(arr_random[indici])
    return arr_random[indici]
1
#metodo alternativo
""" def seleziono_righe(arr_random):
    #fancy indexing per selezionare e stampare righe agli indici (0, 1), (1, 3), (2, 2) e (3, 0)
    indici1 = [0, 1]             #fancy indexing con liste
    print("Righe agli indici 0 e 1")
    print(arr_random[indici1])

    indici2 = [1, 3]
    print("Righe agli indici 1 e 3")
    print(arr_random[indici2])

    indices = np.array([2, 2])  #fancy indexing con array
    print("Righe agli indici 2 e 2")
    print(arr_random[indices])

    indices = np.array([3, 0])
    print("Righe agli indici 3 e 0")
    print(arr_random[indices])  """

def righe_dispari(arr_random):
    #fancy indexing per selezionare e stampare tutte le righe dispari dell'array
    indici = [0,2]
    arr_disp = arr_random[indici]
    print("Le righe dispari sono:")
    print(arr_disp)

def aggiungo_10(selezione):
    #Modificare le righe selezionate nel primo punto dell'esercizio aggiungendo 10 al loro valore
    scalare = 10
    risultato= selezione +scalare
    print("Aggiungo 10 ad ogni valore delle rige selezionate:")
    print(risultato)



def menu():
    arr_random = None
    selezione = None
    while True:
        print("\nMenu:")
        print("1. Crea array casuale")
        print("2. Seleziona righe specifiche")
        print("3. Seleziona righe dispari")
        print("4. Aggiungi 10 alla selezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            arr_random = crea_arr_casuale()
        elif scelta == "2":
            if arr_random is not None:
                selezione = seleziono_righe(arr_random)
            else:
                print("Per favore, crea prima l'array casuale (opzione 1).")
        elif scelta == "3":
            if arr_random is not None:
                righe_dispari(arr_random)
            else:
                print("Per favore, crea prima l'array casuale (opzione 1).")
        elif scelta == "4":
            if selezione is not None:
                aggiungo_10(selezione)
            else:
                print("Per favore, seleziona prima le righe (opzione 2).")
        elif scelta == "5":
            print("Uscita dal programma.")
            break
        else:
            print("Scelta non valida, riprova.")

menu()