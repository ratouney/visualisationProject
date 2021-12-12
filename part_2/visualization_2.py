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
range_end = args.e if args.e else df.shape[0]

if args.s and args.e and args.s >= args.e:
    print('Error: range start must be smaller than range end.')
    exit(1)

print(df.shape)

df = df.iloc[range(range_start, range_end)]

fig = plt.figure(figsize=(15, 8))

# plot stroke patients
ax = fig.add_subplot(111, projection='3d')
df_stroke = df[df['stroke'] == 1]
x_values = df_stroke['age']
y_values = df_stroke['avg_glucose_level']
z_values = df_stroke['bmi']

#plot no-stroke patients
ax.scatter(x_values, y_values, z_values, s=50, alpha=0.6, edgecolors='w')
df_no_stroke = df[df['stroke'] == 0]
x_values = df_no_stroke['age']
y_values = df_no_stroke['avg_glucose_level']
z_values = df_no_stroke['bmi']

ax.scatter(x_values, y_values, z_values, c='red', s=50, alpha=0.6, edgecolors='w')
ax.set_xlabel('Age (in years)')
ax.set_ylabel('Average glucose level (in g/cL)')
ax.set_zlabel('BMI')

plt.savefig("visualization_2.pdf")
plt.close()
