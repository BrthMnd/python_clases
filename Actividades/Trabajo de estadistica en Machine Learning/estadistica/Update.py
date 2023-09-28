
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statistics as st

datasetCD = pd.read_excel('Datosnunidos___8264f0e04f9ef01___.xlsx', sheet_name='Sheet1')

modificacion = datasetCD
modificacion['Nombre'] = modificacion['Nombre'] + ' ' + modificacion['Apellidos']
modificacion = modificacion.drop(['Apellidos'], axis=1)

modificacion = modificacion.dropna()
modificacion = modificacion.drop_duplicates()

edad = modificacion['Edad']
edad = modificacion['Edad'].value_counts().reset_index() 
edad.columns = ['Edad', 'Frecuencia_Absoluta']
suma_absoluta = edad['Frecuencia_Absoluta'].sum()
edad['Frecuencia_Acumulada_Absoluta'] = edad['Frecuencia_Absoluta'].cumsum()
edad['Frecuencia_Relativa'] = edad['Frecuencia_Absoluta'] / suma_absoluta
edad['Frecuencia_Acumulada_Relativa'] = edad['Frecuencia_Relativa'].cumsum()


Estatura = modificacion['Estatura']
Estatura = modificacion['Estatura'].value_counts().reset_index() 
Estatura.columns = ['Estatura', 'Frecuencia_Absoluta']
suma_absoluta = Estatura['Frecuencia_Absoluta'].sum()
Estatura['Frecuencia_Acumulada_Absoluta'] = Estatura['Frecuencia_Absoluta'].cumsum()
Estatura['Frecuencia_Relativa'] = Estatura['Frecuencia_Absoluta'] / suma_absoluta
Estatura['Frecuencia_Acumulada_Relativa'] = Estatura['Frecuencia_Relativa'].cumsum()

Estratos = modificacion['Estrato'].value_counts().reset_index()
Estratos.columns = ['Estrato', 'Frecuencia_Absoluta']
Estratos['Frecuencia_Acumulada_Absoluta'] = Estratos['Frecuencia_Absoluta'].cumsum()
suma_absoluta = Estratos["Frecuencia_Absoluta"].sum()
Estratos["Frecuencia_Relativa"] = Estratos["Frecuencia_Absoluta"] / suma_absoluta
Estratos['Frecuencia_Acumulada_Relativa'] = Estratos['Frecuencia_Relativa'].cumsum()

varianza_edad = modificacion['Edad'].var()
print("Varianza edad: ", varianza_edad, "\n")

desviacion_estandar_ed = modificacion['Edad'].std()
print("Desviacion Estandar Edad: ", desviacion_estandar_ed, "\n")

mediana_edad = modificacion['Edad'].median()
print("Mediana Edad: ", mediana_edad, "\n")

moda_edad = st.mode(modificacion['Edad'])
print("Moda edad:", moda_edad, "\n")

promedio_edad = modificacion['Edad'].mean()
print("promedio edad: ", promedio_edad, '\n')

varianza_estatura = modificacion['Estatura'].var()
print("Varianza Estatura: ", varianza_estatura, "\n")

desviacion_estandar_es = modificacion['Estatura'].std()
print("Desviacion Estandar Estatura: ", desviacion_estandar_es, "\n")

mediana_estatura = modificacion['Estatura'].median()
print("Mediana Estatura: ", mediana_estatura, "\n")

moda_estatura = st.mode(modificacion['Estatura'])
print("Moda estatura:", moda_estatura, "\n")

promedio_estatura = modificacion['Estatura'].mean()
print("promedio estatura: ", promedio_estatura, '\n')

qCD1 = np.quantile(modificacion['Edad'], q=0.25)
qCD2 = np.quantile(modificacion['Edad'], q=0.50)
qCD3 = np.quantile(modificacion['Edad'], q=0.75)
qCD4 = np.quantile(modificacion['Edad'], q=1)
print(f"Cuartiles Edad \n Q1={qCD1}, Q2={qCD2}, Q3={qCD3}, Q4={qCD4}")

IQR1 = qCD3 - qCD1
print(f"Intercuartiles Edad \n Q1={qCD1}, Q3={qCD3} y IQR={IQR1}")

qCC1 = np.quantile(modificacion['Estatura'], q=0.25)
qCC3 = np.quantile(modificacion['Estatura'], q=0.75)
print(f"Cuartiles Estatura \n Q1={qCC1}, Q2={qCC3}")

IQR2 = qCC3 - qCC1
print(f"Intercuartiles Estatura \n Q1={qCC1}, Q3={qCC3}, IQR={IQR2}")

plt.figure(figsize=(8, 6))
plt.boxplot(modificacion['Edad'], vert=False)
plt.title('Gráfico de Caja - Edad')
plt.xlabel('Edad')
plt.show()

plt.figure(figsize=(8, 6))
plt.boxplot(modificacion['Estatura'], vert=False)
plt.title('Gráfico de Caja - Estatura')
plt.xlabel('Estatura')
plt.show()

x = edad['Edad']
y = edad['Frecuencia_Absoluta']

plt.scatter(x, y, color='blue', label='edad')
plt.title('Gráfico de dispersión Frecuencia Abs edad')
plt.xlabel('edad')
plt.ylabel('Frecuencia_Acumulada')
plt.legend()
plt.show()

x = edad['Edad']
y = edad['Frecuencia_Acumulada_Absoluta']

sns.set(style='whitegrid')  
sns.scatterplot(x=x, y=y, color='blue', label='datos')
plt.title('Gráfico Frecuencia Acumulada Absoluta')
plt.xlabel('Edad')
plt.ylabel('Frecuencia Acumulada Absoluta')
plt.legend()
plt.show()

intervalos = Estatura['Estatura'].astype(str)
x = intervalos

y = Estatura['Frecuencia_Absoluta']

plt.bar(x, y, color='orange')
plt.title('Frecuencia Absoluta Estatura')
plt.xlabel('Estatura')
plt.ylabel('Frecuencia Absoluta')
plt.xticks(rotation=90)  
plt.show()

sns.set(style='whitegrid')

intervalos = Estatura['Estatura'].astype(str)
frecuencia_acumulada_absoluta = Estatura['Frecuencia_Acumulada_Absoluta']

plt.plot(intervalos, frecuencia_acumulada_absoluta, marker='o', color='orange', linestyle='-')
plt.title('Gráfico de densidad de Frecuencia Acumulada Absoluta')
plt.xlabel('Estatura')
plt.ylabel('Frecuencia Acumulada Absoluta')
plt.xticks(rotation=90)  
plt.show()

x = Estratos['Estrato']
y = Estratos['Frecuencia_Absoluta']

plt.pie(y, labels=x, autopct='%1.1f%%')
plt.title('Gráfico Frecuencia Absoluta Estrato')
plt.show()

ax = sns.lineplot(x='Estrato', y='Frecuencia_Acumulada_Absoluta', data=Estratos, marker='o', color='blue')
ax.set_xlabel('Estrato')
ax.set_ylabel('Frecuencia Acumulada Absoluta')
plt.xticks(rotation=45) 
plt.show()
