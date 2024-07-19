""" Esercizio Facile: Calcolo di Statistiche di Base

Testo dell'esercizio:

Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese. 

Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:

La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature """

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def genera_temperature():
    array_temp = np.random.randint(20, 30, size = 30)
    return array_temp

def genera_dataframe(array_temp):
    df = pd.DataFrame(array_temp, columns=['temperature'])
    print(df)
    return df

def media(df):
    mean_temp = df['temperature'].mean()
    print(f"La media delle temperature è: {mean_temp:.2f} °C")
    return mean_temp

def max_min(df):
    max_temp = df['temperature'].max()
    min_temp = df['temperature'].min()
    print (f"La temperatura massima è {max_temp:.2f} °C e quella minima è {min_temp:.2f} °C")
    return max_temp, min_temp

def mediana(df):
    median_temp = df['temperature'].median()
    print(f"La mediana delle temperature è: {median_temp:.2f} °C")
    return median_temp

array_temp=genera_temperature()
df = genera_dataframe(array_temp)
mean_temp = media(df)
max_temp, min_temp = max_min(df)
median_temp = mediana(df)

#grafico

statistiche = ['media', 'min', 'max', 'mediana']
temperature = [mean_temp, min_temp, max_temp, median_temp]

plt.figure()
plt.bar(statistiche, temperature, color='orange')
plt.title('Analisi temperature')
plt.xlabel('Statistiche')
plt.ylabel('Temperature')
plt.show()