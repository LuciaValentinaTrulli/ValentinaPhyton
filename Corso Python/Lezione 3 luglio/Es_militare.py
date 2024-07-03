class UnitaMilitare:

    def __init__(self, nome, numero_soldati):                                      #costruttore della classe base
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} sta avanzando")
    
    def attacca(self):
        print(f"L'unità {self.nome} sta attaccando")
    
    def ritira(self):
        print(f"L'unità {self.nome} si sta ritirando")


class Fanteria(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati):
       super().__init__(nome, numero_soldati)
       self.lista_fanteria = []

    def crea_fanteria(self):
        self.lista_fanteria.append(Fanteria)
"""         contatore = 0
        while True:
            x = input("Vuoi creare un'unità di fanteria? ")
            if x.lower() == "si":
                contatore+=1
                fanteria, contatore = Fanteria()
                self.lista_fanteria.append(fanteria, contatore)
                
            else:
                break
            
            return contatore """






class ControlloMilitare(UnitaMilitare, Fanteria):
    tipo_unità_registrate = ["fanteria"]
    numero_unità_registrate = [0]

    def __init__(self, nome, numero_soldati, ):
        UnitaMilitare.__init__(self, nome, numero_soldati)
        Fanteria.__init__(self, nome, numero_soldati)

    
    def registra_unità(self):
        scelta = print("Che tipo di unità vuoi aggiungere? (fanteria)")
        if scelta.lower() == "fanteria":
            self.crea_fanteria()
            self.numero_unità_registrate[0]+=1
        else:
            pass