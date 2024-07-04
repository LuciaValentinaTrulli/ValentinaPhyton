class Veicolo:
    def __init__(self, marca, modello, anno, accensione):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = accensione
    
    def accendi(self):
        self.__accensione == True
        print("Il veicolo è acceso")
    
    def spegni(self):
        self.__accensione == False
        print("Il veicolo è spento")


class Auto(Veicolo):
    def __init__(self, marca, modello, anno, accensione, numero_porte):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte = numero_porte
    
    def suona_clacson(self):
        print(f"L'auto {self.__marca} {self.__modello} sta suonando il clacson")
    
    def __get_marca(self):
        return self.__marca
    
    def __set_marca(self, nuova_marca):
        self.__marca = nuova_marca



class Furgone(Veicolo):
    def __init__(self, marca, modello, anno, accensione, capacità_carico):
        super().__init__(marca, modello, anno, accensione)
        self.__capacità_carico = capacità_carico
    
#continuare qui








class GestoreParcoVeicoli(Auto, Furgone):
    def __init__(self):
        self.__veicoli = []
    
    def set_marca(self, veicolo, nuova_marca):
        veicolo.__set_marca(nuova_marca)
        #return super().__set_marca(nuova_marca)



veicolo_prova = Veicolo("Fiat", "Punto", 2020, True)
gestore = GestoreParcoVeicoli()
gestore.set_marca(veicolo_prova, "Ford")

