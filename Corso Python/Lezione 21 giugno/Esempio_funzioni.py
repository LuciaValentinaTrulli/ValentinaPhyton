#definisco una funzione con parametro nome
def saluta(nome):
    print("Ciao " + nome)


#richiamo la funzione indicando un argomento (valore) o assegnando un valore alla variabile 
# o passando alla funzione l'input dell'utente
saluta("Maria")

x="Antonio"
saluta(x)

x = input("Scrivi il nome della persona che vuoi salutare: ")
saluta(x)

x = input("Scrivi un altro nome da salutare: ")
saluta(x)


#funzione senza parametro
def concludi():
    print("procedimento finito")

concludi()