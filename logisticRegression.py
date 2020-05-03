#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''
範囲1-10
[飲酒量、喫煙量、先活習慣病かどうか]
'''
 
input_data = np.array([[1,1,0],[1,4,0],[3,1,0],[4,5,1],[0,5,1]])
data_number = input_data.shape[0]

epochs = 10000
alpha = 0.2

b0 = 0.1
b1 = 0.1
b2 = 0.1


for t in range(epochs):
    #移動後に初期化
    db0 = 0
    db1 = 0
    db2 = 0
    Likelyhood = 1
    
    for i in range(data_number):
        Z = b0 + b1*input_data[i,0] +b2*input_data[i,1]
        Sigmoid = 1 / (1 + np.exp(-Z))#sigmoid
        
        if input_data[i,2]:
            db0 = db0 + (1-Sigmoid)
            db1 = db1 + (1-Sigmoid)*input_data[i,0]
            db2 = db2 + (1-Sigmoid)*input_data[i,1]
            
            #尤度関数
            Likelyhood = Likelyhood*(1 / (1 + np.exp(-Z)))
            
        else:
            db0 = db0 - Sigmoid
            db1 = db1 - Sigmoid*input_data[i,0]
            db2 = db2 - Sigmoid*input_data[i,1]
            
            #尤度関数
            Likelyhood = Likelyhood*(1 - 1 / (1 + np.exp(-Z)))

    b0 = b0 + alpha*db0
    b1 = b1 + alpha*db1
    b2 = b2 + alpha*db2
    
    '''
    plt.scatter(t, Likelyhood)
    print(db1)
    '''
    
'''
z = b0 + b1*X1 +b2*X2 > 0 なら生活習慣病
b0 + b1*X1 +b2*X2 = 0 グラフが　境目になる
x1 =x
x2 =y として

b2*y = -b0 -b1*x1
y = -b0/b2 -b1/b2*x

'''


x = np.linspace(0,7,100)
y = -b0/b2 - b1/b2*x

plt.plot(x,y)

for n in range(data_number):
    plt.scatter(input_data[n,0],input_data[n,1])
