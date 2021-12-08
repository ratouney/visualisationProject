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
range_end = args.e if args.e else df.shape[0]

if args.s and args.e and args.s >= args.e:
    print('Error: range start must be smaller than range end.')
    exit(1)

print(df.shape)

df = df.iloc[range(range_start, range_end)]

sn.scatterplot(data=df, x='age', y='avg_glucose_level')

plt.show()
