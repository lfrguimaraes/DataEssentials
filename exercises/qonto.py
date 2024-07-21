import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import ztest

df = pd.read_csv("../files/qonto_loans.csv")
data = df.iloc[:,1:2]


mean = data.mean().values[0]
std = data.std().values[0]
size = len(data)

Zscore = (mean-0.085)/(std/np.sqrt(size))
Pvalue = ztest(x1=data,value=mean)

print(Zscore)
print(Pvalue)
