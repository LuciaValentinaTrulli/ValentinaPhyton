class Posto:

    def __init__(self, numero, fila, occupato):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = occupato
    
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_occupato(self):
        return self.__occupato

    def prenota(self, numero, fila):                                #creo oggetto teatro nella classe Posti
        teatro = Teatro()
        for posto in teatro.get_posti():
            if numero == posto[0] and fila == posto[1]:
                if posto[2] == False:
                    posto[2] == True
                    print("Hai prenotato il posto")
                else:
                    print("Posto già occupato")
            else:
                print("Posto non trovato")


    def libera(self,numero, fila):
        teatro = Teatro()
        for posto in teatro.get_posti():
            if numero == posto[0] and fila == posto[1]:
                if posto[2] == True:
                    posto[2] == False
                    print("Hai liberato il posto")
                else:
                    print("Posto già libero")
            else: #lo stampa più volte
                print("Posto non trovato")


class PostoVIP(Posto):

    def __init__(self, numero, fila, occupato, servizi_extra):
        super().__init__(numero, fila, occupato)
        self.__servizi_extra = servizi_extra

    def prenota(self, numero, fila):
        super().prenota(numero, fila)
        servizi = input("Scegli il servizio extra che vuoi aggiungere: lounge, priorità")
        if servizi == "lounge":
            print("Accesso al lounge aggiunto")
        elif servizi == "priorità":
            print("Priorità aggiunta")
        else:
            print("Nessun servizio extra aggiunto")
            exit()


class PostoStandard(Posto):

    def __init__(self, numero, fila, occupato, costo_prenotazione):
        super().__init__(numero, fila, occupato)
        self.__costo_prenotazione = costo_prenotazione

    def costo_prenotazione(self):
        return self.__costo_prenotazione



class Teatro:
        
    def __init__(self):
        self.__posti = [[1, "a", False], [2, "a", False]]
    
    def get_posti(self):
        return self.__posti
    
    def prenota_posto(numero, fila):
        pass

    def stampa_posti_occupati(self):
        posti_occupati =[]
        for posto in self.__posti:
            if posto[2] == True:
                posti_occupati.append(posto)
                print(f"I posti occupati sono {posti_occupati}")



posto1 = Posto(3, "a", True)
posto1.prenota(3, "a")
