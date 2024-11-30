import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

data = r"C:\Users\admin\Downloads\wine\Iris.csv"
df = pd.read_csv(data)


df = df.dropna()
if 'Id' in df.columns:
    df = df.drop(columns=['Id'])


species = df.columns[-1]

plt.figure(figsize=(10, 6))  
parallel_coordinates(df, class_column=species, colormap=plt.get_cmap("Set2"))
plt.title("Parallel Coordinates Plot for Iris Dataset")
plt.xlabel("Features")
plt.ylabel("Values")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
