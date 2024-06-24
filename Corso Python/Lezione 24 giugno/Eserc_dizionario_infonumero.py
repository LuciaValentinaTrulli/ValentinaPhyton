""" Scrivete un programma che chiede un numero all’utente e
restituisce un dizionario con il quadrato del numero, se è pari o
dispari e quante cifre contiene.
Esempio:
Numero 12
Risultato
{‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 } """


numero = input("Inserisci un numero: ")

info_numero = {}


info_numero["quadrato"] = float(numero)**2

if float(numero)%2 == 0:
    info_numero["pari o dispari"] = "pari"
else:
    info_numero["pari o dispari"] = "dispari"

info_numero["cifre"] = len(numero)



print(info_numero)