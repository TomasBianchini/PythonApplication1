from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection  import train_test_split
import pandas as pd
import mysql.connector



# Configura la información de la base de datos
db_config = {
    "host": "localhost",
    "user": "usu_semillas",
    "password": "usu_semillas",
    "database": "tpinvestigacion"
}

# Conecta a la base de datos
conn = mysql.connector.connect(**db_config)

# Crea un cursor para ejecutar consultas
cursor = conn.cursor()

# Ejemplo: Ejecuta una consulta SELECT
query = "SELECT * FROM semilla"
cursor.execute(query)

# Obtiene los resultados de la consulta
results = cursor.fetchall()

# Imprime los resultados
for row in results:
    print(row)

# Cierra el cursor y la conexión
cursor.close()
conn.close()




datos1=[25,60,1,'Maíz']
datos2=[30,60,2,'Sorgo']
datos3=[15,70,3,'Lechuga']
datos4=[25,80,4,'Arroz']
datos5=[22.5,60,5,'Tomate']
datos6=[25,60,6,'Frijoles']
# Etc.
data = [datos1, datos2, datos3, datos4, datos5, datos6]  


# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data, columns=['temperatura', 'humedad', 'zona_cultivo', 'semilla_optima'])


# Definir las características (X) y las etiquetas (y)
X = df[['temperatura', 'humedad', 'zona_cultivo']]
y = df['semilla_optima']


# Creamos el modelo de árbol de decisión multietiqueta
model = DecisionTreeClassifier()
model_sem = model.fit(X, y)

#Entrenamiento del modelo 

X_train, X_test, y_tain, y_test = train_test_split(X, y, test_size =0.8)

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


