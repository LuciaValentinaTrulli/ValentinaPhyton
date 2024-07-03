class ContoBancario:
    def __init__(self, titolare):
        self.__titolare = titolare
        self.__saldo = 0
    
    def deposita(self,importo):
        #importo = float(input("Inserisci l'importo da depositare"))
        if importo > 0:
            self.__saldo += importo
            print ("Deposito avvenuto con successo")
        else: 
            print ("Importo inserito negativo")
    
    def preleva(self, importo):
        if importo > 0 and importo < self.__saldo:
            self.__saldo -= importo
            print ("Prelievo avvenuto con successo")
        else: 
            print ("Importo inserito negativo o saldo non sufficiente")

    def visualizza_saldo(self):
        print(f"Il saldo disponibile è: {self.__saldo}")

    
    def get_titolare(self):
        return self.__titolare
    
    def get_saldo(self):
        return self.__saldo
    

    def set_titolare(self, nuovo_titolare):
        if len(nuovo_titolare) > 0:
            self.__titolare = nuovo_titolare
            print(f"Il nuovo titolare è {self.__titolare}")
        else:
            print("Inserita stinga vuota")



conto1 = ContoBancario("Valentina")
conto1.deposita(100)
conto1.preleva(40)
conto1.visualizza_saldo()
conto1.preleva(150)
conto1.visualizza_saldo()
conto1.set_titolare("Maria")