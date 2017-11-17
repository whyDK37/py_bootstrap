#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Required Packages
# http://blog.csdn.net/lulei1217/article/details/49385531
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model


# Function to get data
def get_data(file_name):
    # 将.csv数据读入 Pandas 数据帧
    data = pd.read_csv(file_name)  # here ,use pandas to read cvs file.
    X_parameter = []
    Y_parameter = []
    # 把Pandas数据帧转换为X_parameter和Y_parameter数据，并返回他们。所以，让我们把X_parameter和Y_parameter打印出来：
    for single_square_feet, single_price_value in zip(data['square_feet'], data['price']):  # 遍历数据，
        X_parameter.append([float(single_square_feet)])  # 存储在相应的list列表中
        Y_parameter.append(float(single_price_value))
    return X_parameter, Y_parameter


# Function for Fitting our data to Linear model
def linear_model_main(X_parameters, Y_parameters, predict_value):
    # Create linear regression object
    # 首先，创建一个线性模型，用我们的X_parameters和Y_parameter训练它。
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)  # train model
    predict_outcome = regr.predict(predict_value)
    # 我们创建一个名称为predictions的字典，存着a、b和预测值，并返回predictions字典为输出。
    # 所以让我们调用一下我们的函数，要预测的平方英尺值为700。
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


# Function to show the resutls of linear fit model
def show_linear_line(X_parameters, Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters, Y_parameters, color='blue')
    plt.plot(X_parameters, regr.predict(X_parameters), color='red', linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()


X, Y = get_data('input_data.csv')
# 预测值
predictvalue = 700
result = linear_model_main(X, Y, predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
print("Predicted value: ", result['predicted_value'])
predictvalue = 800
result = linear_model_main(X, Y, predictvalue)
print("Intercept value ", result['intercept'])
print("coefficient", result['coefficient'])
print("Predicted value: ", result['predicted_value'])
show_linear_line(X, Y)

