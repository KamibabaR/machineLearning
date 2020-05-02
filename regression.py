#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

#pythonは整数通しの演算は小数点切り捨てがデフォルトなので、小数型で宣言
input_data = np.array([[20,30],
                       [23,32],
                       [28,40],
                       [30,44]],dtype='float')

before_normalize = np.copy(input_data)#pythonは浅いコピーされて参照渡しになるので、copy関数で実態コピーさせる

data_number = input_data.shape[0]


min_xyArray = np.min(input_data,axis=0,keepdims=True)
input_data = input_data - min_xyArray#numpyはベクトルの計算が可能


max_xyArray = np.max(input_data,axis=0,keepdims=True)

input_data = input_data / max_xyArray

        

epochs = 1000
alpha = 0.05

w0 = 0.1
w1 = 0.1

for t in range(epochs):
    dw0 = 0
    dw1 = 0
    for i in range(data_number):
        #誤差関数を偏微分したもの（傾き）
        dw0 = dw0 + 2*w0 + 2*w1*input_data[i,0] -2*input_data[i,1]
        dw1 = dw1 + input_data[i,0]*(2*w1*input_data[i,0] + 2*w0 -2*input_data[i,1])
    #傾きにalphaをかけた分だけ、動かす    
    w0 = w0 -alpha*(dw0)
    w1 = w1 -alpha*(dw1)
    
    #最急降下法は誤差関数の傾きを最小（0）に近づけるので、傾きを確認する
    #print(dw0)
    


    
ori_data_min_xyArray = np.min(before_normalize,axis=0,keepdims=True)
ori_data_max_xyArray = np.max(before_normalize,axis=0,keepdims=True)

x =np.linspace(0,ori_data_max_xyArray[0][0]-ori_data_min_xyArray[0][0],100)
y = w0 + w1*x


#正規化を元に戻す
#x方向の変形。x方向に圧縮された分、伸ばすので傾きが圧縮された分だけ緩くなる
y = w0 + w1*(x/max_xyArray[0][0])


y = y*max_xyArray[0][1]


#最小値分の平行移動をする
x = x + min_xyArray[0][0]
y = y + min_xyArray[0][1]

plt.plot(x,y)

for u in range(data_number):
    plt.scatter(before_normalize[u,0], before_normalize[u,1])


