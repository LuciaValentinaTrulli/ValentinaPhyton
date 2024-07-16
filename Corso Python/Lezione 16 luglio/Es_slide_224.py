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

#Creo un array di 50 numeri equidistanti tra 0 e 10 usando linspace
arr = np.linspace(0, 10, 50) #numero iniziale, finale, numero di elementi voluti
print("L'array iniziale é:")
print(arr) 

#Creo un array di 50 numeri casuali compresi tra 0 e 1
arr_random = np.random.random(50)
print("L'array di 50 numeri casuali tra 0 e 1 è")
print(arr_random)

#Sommo i due array elemento per elemento per ottenere un nuovo array
arr_somma = arr + arr_random
print ("L'array somma è:", arr_somma)

#Calcolo la somma totale degli elementi del nuovo array
somma_nuovo_arr = np.sum(arr_somma)
print("La somma degli elementi del nuovo array è ", somma_nuovo_arr)

#Calcolo la somma degli elementi del nuovo array che sono maggiori di 5
somma_maggiori_5 = np.sum(arr_somma[arr_somma>5])
print ("La somma degli elementi del nuovo array che sono maggiori di 5 é", somma_maggiori_5)

