import statistics
class Dati:
    vendite = []

    def inserimento_dati(self):
       # controllo = True
        #while controllo:
            importi = input("Inserisci una serie di importi di vendita separati da spazi: ")
            lista_importi = importi.split(" ")
            lista_imp_int = []
            try:
                for importo in lista_importi:
                    importo_int = int(float(importo))
                    lista_imp_int.append(importo_int)
                print(lista_imp_int)
               # controllo = False
                return lista_imp_int
                
            except ValueError as errore:
                print("Inserimento non valido, errore: " , errore)
                print("Reinserire i dati")


    def totale(self):
        totale = sum(self.inserimento_dati())
        print("Il totale delle vendite inserite é: ", totale)
    
    def media(self):
        media = statistics.mean(self.inserimento_dati())
        print("La media delle vendite inserite é: ", media)






dati = Dati()
dati.inserimento_dati()
dati.totale()
dati.media()
