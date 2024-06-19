età = input("Inserisci la tua età:")
if età < "18" :
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film")

num1 = input("Inserisci un numero:")
num2 = input("Inserisci un altro numero:")
operazione = input("Scegli l'operazione da eseguire tra addizione (+), sottrazione (-), moltiplicazione (*) e divisione (/):")
if operazione == "+":
    risultato = (num1 + num2)
    print(risultato)
elif operazione == "-":
    risultato = (num1 - num2)
    print(risultato)
elif operazione == "*":
    risultato = (num1 * num2)
    print(risultato)
elif operazione == "/":
    if num2 == 0:
        print("Errore: divisione per zero")
    else:
        risultato = (num1 / num2)
        print(risultato)
else:
    print("Operazione non valida")