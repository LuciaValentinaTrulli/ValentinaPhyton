from random import randint

#definisco una funzione che genera numeri casuali
def genera_numero():
    return(randint(1, 100))


#potrei definire una funzione che confronta due numeri
#def confronto(numero1, numero2):


#definisco la funzione
def indovina_numero():    

    print("Indovina un numero compreso tra 1 e 100")
    num_generato = genera_numero()
    controllo =True
    while controllo:
        num_inserito = int(input("Inserisci un numero: "))

        if num_inserito < num_generato:
            print ("Il numero da indovinare è più grande")

            #chiedo all'utente se vuole uscire dal programma
            scelta = input("Vuoi uscire? ")
            if scelta.lower() == "si":
                controllo = False

        elif num_inserito > num_generato:
            print ("Il numero da indovinare è più piccolo")

            #chiedo all'utente se vuole uscire dal programma
            scelta = input("Vuoi uscire? ")
            if scelta.lower() == "si":
                controllo = False           

        else:
            print ("Hai indovinato!")
            controllo = False


#chiamo la funzione
indovina_numero()                                 