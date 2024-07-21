import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#df = pd.read_csv("../files/km_traveled_all_transportations.csv")
#df = df.iloc[:,1:]
#df = df.groupby("type_of_transport").mean()

#sns.catplot(x="type_of_transport", y="Km_traveled", data = df, kind="bar")
#plt.show()

df = pd.read_csv("../files/km_traveled_per_transport.csv")
df = df.iloc[:,1:]
#df = df.mean()
#print(df)

#sns.catplot(x="type_of_transport", y="Km_traveled", data = df, kind="bar")
#plt.show()
z_value = 1.96
sigma = df.std()
n = len(df)
E = z_value*sigma/np.sqrt(n)
print(E)

df.mean().plot(kind="bar", yerr=E)
plt.show()






