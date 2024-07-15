""" Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
Esercizio:
Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array. """

import numpy as np

#creo array
arr = np.arange(10, 50)
print (arr)

#stampo tipo di dato
print("Tipo di dati", arr.dtype)

#cambio tipo di dato
arr = np.array(arr, dtype='int32')
print("Tipo di dati", arr.dtype)

#stampo al forma dell'array
print("Forma", arr.shape)