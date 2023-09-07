from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection  import train_test_split
import pandas as pd
import mysql.connector
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

semillas_optimas = []

def intercambiar_columnas(matriz, col1, col2):
    for fila in matriz:
        aux = fila[col1]
        fila[col1] = fila[col2]
        fila[col2] = aux


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
data = cursor.fetchall()

# Cierra el cursor y la conexión
cursor.close()
conn.close()


#Pasamos los datos de tuplas a lista de listas para poder utilizar la libreria sklearn 
datos = [list(tupla) for tupla in data]
intercambiar_columnas(datos, 0 , 3)

#tipo_suelo_actual = int(input("Ingrese el tipo de suelo del cultivo:\n1-Alfidoles\n2-Aridisoles\n3-Entisoles\n4-Histosoles\n5-Molisoles\n6-Vertisoles\n7-Ultisoles\n8-Inceptisoles\n "))
#while(tipo_suelo_actual < 1 or tipo_suelo_actual > 8): 
#     print("Debe ingresar un numero entre 1 y 8")
#     tipo_suelo_actual = int(input("Ingrese el tipo de suelo del cultivo:\n1-Alfidoles\n2-Aridisoles\n3-Entisoles\n4-Histosoles\n5-Molisoles\n6-Vertisoles\n7-Ultisoles\n8-Inceptisoles\n "))

#temperatura_actual = float(input("Ingrese la temperatura promedio: "))
#humedad_actual = float(input("Ingrese la humedad promedio: "))
tipo_suelo_actual = 1
temperatura_actual = 25
humedad_actual = 80



datos = datos[-5:]

# Convertir los datos a un DataFrame de pandas

df = pd.DataFrame(datos, columns=['tipo_suelo', 'temperatura', 'humedad', 'semilla_optima'])

    # Definir las características (X) y las etiquetas (y)
X = df[['tipo_suelo', 'temperatura', 'humedad']]
y = df['semilla_optima']

    # Creamos el modelo de árbol de decisión multietiqueta
model = DecisionTreeClassifier()
model_sem = model.fit(X, y)

    #Entrenamiento del modelo 

X_train, X_test, y_tain, y_test = train_test_split(X, y, test_size =0.8)

# Especifica los nombres de columna para las características en el DataFrame de predicciones
X_pred = pd.DataFrame([[tipo_suelo_actual, temperatura_actual, humedad_actual]], columns=['tipo_suelo', 'temperatura', 'humedad'])

# Hacer una predicción basada en los valores proporcionados por el usuario
semilla_optima = model.predict(X_pred)



# Visualizar el árbol de decisión
plt.figure(figsize=(10, 10))  # Tamaño de la figura
plot_tree(model_sem, feature_names=['tipo_suelo', 'temperatura', 'humedad'], class_names=df['semilla_optima'].unique().tolist(), filled=True, rounded=True)
plt.show()


# Imprimir la recomendación de la semilla óptima
print("Las semillas recomendadas para plantar \nen función del clima y el tipo de suelo son:")
print(semilla_optima) 
   

