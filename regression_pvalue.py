import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

np.random.seed(0) 
n = 50  
tamaño = np.random.normal(1500, 250, n)  
precio = 30000 + tamaño * 50 + np.random.normal(0, 10000, n)  

data = pd.DataFrame({'Tamaño': tamaño, 'Precio': precio})

X = data['Tamaño']  
y = data['Precio']  

X = sm.add_constant(X) 

modelo = sm.OLS(y, X).fit()  

print(modelo.summary())

plt.scatter(data['Tamaño'], data['Precio'], color='blue', label='Datos observados')

plt.plot(data['Tamaño'], modelo.predict(X), color='red', label='Línea de regresión')

plt.xlabel('Tamaño (pies cuadrados)')
plt.ylabel('Precio (USD)')
plt.title('Relación entre Tamaño y Precio de Casas')
plt.legend()
plt.show()