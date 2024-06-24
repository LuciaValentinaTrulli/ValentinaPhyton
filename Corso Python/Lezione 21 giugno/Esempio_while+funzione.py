controllo = True

#definisco una funzione che saluta
def saluta():
    nome = input("Scrivi il nome della persona che vuoi salutare: ")
    print("Ciao " + nome)



#definisco una funzione controllore
def controllore():
    scelta = input("Vuoi uscire? ")
    if scelta == "si":
        controllo = False     #in realtà non esce e non si può mettere neanche il break perchè non è un ciclo


while controllo:
    #x = input("Scrivi il nome della persona che vuoi salutare: ")
    saluta()
    controllore()