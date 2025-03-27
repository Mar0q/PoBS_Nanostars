from DataSets import * # Get all data sets Extracted in DataSets file (SP=Simulation Parameters, Data=Data)
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress

print(Data_Set1_df.head(2))
sns.scatterplot(data=Data_Set1_df, x="NR_free", y="Coverage")
plt.xlabel("NR_free")
plt.ylabel("Coverage")
plt.title("Coverage vs NR_free")
plt.text(0.5, 0.5, (SP_Set1_df), fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
plt.show()

for i in range(len(SP_list)):

    sns.scatterplot(data=Data_list[i], x="NR_free", y="Coverage")   # Plot data
    plt.xlabel("NR_free")
    plt.ylabel("Coverage")
    slope, intercept, r_value, p_value, std_err = linregress(Data_list[i]["NR_free"], Data_list[i]["Coverage"])
    plt.title(f"Coverage vs NR\nk_Ratio"+str(SP_list[i]["k_ratio"][0])+f"\nSlope = {slope:.4f}")
    #plt.text(0.5, 0.5, (SP_Set1_df), fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)
    plt.show()