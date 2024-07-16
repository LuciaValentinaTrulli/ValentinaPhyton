""" Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, 
genera un array casuale e calcola la somma degli elementi.

Esercizio:
Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
Cambia la forma dell'array a una matrice 3x4.
Genera una matrice 3x4 di numeri casuali tra 0 e 1.
Calcola e stampa la somma degli elementi di entrambe le matrici. """

import numpy as np

#Creo un array di 12 numeri equidistanti tra 0 e 1 usando linspace
arr = np.linspace(0, 1, 12) #numero iniziale, finale, numero di elementi voluti
print("L'array iniziale é:")
print(arr) 

#Cambia la forma dell'array a una matrice 3x4.
matrice = arr.reshape(3,4)
print("La matrice 3x4 é:")
print(matrice)

#Genera una matrice 3x4 di numeri casuali tra 0 e 1.
matrice_random = np.random.rand(3, 4)  
print("Matrice 3x4 di numeri casuali tra 0 e 1")
print(matrice_random)

#Calcolo e stampo la somma degli elementi di entrambe le matrici
sum1 = np.sum(matrice)
sum2 = np.sum(matrice_random)
print("Somma elementi prima matrice:", sum1)
print("Somma elementi seconda matrice:", sum2)