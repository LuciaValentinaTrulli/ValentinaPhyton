""" Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
Estrai la sotto-matrice centrale 4x4 dalla matrice originale.
Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
Stampa la matrice originale, la sotto-matrice centrale estratta, la matrice invertita, la diagonale principale e la matrice invertita modificata.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre, modificare e manipolare sotto-matrici e array, applicando operazioni avanzate come 
l'inversione delle righe e la sostituzione condizionale degli elementi. """

import numpy as np

#creo matrice random 6 x 6
matrice_random = np.random.randint(1, 100, size=(6,6))
print("La matrice generata randomicamente è:")
print (matrice_random)

# Estraggo la sotto-matrice centrale 4x4 dalla matrice originale
# Slicing su rige e colonne
print("La matrice centrale 4x4 é:")
print(matrice_random[1:5, 1:5]) 

#Inverti le righe della matrice estratta (cioè, la prima riga diventa l'ultima, la seconda diventa la penultima, e così via).
""" prima_riga = matrice_random[1:5, 1:5][0]
seconda_riga = matrice_random[1:5, 1:5][1]
print(prima_riga)
print(seconda_riga) """
matrice_invertita = np.flipud(matrice_random[1:5, 1:5])
print("La matrice invertita é:")
print(matrice_invertita)

#Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
diagonale = np.diagonal(matrice_invertita)
print("La diagonale della matrice invertita è:")
print(diagonale)

#Sostituisci tutti gli elementi della matrice invertita che sono multipli di 3 con il valore -1.
matrice_invertita[matrice_invertita%3==0]=-1
print("Matrice con valori sostituiti")
print(matrice_invertita)