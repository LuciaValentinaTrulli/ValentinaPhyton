""" Descrizione: Crea un array utilizzando linspace, cambia la sua forma con reshape, 
genera un array casuale e calcola la somma degli elementi.

Esercizio:
Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.
Cambia la forma dell'array a una matrice 3x4.
Genera una matrice 3x4 di numeri casuali tra 0 e 1.
Calcola e stampa la somma degli elementi di entrambe le matrici. """

import numpy as np

def crea_arr_linspace():
    #Creo un array di 12 numeri equidistanti tra 0 e 1 usando linspace
    arr = np.linspace(0, 1, 12) #numero iniziale, finale, numero di elementi voluti
    print("L'array iniziale é:")
    print(arr) 

def cambia_forma_array(arr):
    #Cambia la forma dell'array a una matrice 3x4.
    matrice = arr.reshape(3,4)
    print("La matrice 3x4 é:")
    print(matrice)
    return matrice

def crea_mat_random():
    #Genera una matrice 3x4 di numeri casuali tra 0 e 1.
    matrice_random = np.random.rand(3, 4)  
    print("Matrice 3x4 di numeri casuali tra 0 e 1")
    print(matrice_random)
    return matrice_random

def somma(matrice, matrice_random):
    #Calcolo e stampo la somma degli elementi di entrambe le matrici
    sum1 = np.sum(matrice)
    sum2 = np.sum(matrice_random)
    print("Somma elementi prima matrice:", sum1)
    print("Somma elementi seconda matrice:", sum2)



def menu():
    print("1. Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace")
    print("2. Cambia la forma dell'array a una matrice 3x4")
    print("3. Genera una matrice 3x4 di numeri casuali tra 0 e 1")
    print("4. Calcola e stampa la somma degli elementi di entrambe le matrici")
    print("0. Esci")


while True:
    menu()
    scelta=input("Inserisci scelta: ")
    if scelta=="1":
        crea_arr_linspace()
    elif scelta=="2":
        inizio = input("Inserisci numero iniziale")
        fine = input("Inserisci numero finale")
        num_elem = input("Inserisci numero di elementi voluti") 
        arr = np.linspace(inizio, fine, num_elem)
        cambia_forma_array(arr)
    elif scelta=="3":
        crea_mat_random()
    elif scelta=="4":
        inizio = input("Inserisci numero iniziale")
        fine = input("Inserisci numero finale")
        num_elem = input("Inserisci numero di elementi voluti") 
        arr = np.linspace(inizio, fine, num_elem)
        matrice = cambia_forma_array(arr)
        matrice_random = crea_mat_random()
        somma(matrice, matrice_random)
    elif scelta=="0":
        break
    else:
        print("Scelta sbagliata")