import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
pd.plotting.scatter_matrix(df, alpha=0.2)

plt.show()