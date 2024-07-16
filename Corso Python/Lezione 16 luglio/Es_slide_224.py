""" Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
Somma i due array elemento per elemento per ottenere un nuovo array.
Calcola la somma totale degli elementi del nuovo array.
Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.

Obiettivo:

Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per creare array 
di numeri casuali, e sum per eseguire operazioni di somma sugli array, incluso l'uso di condizioni 
per la somma parziale. """

import numpy as np

def crea_arr_linspace():
    #Creo un array di 50 numeri equidistanti tra 0 e 10 usando linspace
    arr = np.linspace(0, 10, 50) #numero iniziale, finale, numero di elementi voluti
    print("L'array iniziale é:")
    print(arr)
    return arr 

def crea_arr_casuale():
    #Creo un array di 50 numeri casuali compresi tra 0 e 1
    arr_random = np.random.random(50)
    print("L'array di 50 numeri casuali tra 0 e 1 è")
    print(arr_random)
    return arr_random

def somma_elementi(arr, arr_random):
    #Sommo i due array elemento per elemento per ottenere un nuovo array
    arr_somma = arr + arr_random
    print ("L'array somma è:", arr_somma)
    return arr_somma

def somma(arr_somma):
    #Calcolo la somma totale degli elementi del nuovo array
    somma_nuovo_arr = np.sum(arr_somma)
    print("La somma degli elementi del nuovo array è ", somma_nuovo_arr)

def somma_maggiori_5(arr_somma):
    #Calcolo la somma degli elementi del nuovo array che sono maggiori di 5
    somma_maggiori_5 = np.sum(arr_somma[arr_somma>5])
    print ("La somma degli elementi del nuovo array che sono maggiori di 5 é", somma_maggiori_5)


def menu():
    print("1. Crea un array di 50 numeri equidistanti tra 0 e 10")
    print("2. Creo un array di 50 numeri casuali compresi tra 0 e 1")
    print("3. Sommo i due array elemento per elemento per ottenere un nuovo array")
    print("4. Calcolo la somma totale degli elementi del nuovo array")
    print("5. Calcolo la somma degli elementi del nuovo array che sono maggiori di 5")
    print("0. Esci")


while True:
    menu()
    scelta=input("Inserisci scelta: ")
    if scelta=="1":
        crea_arr_linspace()
    elif scelta=="2":
        crea_arr_casuale()
    elif scelta=="3":
        arr = crea_arr_linspace()
        arr_random = crea_arr_casuale()
        somma_elementi(arr, arr_random)
    elif scelta=="4":
        arr = crea_arr_linspace()
        arr_random = crea_arr_casuale()
        arr_somma = somma_elementi(arr, arr_random)
        somma(arr_somma)
    elif scelta=="5":
        arr = crea_arr_linspace()
        arr_random = crea_arr_casuale()
        arr_somma = somma_elementi(arr, arr_random)
        somma_maggiori_5(arr_somma)
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")