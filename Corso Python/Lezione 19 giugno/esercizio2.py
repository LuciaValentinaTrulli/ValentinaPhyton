lista = ["Mario", "Vale", "Carla"]

scelta = input("Scegli un opzione tra Aggiungi, Rimuovi, Modifica, Esci:")

if scelta == "Aggiungi":
    elemento=input("inserisci elemento da aggiungere")
    lista.append(elemento)
    print("elemento aggiunto")
elif scelta == "Rimuovi":
    elemento=input("inserisci elemento da eliminare")
    if elemento in lista:
        lista.remove(elemento)
        print("elemento rimosso")
elif scelta == "Modifica" :
    elemento=input("inserisci elemento da modificare")
    nuovoElemento=input("inserisci nuovo elemento")
    lista.replace(elemento,nuovoElemento)
    print("elemento modificato")
elif scelta == "Esci":
    pass
else:
    print("opzione non valida")