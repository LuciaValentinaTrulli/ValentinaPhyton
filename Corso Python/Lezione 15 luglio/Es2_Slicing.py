""" Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing. """

import numpy as np

#creo array random di 20 elementi tra 10 e 50
array_random = np.random.randint(10, 50, 20)
print("L'array generato randomicamente è:")
print (array_random)

#stampo i primi 10 numeri
print("I primi dieci numeri dell'array sono:")
print(array_random[:10])

#stampo gli ultimi 5 numeri
print("Gli ultimi cinque numeri dell'array sono:")
print(array_random[-5:])

#stampo da indice 5 a 15 escluso
print("Gli elementi dall'indice 5 all'indice 15 (escluso) sono:")
print(array_random[5:15])

#stampo ogni terzo elemento dell'array
indici = [2, 5, 8, 11, 14, 17]              #Fancy Indexing
print ("Gli elementi terzo, sesto, nono ecc sono:")
print(array_random[indici])
print(array_random[2::3])  #slicing con passo 3, equivalente


#assegno il valore 99 agli elementi dall'indice 5 all'indice 10 (escluso)
array_random[5:10] = 99
print("L'array modificato è:")
print(array_random)