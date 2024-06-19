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
                print(lista_acquisti_utente)
            else:
                break
        else:
            break
    
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
    