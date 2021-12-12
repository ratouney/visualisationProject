"""
3d scatter plot
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

plt.style.use('seaborn')

parser = argparse.ArgumentParser(description='Generate visualization from dataset.')
parser.add_argument('-s', metavar='range_start', type=int, help='start of the selected range of points')
parser.add_argument('-e', metavar='range_end', type=int, help='end of the selected range of points')
parser.add_argument('-f', type=str, help='path to the data file.', default='./data.csv')

args = parser.parse_args()
print(args)

DATA_PATH = args.f

df = pd.read_csv(DATA_PATH)

range_start = args.s if args.s else 0
range_end = args.e if args.e else 600

if args.s and args.e and args.s >= args.e:
    print('Error: range start must be smaller than range end.')
    exit(1)

print(df.shape)

df = df.iloc[range(range_start, range_end)]
<<<<<<< Updated upstream
df = df.dropna()
df = df[cols]

if args.m == True:
    pd.plotting.scatter_matrix(df, alpha=1)
    plt.title("ScatterMatrix of the columns")
else:
    selectedDf = df[[args.x, args.y]]
    kmeans = KMeans(args.k)
    kmeans.fit(selectedDf)
    identified_clusters = kmeans.fit_predict(selectedDf)
    print(identified_clusters)
    data_with_clusters = selectedDf.copy()
    data_with_clusters['Clusters'] = identified_clusters
    title = f'KMeans[{args.k}] Clustering of {args.x}/{args.y}'
    plt.title(title)
    #plt.scatter(data_with_clusters['avg_glucose_level'],data_with_clusters['bmi'],c=data_with_clusters['Clusters'],cmap='rainbow')
    sns.scatterplot(data_with_clusters[args.x],data_with_clusters[args.y],c=data_with_clusters['Clusters'],cmap='rainbow', marker="o")
    plt.xlabel(args.x)
    plt.ylabel(args.y)

plt.show()
plt.savefig("figures/visualization_1.pdf")
=======

fig = plt.figure(figsize=(15, 8))

# plot stroke patients
ax = fig.add_subplot(111, projection='3d')
df_stroke = df[df['stroke'] == 0]
x_values = df_stroke['age']
y_values = df_stroke['avg_glucose_level']
z_values = df_stroke['bmi']
ax.scatter(x_values, y_values, z_values, s=50, alpha=0.6, edgecolors='w', label='No stroke')

#plot no-stroke patients
df_no_stroke = df[df['stroke'] == 1]
x_values = df_no_stroke['age']
y_values = df_no_stroke['avg_glucose_level']
z_values = df_no_stroke['bmi']
ax.scatter(x_values, y_values, z_values, c='red', s=50, alpha=0.6, edgecolors='w', label='Stroke')
ax.set_xlabel('Age (in years)')

ax.set_ylabel('Average glucose level (in g/cL)')
ax.set_zlabel('BMI')

# add legend
plt.legend()

plt.title('BMI as a function of age and glycaemia')

plt.savefig("figures/visualization_2.pdf")
>>>>>>> Stashed changes
plt.close()
