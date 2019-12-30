import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_df = pd.read_excel('D:\Document\Work\CropAnalysis\sourcedata\summer_origin.xlsx', sheet_name= 0)
describe = data_df.describe()
x = data_df.columns[0:12]

print(x)
plot_Data = pd.DataFrame(data_df)
plt.plot(x, data_df[0,:])

ts = pd.Series(x, index=pd.date_range('1/1/2000', periods=1000))

ts = ts.cumsum()


plt.show()

#
# print(format(data_df))
# print(describe)




