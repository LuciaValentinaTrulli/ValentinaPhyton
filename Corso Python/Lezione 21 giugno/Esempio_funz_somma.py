#definisco la fuzione somma
def somma(a, b):
    risultato = a + b
    print("La somma è: " , risultato)

#passo alla funzione somma due valori inseriti dall'utente
a = float(input("Scrivi un numero: "))
b = float(input("Scrivi un altro numero: "))
somma(a, b)

#funzione somma di due numeri presi da una lista
numeri = [2,4,6,1,9]
somma(numeri[0], numeri[3])