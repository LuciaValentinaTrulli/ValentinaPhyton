class Animale:

    def __init__(self, nome, età):
        self.nome = nome
        self.età = età
    
    def fai_suono():
        print("verso animale: ")


class Leone(Animale):

    def __init__(self, nome, età, criniera):
        super().__init__(nome, età)
        self.criniera = criniera
       


    def fai_suono():
        super().fai_suono()
        print("verso animale: roar")


leone1 = Leone("Simba", 10, "si")
print(leone1.nome, leone1.età, leone1.criniera)
leone1.fai_suono()









