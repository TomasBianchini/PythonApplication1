from sklearn.tree import DecisionTreeClassifier 
import pandas as pd

datos1=[25,70,1,'Maíz']
datos2=[30,80,2,'Trigo']
datos3=[35,75,3,'Arroz']
datos4=[25,70,1,'Trigo']
datos5=[30,80,2,'Arroz']
datos6=[35,75,3,'Soja']
# Etc.
data = [datos1, datos2, datos3, datos4, datos5, datos6]  # Añadir más combinaciones si es necesario

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data, columns=['temperatura', 'humedad', 'zona_cultivo', 'semilla_optima'])

# Definir las características (X) y las etiquetas (y)
X = df[['temperatura', 'humedad', 'zona_cultivo']]
y = df['semilla_optima']

# Creamos el modelo de árbol de decisión multietiqueta
model = DecisionTreeClassifier()
model_sem = model.fit(X, y)

temperatura_actual = float(input("Ingrese la temperatura actual: "))
humedad_actual = float(input("Ingrese la humedad actual: "))
zona_cultivo_actual = int(input("Ingrese la zona de cultivo actual (Norte(1)/Sur(2)/Este(3)): "))

# Especifica los nombres de columna para las características en el DataFrame de predicciones
X_pred = pd.DataFrame([[temperatura_actual, humedad_actual, zona_cultivo_actual]], columns=['temperatura', 'humedad', 'zona_cultivo'])

# Hacer una predicción basada en los valores proporcionados por el usuario
semilla_optima = model.predict(X_pred)

# Imprimir la recomendación de semillas óptimas
print("Las semillas óptimas para plantar en función del clima y la ubicación son:")
print(semilla_optima)



