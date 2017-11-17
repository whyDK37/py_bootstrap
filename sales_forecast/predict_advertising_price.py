#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Required Packages
# http://blog.csdn.net/lulei1217/article/details/49386295
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split  # 这里是引用了交叉验证
from sklearn.linear_model import LinearRegression

data = pd.read_csv('Advertising.csv')

# display the first 5 rows
data.head()
# display the last 5 rows
# data.tail()

# visualize the relationship between the features and the response using scatterplots
# sns.pairplot(data, x_vars=['TV','Radio','Newspaper'], y_vars='Sales', size=7, aspect=0.8)
sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')
plt.show()  # 注意必须加上这一句，否则无法显示。

# create a python list of feature names
print('create a python list of feature names')
# use the list to select a subset of the original DataFrame
# feature_cols = ['TV', 'Radio', 'Newspaper']
# X = data[feature_cols]
# equivalent command to do this in one line
X = data[['TV', 'Radio', 'Newspaper']]
# print the first 5 rows
print(X.head())
# check the type and shape of X
print(type(X))
print(X.shape)

# select a Series from the DataFrame
y = data['Sales']
# equivalent command that works if there are no spaces in the column name
# y = data.Sales
# print the first 5 values
print(y.head())

print('（2）、构建训练集与测试集')
##构造训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(y_train.shape)
print(X_test.shape)
print(y_test.shape)

print('（3）sklearn的线性回归')
linreg = LinearRegression()
model = linreg.fit(X_train, y_train)
print(model)
print(linreg.intercept_)
print(linreg.coef_)

# pair the feature names with the coefficients
zip(feature_cols, linreg.coef_)

print('（4）、预测')
y_pred = linreg.predict(X_test)
print(y_pred)
print(type(y_pred))

print('5、回归问题的评价测度')
print('计算Sales预测的RMSE')
print(type(y_pred), type(y_test))
print(len(y_pred), len(y_test))
print(y_pred.shape, y_test.shape)
from sklearn import metrics
import numpy as np

sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += (y_pred[i] - y_test.values[i]) ** 2
sum_erro = np.sqrt(sum_mean / 50)
# calculate RMSE by hand
print("RMSE by hand:", sum_erro)

print('（2）做ROC曲线')
plt.figure()
plt.plot(range(len(y_pred)),y_pred,'b',label="predict")
plt.plot(range(len(y_pred)),y_test,'r',label="test")
plt.legend(loc="upper right") #显示图中的标签
plt.xlabel("the number of sales")
plt.ylabel('value of sales')
plt.show()


print('6、改进特征的选择')
#create a python list of feature names
feature_cols = ['TV', 'Radio', 'Newspaper']
# use the list to select a subset of the original DataFrame
X = data[feature_cols]
# equivalent command to do this in one line
#X = data[['TV', 'Radio', 'Newspaper']]#只需修改这里即可<pre name="code" class="python" style="font-size: 15px; line-height: 35px;">X = data[['TV', 'Radio']]  #去掉newspaper其他的代码不变