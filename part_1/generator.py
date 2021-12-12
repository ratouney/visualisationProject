import numpy as np
import math
from numpy.lib.shape_base import column_stack
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

lines = 20
cols = 6

# Generate random means and standart deviations for the columns
# Setting the starting mean at 2.5 so at least one of them should be close enough
means = np.random.normal(2.5, 1.5, (cols))
devs = np.random.normal(1.5, 0.5, (cols))

# A simple float column
col0 = np.random.normal(means[0], devs[0], (lines))
# A positively correlated column
col1 = col0 * math.pi
# Same, but negative this time
col2 = col1 / -2.5

# Now re-build a colum with random values, should not correlate to col0
col3 = []
for i in range(0, lines):
    noise1 = np.random.randint(5) + 1
    noise2 = np.random.random(1) * 10 ** np.random.randint(2)
    val = noise1 * noise2
    #print(f'{noise1} * {noise2} = {val}')
    col3.append(val)

# Store the arbitrarily generated columns
currentColumns = [col0, col1, col2, col3]

randomsColsToAdd = cols - len(currentColumns)
# Add a couple of colmumns using the generated means/devs
for k in range(0, randomsColsToAdd):
    generatedColumn = np.random.normal(means[k], devs[k], (lines))
    currentColumns.append(generatedColumn)

# Merging them together into a dataframe
full = np.column_stack(currentColumns)
columnNames = ["Base", "Positive", "Negative", "Corr0"]
for k in range(0, randomsColsToAdd):
    columnNames.append("Random")
df = pd.DataFrame(full, columns=columnNames)

if lines <= 20:
    print(df)

# Save the generation parameters for back checking
usedParams = np.column_stack((means, devs))
np.save("dataset", full)
np.save("usedParams", usedParams)

# Display the correlation factors between the columns
cor_df = df.corr()
print("================ CORRELATIONS ================")
print(cor_df)


print("=================== MEANS ====================")
for k in range(0, cols):
    print(df.columns[k], ".mean : ", df.iloc[:, k].mean())

print("============ STANDART DEVIATIONS =============")
for k in range(0, cols):
    print(df.columns[k], ".std : ", df.iloc[:, k].std())