class Prodotto:                                                             #definisco la classe Prodotto
    def __init__ (self, nome, costo_produzione, prezzo_vendita):            #costruttore della classe Prodotto
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto

class Elettronica:                                                                    #definisco la classe Elettronica
    def __init__ (self, nome, costo_produzione, prezzo_vendita, garanzia):            #costruttore della classe Elettronica
        super().__init__(self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia


class Abbigliamento:                                                                   #definisco la classe Abbigliamento
    def __init__ (self, nome, costo_produzione, prezzo_vendita, materiale):            #costruttore della classe Abbigliamento
        super().__init__(self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale


class Fabbrica:                                                                         #definisco la classe Fabbrica
    inventario ={}                                                                      #attributo della classe

    def aggiungi_prodotto(self):
        while True:
            prodotto = input("Inserisci un prodotto:")
            quantità = input("Inserisci la quantità: ")
            self.inventario[prodotto] = quantità

            scelta = input("Vuoi inserire un altro prodotto? ")
            if scelta.lower() == "no":
                break

    def vendi_prodotto(self):
        fabbrica = Fabbrica()
        prod_venduto = input("Inserisci il nome del prodotto venduto: ")
        for prodotto in fabbrica.inventario:
            if fabbrica.inventario.keys() == prodotto:
                fabbrica.inventario["prod_venduto"] = fabbrica.inventario.quantità - 1
                prodotto.calcola_profitto
                print()






#creazione oggetti e chiamata metodi
prodotto1 = Prodotto("telefono", 200, 400)
print(prodotto1.nome)
elettronica1 = Elettronica(prodotto1, 2)
print(elettronica1.nome)
print (elettronica1.garanzia)
