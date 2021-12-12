import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import keyboard
sns.set()
from sklearn.cluster import KMeans

df = pd.read_csv("data.csv")
print("Read entry count : ", df.shape[0])
print(df)

dff = df[['age', 'avg_glucose_level', 'bmi', 'stroke']]
dff = dff.dropna()

#dff = dff[dff['stroke'] == 1]

print("After removal of empty : ", dff.shape[0])
print(dff)


# Display a complete scatter matrix for all columns
pd.plotting.scatter_matrix(dff, alpha=0.2)
plt.show()

# Display a scatter plot with various Kmeans on specific columns
#selectedDf = dff[['avg_glucose_level', 'bmi']]
#k = 18
##for k in range(0, 19):
#kmeans = KMeans(20 - k)
#kmeans.fit(selectedDf)
#identified_clusters = kmeans.fit_predict(selectedDf)
#print(identified_clusters)
#data_with_clusters = selectedDf.copy()
#data_with_clusters['Clusters'] = identified_clusters 
##plt.scatter(data_with_clusters['avg_glucose_level'],data_with_clusters['bmi'],c=data_with_clusters['Clusters'],cmap='rainbow')
#sns.scatterplot(data_with_clusters['avg_glucose_level'],data_with_clusters['bmi'],c=data_with_clusters['Clusters'],cmap='rainbow', marker="+")
#plt.xlabel("Avg_glucose_level")
#plt.ylabel("BMI")
#plt.show()