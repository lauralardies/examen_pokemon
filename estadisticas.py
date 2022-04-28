import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')

df = pd.read_csv("Pokemon.csv", ",")
df_resumen = df.describe().transpose()

print (df_resumen)