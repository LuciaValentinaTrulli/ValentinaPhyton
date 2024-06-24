parole =[]

while True:
    parola = input("Inserisci una parola: ")
    parole.append(parola)

    scelta = input("Vuoi inserire un altra parola?")
    if scelta.lower() == "no":
        break

lunghezze = []
for parola in parole:
    lunghezza = len(parola)
    lunghezze.append(lunghezza)

print("Le lungezze delle parole inserite sono: " , lunghezze)