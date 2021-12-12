
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

plt.style.use('seaborn')


"""
You are free to choose the dataset within the following constraints :
* utf-8 encoded in a `data.csv` file
* several hundreds of lines
* at least 6 attributes (columns), the first being a unique id, separated by commas
* you may use some categorical (non quantitative) features.
* some fields should be correlated

If necessary, you can tweak a dataset in order to artificially make it possible to
apply analysis ans visualization techniques.
"""


df = pd.read_csv("./data.csv")
df.head()


"""
The file analysis.py presents a quick analysis of the dataset. For instance :
* Histograms of quantitative variables with a comment on important statistical aspects, such as means , standard deviations , etc.
* A study of potential outliers
* Correlation matrices (maybe not for all variables)
* Any interesting analysis : if you have categorical data, with categories are represented most ? To what extent ?
"""


# normalize column names

df.columns = df.columns.str.lower()
df.head()

# drop lines with missing values
print(df.shape)
df = df.dropna()
print(df.shape)
df.head()


"""
## Plot distribution of each column

We use the raw dataset because it has better visibility for binary/categorical variables.
We don't plot the id as it doesn't make sense.
"""


import seaborn as sns

# plot distribution of each column

for col in df.columns[1:]:
    fig = sns.displot(df, x=col)
    fig.savefig(f'figures/histogram_{col}.pdf')


# compute mean & stddev for each column

numeric_cols = ['age', 'bmi', 'avg_glucose_level']

for col in numeric_cols:
    mean = df[col].mean()
    stdev = df[col].std()
    print(f'{col}\tmean: {mean:.2f}\tstdev: {stdev:.2f}')


corr_matrix = df[df.columns[1:]].corr()
hm = sns.heatmap(corr_matrix, annot=True)
hm.get_figure().savefig('figures/correlation_matrix.pdf')
