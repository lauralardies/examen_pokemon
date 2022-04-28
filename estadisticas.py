import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

df = pd.read_csv("Pokemon.csv", ",", index_col=0)
df_resumen = df.describe().transpose()

print (df_resumen)

plt.figure(figsize=(12,8))
plt.title("How are the Attributes distributed?")
sns.boxplot(data=df)
plt.show()

df2=df.copy()
df2 = df2.drop(['Generation', 'Legendary','Total'],1)
df2 = pd.melt(df2, id_vars=["Name", "Type 1", "Type 2"], var_name="Stat")

plt.figure(figsize=(20,10))
plt.title("How are the Performance Attributes distributed?")
plt.xlabel("Value of Feature")
sns.histplot(data=df2)
plt.show()

sns.catplot(x='Legendary',kind='count',data=df,height=6,aspect=1)
plt.title("Legendary Pokemons are less than 12% of all Pokemons")
plt.show()