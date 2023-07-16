from array import array
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import matplotlib.pyplot as plt


df=pd.read_csv("C:\\Users\\naman\\Desktop\\Regression Anlysis\\code\\final_project\\final.csv" )

print(df)

x = df[['c', 's']]
x1 = df[['c']]
y = df['p']

regr = linear_model.LinearRegression()
regr1= linear_model.LinearRegression()

regr.fit(x, y)
regr1.fit(x1,y)

print(regr.coef_) # coco +spy
print(regr1.coef_) ## only coco
print(regr.score(x, y))
print(regr1.score(x1, y))

y_pred = regr.predict(x)

plt.scatter(x1,y,color="b",marker="o",s=10)
coef=regr1.coef_
intc=regr1.intercept_
line=intc + coef*x1
plt.plot(x1,line,color="y")
plt.xlabel('Coca-cola price')
plt.ylabel('Pepsi price')
plt.title('Pepsi price predicted just by coca-cola')



plt.show()



