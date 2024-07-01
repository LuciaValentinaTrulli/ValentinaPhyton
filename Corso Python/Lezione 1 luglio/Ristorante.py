class Ristorante:                                   #definisco la classe

    aperto = False                                  #attributi della classe
    menu = {}

    def __init__ (self, nome, tipo_cucina):         #costruttore
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    
    def descrivi_ristorante(self):
        print("Il ristorante", self.nome, "serve cucina", self.tipo_cucina)


    def stato_apertura(self):
        print("Il ristorante é ")
        if self.aperto:
            print("aperto")
        else:
            print("chiuso")
    

    def apri_ristorante(self):
        self.aperto = True
        print("Il ristorante è aperto")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print("Il ristorante è chiuso")
    
    def aggiungi_al_menu(self):
        piatto = input("Inserisci un piatto:")
        prezzo = input("Inserisci il prezzo: ")
        self.menu[piatto] = prezzo

    def togli_dal_menu(self):
        piatto = input("Inserisci il piatto da eliminare:")
        self.menu.pop(piatto)


    def stampa_menu(self):
        print("Il menu é: ", self.menu)




#reo un oggetto e richiamo  i metodi
ristorante1 = Ristorante("Da Gianni", "italiana")
ristorante1.descrivi_ristorante()
ristorante1.stato_apertura()
ristorante1.apri_ristorante()
ristorante1.stato_apertura()
ristorante1.stampa_menu()
ristorante1.aggiungi_al_menu()
ristorante1.stampa_menu()
ristorante1.togli_dal_menu()