import pandas as pd

df = pd.read_csv("Pokemon.csv", ",")
n = len(df) # El número de Pokemon que hay en nuestro dataset

print("Tenemos " + str(n) + " Pokemons distintos en nuestro dataset. Vamos a seleccionar 400 para cada entrenador de manera equilibrada.")

