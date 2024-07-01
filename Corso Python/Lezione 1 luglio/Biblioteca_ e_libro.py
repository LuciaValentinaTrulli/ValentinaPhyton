class Libro:                                    #definisco la classe

    def __init__ (self, titolo, autore, pagine):        #costruttore
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine")



class Biblioteca:
    
    def crea_libro(self):
        libri =[]
        iterazioni = int(input("Quanti libri vuoi inserire? "))
        for i in range(0, iterazioni):
            titolo = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            pagine = input("Inserisci il numero di pagine: ")
            libri.append(Libro(titolo, autore, pagine))


biblio1 = Biblioteca()                  #creo oggetto della classe Biblioteca
biblio1.crea_libro()                    #chiamo il metodo crea libro

        