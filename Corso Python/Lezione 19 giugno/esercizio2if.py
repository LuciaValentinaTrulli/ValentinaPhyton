nomeUtente = str(input("Inserisci nome utente:"))
password = str(input("Inserisci password:"))

nomeUtenteCorretto = "admin"
passwordCorretta = "12345"

if (nomeUtente == nomeUtenteCorretto and password == passwordCorretta):
    print("Benvenuto")
    domandaSegreta = input ("Scegli come domanda segreta: colore preferito (C) o animale preferito (A):")
    if domandaSegreta == "C":
        colorePreferito = input ("Inserisci il tuo colore preferito:")
    elif domandaSegreta == "A":
        animalePreferito = input ("Inserisci il tuo animale preferito:")


    scelta = input("Se vuoi modificare il mone utente premi 1, se vuoi modificare la password premi 2, altrimenti premi 0: ")
    if scelta == "1" :
        nuovoNome = input("Inserisci nuovo nome:")
        nomeUtente = nuovoNome
        print("nome cambiato")
    elif scelta == "2" :
        nuovaPassword = input("Inserisci nuova password:")
        password = nuovaPassword
        print("password cambiata")
    elif scelta == "0":
        pass
else:
    print("credenziali errate")