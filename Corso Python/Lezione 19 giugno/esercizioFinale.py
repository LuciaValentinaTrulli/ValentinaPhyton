controllo_ciclo = True

selezione = input("Vuoi avviare il software? Srivi SI o NO")
lista_prodotti = ["1.tazza", "2.borsa", "3.penna"]
lista_acquisti_utente = []

if selezione == "SI":
    while controllo_ciclo:
        selez2 = input("Vuoi vedere i prodotti disponibili?")
        if selez2.lower() =="si":
            print(lista_prodotti)
            selez3 = input("Vuoi acquistare un articolo?")
            if selez3.lower() == "si":
                selez4 = int(input("Scrivi il numero dell'articolo che vuoi acquistare"))
                lista_acquisti_utente.append(selez4)
                break
            
        else:
            break
            

else:
    print("Arrivederci")
    