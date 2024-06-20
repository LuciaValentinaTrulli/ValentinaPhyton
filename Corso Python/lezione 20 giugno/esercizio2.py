#punto 1
#chiedo all'utente di inserire un numero
numero_inserito = float(input("Inserisci un numero: "))

resto = numero_inserito % 2

if resto == 0:
    print("Pari")
else:
    print ("Dispari")


#punto 2
#chiedo all'utente di inserire un numero
n = int(input("Inserisci un numero intero positivo: "))

#controllo se positivo
if n>0:

    range(n, -1, -1)

    #stampo ciclando sugli elementi
    for i in range():
        print(i)

    scelta = input("Vuoi ripetere? (Si o no): ")
    while scelta.lower() == "si":
        numero_inserito = int(input("Inserisci un numero: "))

        range(n, -1, -1)

        for i in range():
            print(i)
else:
    print("Il numero non è positivo")