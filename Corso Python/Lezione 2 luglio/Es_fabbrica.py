class Prodotto:                                                             #definisco la classe Prodotto
    def __init__ (self, nome, costo_produzione, prezzo_vendita):            #costruttore della classe Prodotto
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    

    def calcola_profitto(self):
        profitto = self.prezzo_vendita - self.costo_produzione
        return profitto

class Elettronica(Prodotto):                                                          #definisco la classe derivata Elettronica
    def __init__ (self, nome, costo_produzione, prezzo_vendita, garanzia):            #costruttore della classe Elettronica
        Prodotto.__init__ (self, nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia


class Abbigliamento(Prodotto):                                                         #definisco la classe derivata Abbigliamento
    def __init__ (self, nome, costo_produzione, prezzo_vendita, materiale):            #costruttore della classe Abbigliamento
        Prodotto.__init__ (self, nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale


class Fabbrica:                                                                         #definisco la classe Fabbrica
    inventario ={}
    prodotti = []                                                                      #attributo della classe

    def aggiungi_prodotto(self):
        while True:
            nome = input("Inserisci il nome del prodotto:")
            costo_produzione = int(input("Inserisci il costo di produzione del prodotto:"))
            prezzo_vendita = int(input("Inserisci il prezzo del prodotto:"))
            prodotto = Prodotto(nome, costo_produzione, prezzo_vendita)  #creo oggetto Prodotto e lo aggiungo alla lista prodotti
            self.prodotti.append(prodotto)

            quantità = int(input("Inserisci la quantità: "))
            self.inventario[nome] = quantità                    #salvo prodotto e quantità nel dizionario
            print(f"L'articolo {nome} è stato aggiunto all'inventario")

            scelta = input("Vuoi inserire un altro prodotto? ")
            if scelta.lower() == "no":
                break

    def vendi_prodotto(self):
        nome_prod_venduto = input("Inserisci il nome del prodotto venduto: ")
        for chiave in self.inventario.keys():
            if chiave == nome_prod_venduto:
                self.inventario[nome_prod_venduto] -= 1                  #diminuisco di uno la quantità disponibile del prodotto
                print(f"Un articolo {nome_prod_venduto} tolto dall'inventario")

                for prodotto in self.prodotti:                             #cerco il prodotto nella lista prodotti e stampo il profitto relativo
                    if prodotto.nome == nome_prod_venduto:
                        print(f"Il profitto realizzato con questa vendita è: {prodotto.calcola_profitto()} euro")
       
        if nome_prod_venduto not in self.inventario.keys(): 
            print("Prodotto non trovato")

    def resi_prodotto(self):
        nome_prod_reso = input("Inserisci il nome del prodotto reso: ")
        for chiave in self.inventario.keys():
            if chiave == nome_prod_reso:
                self.inventario[nome_prod_reso] += 1                  #aumento di uno la quantità disponibile del prodotto
                print(f"Un articolo {nome_prod_reso} aggiunto all'inventario")
    
        if nome_prod_reso not in self.inventario.keys():
            print("Articolo non presente in inventario, è necessario aggiungerlo.")

            costo_produzione = int(input("Inserisci il costo di produzione del prodotto:"))
            prezzo_vendita = int(input("Inserisci il prezzo del prodotto:"))
            prodotto = Prodotto(nome_prod_reso, costo_produzione, prezzo_vendita)  #creo oggetto Prodotto e lo aggiungo alla lista prodotti
            self.prodotti.append(prodotto)

            self.inventario[nome_prod_reso] = 1                             #aggiungo l'articolo nell'inventario
            print (f"Un articolo {nome_prod_reso} aggiunto all'inventario")      




#testo funzionamento classe derivata (funziona)
elettronica1 = Elettronica("cellulare", 200, 400, 2)
print("Il profitto relativo all'articolo", elettronica1.nome, "è:", elettronica1.calcola_profitto(), "euro")
print("La garanzia è di", elettronica1.garanzia, "anni")

#testo funzionamento classe Fabbrica(funziona)
fabbrica = Fabbrica()
fabbrica.aggiungi_prodotto()
print("Ecco gli articoli disponibili e le loro quantità:", fabbrica.inventario)
fabbrica.vendi_prodotto()
print("Ecco gli articoli disponibili e le loro quantità:", fabbrica.inventario)
fabbrica.resi_prodotto()
print("Ecco gli articoli disponibili e le loro quantità:", fabbrica.inventario)
print(len(fabbrica.prodotti))
