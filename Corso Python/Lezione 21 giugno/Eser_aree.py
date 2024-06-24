#definisco una funzione che calcola l'area di un triangolo
def area_triangolo():
    aree_triangoli = []
    while True:
        base = float(input("Scrivi il valore della base del triangolo: "))
        altezza = float(input("Scrivi il valore dell'altezza del triangolo: "))
        area = (base * altezza) / 2
        aree_triangoli.append(area)
        print("L'area del triangolo è: " , area)

        #chiedo all'utente se vuole terminare
        scelta = input("Vuoi uscire dal programma? ")
        if scelta.lower() == "si":
            break

    print("Le aree calcolate sono: ", aree_triangoli)
    return aree_triangoli



#definisco una funzione che calcola l'area di un quadrato
def area_quadrato():
    aree_quadrati = []
    while True:
        lato = float(input("Scrivi il valore del lato del quadrato: "))
        area = lato ** 2
        aree_quadrati.append(area)
        print("L'area del quadrato è: " , area)

        #chiedo all'utente se vuole terminare
        scelta = input("Vuoi uscire dal programma? ")
        if scelta.lower() == "si":
            break

    print("Le aree calcolate sono: ", aree_quadrati)
    return aree_quadrati


#definisco una funzione che calcola l'area di un rettangolo
def area_rettangolo():
    aree_rettangoli = []
    while True:
        base = float(input("Scrivi il valore della base del rettangolo: "))
        altezza = float(input("Scrivi il valore dell'altezza del rettangolo: "))
        area = base * altezza
        aree_rettangoli.append(area)
        print("L'area del rettangolo è: " , area)

        #chiedo all'utente se vuole terminare
        scelta = input("Vuoi uscire dal programma? ")
        if scelta.lower() == "si":
            break

    print("Le aree calcolate sono: " , aree_rettangoli)
    return aree_rettangoli



#richiamo le funzioni
area_triangolo()
area_quadrato()
area_rettangolo()