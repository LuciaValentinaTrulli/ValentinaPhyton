#richiedo gli input necessari
nome = input("Inserisci il tuo nome: ")
anno_nascita = int(input("Inserisci il tuo anno di nascita: "))
giorno = int(input("Inserisci il giorno della settimana in cui siamo, espresso con un numero: "))



#stampo la frase
print(f"Il tuo nome é {nome}, hai {2024-anno_nascita} anni e mancano {6-giorno} giorni al weekend")

#il cast si può fare anche direttamente nella stringa 2024 - int(anno_nascita)

#se i dati per es come età mi possono servire, salvo in variabili e poi printo la variabile

#si potrebbero mettere anche controlli su giorno della settimana