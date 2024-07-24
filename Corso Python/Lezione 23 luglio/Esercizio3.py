""" Partendo da questo dataframe su kaggle https://www.kaggle.com/datasets/shivamb/netflix-shows analizzate i dati, 
sistemate gli elementi mancanti e verificate se ci sono correlazioni e create un
grafico a mappa di calore. """

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("Lezione 23 luglio/netflix_titles.csv")


print("Dataframe importato: \n",df)

print("Tipi di dati: \n",df.dtypes)

df['duration'].fillna('0 min')
 
df['duration'] = df['duration'].str.extract('(\d+)').astype(float)

filtro_film = df[df['type'] == 'Movie']
filtro_show = df[df['type'] == 'TV Show']

correlazione_film = filtro_film[['duration', 'release_year']].corr()
correlazione_show = filtro_show[['duration', 'release_year']].corr()

print(filtro_film)
print(filtro_show)

print("Correlazione show: \n",correlazione_show)
print("Correlazione film : \n",correlazione_film)


plt.figure()

sns.heatmap(correlazione_film,annot=True)

plt.title('Film : Durata/Anno di uscita')

plt.show()


plt.figure()

sns.heatmap(correlazione_show,annot=True)

plt.title('TV Show : Durata/Anno di uscita')

plt.show()