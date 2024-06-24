numeri =[]

while True:
    numero = input("Inserisci un numero o scrivi \"esci\" per uscire: ")

    if numero.lower() == "esci":
        break
    else: 
        if (numero <=0):
            print("numero non valido")
            break
        else:
            numeri.append(int(numero))    



for numero in numeri:
        print("*" * numero)

