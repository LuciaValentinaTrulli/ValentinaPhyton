num1 = float(input("Inserisci il primo numero: "))
num2 = float(input("Inserisci il secondo numero: "))
operazione = input("Scrivi l'operazione che vuoi effettuare tra: somma, sottrazione, moltiplicazione, divisione: ")



if operazione.lower() == "somma":
    risultato = num1 + num2
    print("Il risultato é: " , risultato)
elif operazione.lower() == "sottrazione":
    risultato = num1 - num2
    print("Il risultato é: " , risultato)
elif operazione.lower() == "moltiplicazione":
    risultato = num1 * num2
    print("Il risultato é: " , risultato)
elif operazione.lower() == "divisione":
    if num2 ==0:
        print("Operazione non possibile, divisore pari a zero")
    else:
        risultato = num1 / num2
        print("Il risultato é: " , risultato)
else:
    print("Operazione scelta non valida")