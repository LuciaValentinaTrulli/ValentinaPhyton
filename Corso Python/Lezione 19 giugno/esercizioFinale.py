controllo_ciclo = True

selezione = input("Vuoi avviare il software? Srivi SI o NO ")
lista_prodotti = ["tazza", "borsa", "penna"]
lista_acquisti_utente = []

if selezione.lower() == "si":

    #Gestione Clienti
    while controllo_ciclo:
        selez2 = input("Vuoi vedere i prodotti disponibili? Srivi SI o NO ")
        if selez2.lower() =="si":
            for prodotto in lista_prodotti:
                print(prodotto)

            selez3 = input("Vuoi acquistare un articolo? Srivi SI o NO ")
            if selez3.lower() == "si":
                selez4 = input("Scrivi l'articolo che vuoi acquistare: ")
                lista_acquisti_utente.append(selez4)
                print("Hai acquistato:")
                print(lista_acquisti_utente)
            else: 
                controllo_ciclo = False
                
        else:
            controllo_ciclo = False
            
    #Gestione dell'Inventario
    while controllo_ciclo:
        articolo1 = {
            "nome" : "tazza",
            "prezzo" : 20,
            "quantità" : 5
        }

        articolo2 = {
            "nome" : "borsa",
            "prezzo" : 10,
            "quantità" : 12
        }
        
        articolo3 = {
            "nome" : "penna",
            "prezzo" : 1,
            "quantità" : 20
        }
        articoli_magazzino = [articolo1, articolo2, articolo3]
        scelta = input("Scegli l'operazione da effettuare sugli articoli: Aggiunta (A), Rimozione (R), Modifica (M)")
        if scelta == "A":
            nome_nuovo = input("Inserisci nome articolo:")
            prezzo_nuovo = input("Inserisci prezzo articolo:")
            quantità_nuovo = input("Inserisci quantità articolo:")
            #penso ci voglia un ciclo per modificare l'indice
            articolo4 = {}
            articolo4["nome"] = nome_nuovo
            articolo4["prezzo"] = prezzo_nuovo
            articolo4["quantità"] = quantità_nuovo
            #continuare qui

        

else:
    print("Arrivederci")
    