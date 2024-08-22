from kivy.uix.gridlayout import product
#місце для твого коду
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("IMDB-Movie-Data.csv")

df.info()

df['Rating'].plot(kind= 'hist', bins=5)
plt.show()

