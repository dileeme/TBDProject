import pandas as pd
import numpy as np

df = pd.read_csv("counts.csv", index_col=0)

# log normalization
df_log = np.log1p(df)
