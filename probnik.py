import numpy as np
import pandas as pd


data = np.array(list(range(9)))
mask = data%2==0
print(data[mask])

go = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(go)

po = pd.DataFrame(data)
print(po)
