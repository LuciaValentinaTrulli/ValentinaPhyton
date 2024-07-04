class Libro:                                    #definisco la classe Libro

    def __init__ (self, titolo, autore, pagine):        #costruttore
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print("Il libro", self.titolo, "è stato scritto da", self.autore, "e ha", self.pagine, "pagine")



class Biblioteca:                               #definisco la classe Biblioteca

    libri =[]

    def crea_libro(self):
        iterazioni = int(input("Quanti libri vuoi inserire? "))
        for i in range(0, iterazioni):
            titolo = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            pagine = input("Inserisci il numero di pagine: ")
            libro = Libro(titolo, autore, pagine)          #creo oggetto di tipo Libro con input utente
            self.libri.append(libro)                       #aggiungo il libro alla lista libri
            print("Il libro", libro.titolo, "è stato aggiunto alla biblioteca")
            


biblio1 = Biblioteca()                  #creo oggetto della classe Biblioteca
biblio1.crea_libro()                    #chiamo il metodo crea_libro
print("Nella biblioteca ci sono", len(biblio1.libri), "libri")
        