import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

df = pd.read_csv("Pokemon.csv", ",", index_col=0)
df_resumen = df.describe().transpose()

print("Valores analizados de los pokemon del archivo .csv")
print (df_resumen)

# Vista general de los datos
plt.figure(figsize=(12,8))
plt.title("Atributos")
sns.boxplot(data=df)
plt.show()

# Tabla de Ataque 
plt.figure(figsize=(12,10))
sns.displot(x = "Attack", data = df, kde = True)
plt.suptitle("Ataque")
plt.show()

# Tabla de Defensa 
plt.figure(figsize=(12,10))
sns.displot(x = "Defense", data = df, kde = True)
plt.suptitle("Defensa")
plt.show()

# Tabla de HP 
plt.figure(figsize=(12,10))
sns.displot(x = "HP", data = df, kde = True)
plt.suptitle("HP")
plt.show()

df2=df.copy()
df2 = df2.drop(['Generation', 'Legendary','Total'],1)
df2 = pd.melt(df2, id_vars=["Name", "Type 1", "Type 2"], var_name="Stat")

# Estudia en rendimiento general de cada pokemon
plt.figure(figsize=(20,10))
plt.title("Rendimiento")
plt.xlabel("Value of Feature")
sns.histplot(data=df2)
plt.show()
