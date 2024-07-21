# Facebook would like to know the average time spent on their site.
# To do so, they launched a study on 100 people and asked them how much time they spend on Facebook per day:
# 1. Open the Hours spent on Facebook.xlsx file.
# 2. Calculate the mean and standard deviation of the corresponding column.
# 3. We would like to know the mean of the total population. Calculate the 95% confidence interval.


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st
import statsmodels.stats.api as sms
import scipy.stats

files = ("Hours spent on Facebook.xlsx", "Monthly spending on adwords.xlsx")

for file in files:

    df = pd.read_excel("../files/"+file)
    data = df.iloc[:,-1:]
    mean = data.mean().values[0]
    std = data.std().values[0]
    sem = data.sem().values[0]
    n = len(data)


    print("File: ", file)
    print("Mean: ", mean)
    print("Size: ", n)
    print("Standard Deviation: ", std)
    print("Standard Error: ", sem)

    E = 1.96*(std/np.sqrt(n))

    print("Confidence Interval (95%): ",mean-E," to ", mean+E)
    print(st.t.interval(confidence=0.95, df=n, loc=mean, scale=sem))
    print(sms.DescrStatsW(data).tconfint_mean(alpha=0.05))
    print("\n")








