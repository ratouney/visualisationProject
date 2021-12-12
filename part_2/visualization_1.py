"""
2d scatter plot
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

print(df.columns)

cols = [col for col in df.columns if col not in ['id']]

df = df.iloc[range(range_start, range_end)]
df = df[cols]

f, axs = plt.subplots(len(df.columns), len(df.columns), figsize=(10, 10))

i = 0
for x in df.columns:
    for y in df.columns:
        sns.stripplot(data=df, x=x, y=y, ax=axs[i])
        i += 1
f.tight_layout()

plt.savefig("figures/visualization_1.pdf")
plt.close()
