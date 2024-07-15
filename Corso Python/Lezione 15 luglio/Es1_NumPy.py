""" Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.
Esercizio:
Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array. """

import numpy as np

def menu():
    print("1. Crea un array")
    print("2. Verifica il tipo di dato dell'array")
    print("3. Modifica il tipo di dato dell'array")
    print("4. Verifica la forma dell'array")
    print("0. Esci")


while True:
    menu()
    scelta=input("Inserisci scelta: ")
    if scelta=="1":

        #creo array
        arr = np.arange(10, 50)
        print("Array creato")
        print (arr)  

    elif scelta=="2":

        #stampo tipo di dato
        print("Tipo di dati", arr.dtype)

    elif scelta=="3":

        #cambio tipo di dato
        arr = np.array(arr, dtype='int32')
        print("Tipo di dati", arr.dtype)

    elif scelta=="4":

        #stampo al forma dell'array
        print("Forma", arr.shape)

    elif scelta=="0":

        break

    else:
        
        print("Scelta sbagliata")