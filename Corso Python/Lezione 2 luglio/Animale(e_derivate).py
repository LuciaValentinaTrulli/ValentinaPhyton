class Animale:                                          #definizione classe base

    def __init__(self, nome, età):                      #costruttore della classe base
        self.nome = nome
        self.età = età
    
    def fai_suono(self):                                #metodo classe base
        print("verso animale")


class Leone(Animale):                                   #definizione classe derivata

    def __init__(self, nome, età, sesso):               #costruttore della classe derivata
        super().__init__(nome, età)
        self.sesso = sesso
       
    def fai_suono(self):                                #sovrascrittura del metodo della classe base
        print("roar")
    
    def caccia(self):                                           #metodo della classe derivata
        print(f"Il leone {self.nome} sta andando a caccia")


leone1 = Leone("Simba", 10, "maschio")                  #creo oggetto della classe leone
leone1.fai_suono()                                      #chiamo metodi della classe leone
leone1.caccia()









