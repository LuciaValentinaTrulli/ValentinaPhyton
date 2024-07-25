""" Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction ,
utilizzate i dati sugli anni delle case e la distanza dalla stazione metro per prevedere quanto queste
caratteristiche influiscono sul costo delle case. """

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import PredictionErrorDisplay

# Caricare i dati dal file CSV
file_path = 'Lezione 25 luglio/Real estate.csv'
df = pd.read_csv(file_path)

#print(df.head())

X = df[['X2 house age', 'X3 distance to the nearest MRT station']]
y = df['Y house price of unit area']

#print(X.shape)
#print(y.shape)

# dividiamo i dati in train e test
X_train, X_test, y_train, y_test = train_test_split(
    X, y)

#alleno il modello
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)

#faccio previsione
y_pred = regr.predict(X_test)
print(y_pred)


r_sq = regr.score(X_test, y_test)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {regr.intercept_}")
print(f"coefficients: {regr.coef_}") 

#grafico errori
display = PredictionErrorDisplay(y_true=y_test, y_pred=y_pred)
display.plot()
plt.show()