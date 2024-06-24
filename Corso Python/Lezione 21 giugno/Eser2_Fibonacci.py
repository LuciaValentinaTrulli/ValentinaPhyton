#definisco la fuzione somma
def somma(a, b):
    risultato = a + b
    return(risultato)


#definisco la fuzione sequenza di Fibonacci
def sequenza_Fibonacci():
    N = int(input("Inserisci il numero fino al quale vuoi ottenere la sequenza: "))
    print("La sequenza di Fibonacci fino al numero inserito è: ")
    #qui dovrebbe verificare che il num non sia zero o uno ma abbastanza ovvio
    print("0")
    print("1")

    a = 0
    b = 1

    while True:
        c = somma(a,b)

        if c > N:
            break

        else:
            print(c)
            a = b
            b = c


#richiamo la funzione
sequenza_Fibonacci()
    