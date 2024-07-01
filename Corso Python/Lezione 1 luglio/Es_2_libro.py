class Libro:                                    #definisco la classe

    def __init__ (self, titolo, autore, pagine):        #costruttore
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine")


libro1 = Libro("Divina Commedia", "Dante", 1000)            #creo un'istanza
libro1.descrizione()                                        #chiamo il metodo descrizione