""" Creare un array unidimensionale con 50 valori compresi tra 1 e 1.000 e dopo dovete eseguire le seguenti 
operazioni:
- calcolo della media;
- calcolo della deviazione standard;
- trasformarlo in un array 5x10 """

import numpy as np

# Funzione per creare un array unidimensionale con 50 valori compresi tra 1 e 1000
def crea_array():
    array = np.random.randint(1, 1001, 50)
    print("Array unidimensionale:", array)
    return array

# Funzione per calcolare la media dei valori dell'array
def calcola_media(array):
    media = np.mean(array)
    print("Media dell'array:", media)
    return media

# Funzione per calcolare la deviazione standard dei valori dell'array
def calcola_deviazione_standard(array):
    deviazione_standard = np.std(array)
    print("Deviazione standard dell'array:", deviazione_standard)
    return deviazione_standard

# Funzione per trasformare l'array unidimensionale in un array 5x10
def trasforma_array(array):
    array_5x10 = array.reshape((5, 10))
    print("Array 5x10:\n", array_5x10)
    return array_5x10


def menu():
    array = None
    while True:
        print("\nMenu:")
        print("1. Crea array unidimensionale")
        print("2. Calcola media dell'array")
        print("3. Calcola deviazione standard dell'array")
        print("4. Trasforma array in 5x10")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        if scelta == '1':
            array = crea_array()
        elif scelta == '2':
            if array is not None:
                calcola_media(array)
            else:
                print("Per favore, crea prima un array.")
        elif scelta == '3':
            if array is not None:
                calcola_deviazione_standard(array)
            else:
                print("Per favore, crea prima un array.")
        elif scelta == '4':
            if array is not None:
                trasforma_array(array)
            else:
                print("Per favore, crea prima un array.")
        elif scelta == '0':
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Per favore, seleziona un'opzione valida.")


menu()
