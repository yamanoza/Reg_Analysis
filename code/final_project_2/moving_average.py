import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


nif_1 = pd.read_csv("C:\\Users\\naman\\Desktop\\Regression Anlysis\\code\\final_project_2\\base_1.csv",parse_dates=True)

nif_1['SMA60'] = nif_1['c'].rolling(60).mean()
nif_1.dropna(inplace= True )


print(nif_1)

R_square = r2_score(nif_1['c'], nif_1['SMA60']) 
print('Coefficient of Determination', R_square)

plt.plot(nif_1["d"],nif_1['SMA60'],label = "Simple moving Average-60")
plt.plot(nif_1["d"],nif_1['c'],label = "Actual_Value")
plt.xlabel('Trading Days after the crash')
plt.ylabel('Closing Price')
plt.show()


