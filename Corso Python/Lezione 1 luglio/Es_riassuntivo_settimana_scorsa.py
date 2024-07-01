#Programma gestione e-commerce

#importo la libreria per criptare le credenziali degli utenti
import pickle


#funzione per leggere il db utenti e decriptarlo
def leggi_db_utenti():
    with open("db_utenti.bin", "rb") as file:
        db_utenti = pickle.loads(file.read())
    return db_utenti



#funzione per verificare l'esistenza del db utenti
def verifica_db_utenti():
    try:
        db_utenti = leggi_db_utenti()
    except:
        user = input("Inserisci un nome utente: ")
        psw = input("Inserisci una password: ")
        dizionario = {"amministratori":{user:psw},"utenti":{}}
        scrivi_utenti(dizionario)
        db_utenti = leggi_db_utenti()   

    return db_utenti


#funzione per scrivere le credenziali degli utenti criptate in un file.bin
def scrivi_utenti(dato):
    dato_b = pickle.dumps(dato)
    with open("db_utenti.bin", "wb") as file:
            file.write(dato_b)                                         #o append?



db_utenti = verifica_db_utenti()

#funzione per creazione di utenti
def crea_utente():
    ruolo = input("Scrivi 1 per inserire un amministratore o 2 per inserire un utente: ")
    ruolo_ok = True
    #determino la sezione del dizionario utenti in cui accedere
    if ruolo == "1":
        chiave = "amministratori"
    elif ruolo == "2":
        chiave = "utenti"
    else:
        print("Ruolo non valido!")
        ruolo_ok = False
    
    if ruolo_ok:
        user = input("Inserisci user: ")
        if user in db_utenti[chiave]:
            print("Utente già presente!")
        else:
            psw = input("Inserisci password: ")
            db_utenti[chiave][user]= psw
            scrivi_utenti(db_utenti)
            print("Utente aggiunto")


