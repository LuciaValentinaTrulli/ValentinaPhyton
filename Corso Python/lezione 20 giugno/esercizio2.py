#punto 1
#chiedo all'utente di inserire un numero
numero_inserito = float(input("Inserisci un numero: "))

resto = numero_inserito % 2

if resto == 0:
    print("Pari")
else:
    print ("Dispari")


#punto 2
controllo = True

while controllo:
    n = int(input("Inserisci un numero intero positivo: "))
    
    #controllo se positivo
    if n>0:

        #stampo ciclando sugli elementi
        for i in range(n, -1, -1):
            print(i)

        scelta = input("Vuoi ripetere? (si o no): ")
        if scelta.lower() == "no":
            controllo = False
    else:
        print("Il numero non è positivo")



