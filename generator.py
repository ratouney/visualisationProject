import numpy as np

lines = 20
cols = 6

# Generate random means and standart deviations for the columns
means = np.random.normal(5, 1.5, (cols))
devs = np.random.normal(1, 0.5, (cols))

# A simple float column
col0 = np.random.normal(means[0], devs[0], (lines))
# Same base, but building an INT column
col1 = np.random.normal(means[1], devs[1], (lines)) * 100
rt = np.around(col1, 0)
rt = rt.astype(int)

# Merging them together
full = np.column_stack((col0, col1))
print(full)

np.save("dataset", full)
np.save("")