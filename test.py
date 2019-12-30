import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()



df = pd.DataFrame(np.random.randn(1000, 4),index=ts.index, columns=list('ABCD'))

df = df.cumsum()

print(np.random.randn(1000, 4))
ts.plot()
df.plot()
plt.show()

