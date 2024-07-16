""" Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.

Calcolare e stampare la somma di tutti gli elementi dell'array.

Calcolare e stampare la media di tutti gli elementi dell'array. """

import numpy as np

def crea_arr_casuale():
    #Creo un array di 15 numeri casuali compresi tra 1 e 100
    arr_random = np.random.randint(1, 100, 15)
    print("Array di 15 elementi contenente numeri casuali compresi tra 1 e 100:")
    print(arr_random)
    return arr_random

def somma(arr_random):
    #Calcolo la somma degli elementi dell' array
    somma = np.sum(arr_random)
    print("La somma degli elementi dell'array è ", somma)

def media(arr_random):
    #Calcolo la media degli elementi dell' array
    media = np.mean(arr_random)
    print("La media degli elementi dell'array è ", media)



#richiamo le funzioni
arr_random =crea_arr_casuale()
somma(arr_random)
media(arr_random)