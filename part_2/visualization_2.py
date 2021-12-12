"""
2d scatter plot
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

plt.style.use('seaborn')

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description='Generate visualization from dataset.')
parser.add_argument('-s', metavar='range_start', type=int, help='start of the selected range of points')
parser.add_argument('-e', metavar='range_end', type=int, help='end of the selected range of points')
parser.add_argument('-f', type=str, help='path to the data file.', default='./data.csv')
parser.add_argument('-m', type=str2bool, nargs="?", help='generate scatter matrix', const=True, default=False)
parser.add_argument('-x', type=str, help="column to use for axis X", default="avg_glucose_level")
parser.add_argument('-y', type=str, help="column to use for axis Y", default="bmi")
parser.add_argument('-k', type=int, help="KMeans cluster count",  default=5)
parser.add_argument('-c', type=str, nargs="+", action="append", help="Columns to use in ScatterMatrix")

args = parser.parse_args()
print(args)

DATA_PATH = args.f

df = pd.read_csv(DATA_PATH)

range_start = args.s if args.s else 0
range_end = args.e if args.e else 600

if args.s and args.e and args.s >= args.e:
    print('Error: range start must be smaller than range end.')
    exit(1)

print(df.columns)

cols = [col for col in df.columns if col not in ['id']]

df = df.iloc[range(range_start, range_end)]
df = df.dropna()
df = df[cols]

if args.m == True:
    pd.plotting.scatter_matrix(df, alpha=1)
else:
    selectedDf = df[[args.x, args.y]]
    kmeans = KMeans(args.k)
    kmeans.fit(selectedDf)
    identified_clusters = kmeans.fit_predict(selectedDf)
    print(identified_clusters)
    data_with_clusters = selectedDf.copy()
    data_with_clusters['Clusters'] = identified_clusters 
    #plt.scatter(data_with_clusters['avg_glucose_level'],data_with_clusters['bmi'],c=data_with_clusters['Clusters'],cmap='rainbow')
    sns.scatterplot(data_with_clusters[args.x],data_with_clusters[args.y],c=data_with_clusters['Clusters'],cmap='rainbow', marker="o")
    plt.xlabel(args.x)
    plt.ylabel(args.y)

plt.show()
plt.savefig("figures/visualization_1.pdf")
plt.close()
