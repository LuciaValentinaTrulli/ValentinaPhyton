""" Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.

Estrarre e stampare la seconda colonna della matrice.

Estrarre e stampare la terza riga della matrice.

Calcolare e stampare la somma degli elementi della diagonale principale della matrice. """

import numpy as np

#Creo una matrice 5x5 contenente numeri interi sequenziali da 1 a 25
arr = np.arange(1,26)
matrice = arr.reshape(5,5)
print("Matrice iniziale:")
print(matrice)

#Estraggo la seconda colonna della matrice
seconda_colonna= matrice[:,1]
print("Seconda colonna della matrice")
print(seconda_colonna)

#Estraggo la terza riga della matrice
terza_riga= matrice[2,:]
print("Terza riga della matrice")
print(terza_riga)

#Calcolo e stampo la somma degli elementi della diagonale principale della matrice
diagonale = np.diagonal(matrice)
somma_diagonale = np.sum(diagonale)
print ("La somma degli elementi della diagonale principale è", somma_diagonale)