""" Partendo da questo dataframe su kaggle https://www.kaggle.com/datasets/vikrishnan/boston-house-prices :
-analizzate il tipo di dati,
- sistemate gli elementi mancanti - verificate se ci sono correlazioni - create un grafico a mappa di calore. """

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class Housing:

    def __init__(self, path):
        etichette = ["crim", "zn", "indus", "chs", "nox", "rm", "età", "dis", "rad", "tax", "ptratio", "bk", "lstat%", "medv"]
        self.df = pd.read_csv(path, sep='\s+', names=etichette)  #regex dove \s indica spazi vuoti, + per dire anche più di uno
        self.path = path

    def scrivi_csv(self):
        self.df.to_csv("Lezione 23 luglio/housing_pulito.csv")

    def mostra_df(self):
        print(f"Anteprima Dataset:\n{self.df}")
    
#analizzo dati
    def mostra_info(self):
        print(f"Descrizione:\n{self.df.describe()}")
        print(f"")

    def tipo_dati(self):
        #Verifico il tipo di dati
        print(self.df.dtypes)

    def verifica_valori_nulli(self):
        print("Totale valori nulli per colonna:")
        print(self.df.isnull().sum())
#correlazione

    def correlazione(self):
            # Calcola la matrice di correlazione
            corr_matrix = self.df.corr()
            print(corr_matrix)
            plt.figure()
            sns.heatmap(corr_matrix, cmap='coolwarm')
            plt.title('Heatmap correlazione')
            plt.show()


oggetto = Housing("Lezione 23 luglio/housing.csv")
oggetto.scrivi_csv()
oggetto.mostra_df()
#oggetto.mostra_info()
#oggetto.tipo_dati()
oggetto.verifica_valori_nulli()
oggetto.correlazione()