
from statistics import linear_regression
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.regression.rolling import RollingOLS
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.regression.rolling import RollingOLS

data=pd.read_csv("C:\\Users\\naman\\Desktop\\Regression Anlysis\\code\\final_project_2\\f.csv")

print(data)

x = np.array(data['c_n']).reshape(-1,1)
y = data['c_bn']
t = data['days']


sum = 0 
i = 1

while i<=2439 :
    model = LinearRegression().fit(x[i:i+30], y[i:i+30])
    r_sq = model.score(x[i:i+30], y[i:i+30])
    sum = sum +r_sq 
    print(f"coefficient of determination: {r_sq}")
    i=i+1 


print(sum/i) 

plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Rolling Regression')






