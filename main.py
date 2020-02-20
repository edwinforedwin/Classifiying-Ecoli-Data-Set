import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_file = pd.read_csv('/home/root-user/Documents/ecoli.csv')  #Loading Data

df1 = pd.DataFrame(data_file)                    #Data frame created and cleaned
df1_cleaned = df1.drop('SEQUENCE_NAME',axis=1)

df1_cleaned.SITE.replace(('cp','im','imS','imL','imU','om','omL','pp'),(1,2,3,4,5,6,7,8),inplace=True) #Data encoding
print("Correlation",df1_cleaned.corr(method='pearson'))  #Correlation between each measures
