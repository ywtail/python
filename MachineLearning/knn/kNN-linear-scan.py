# coding:utf-8
from __future__ import division
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def knnClassify(newinput, datas, labels, k, p):
    # 计算距离
    diff = abs(np.tile(newinput, (len(datas), 1)) - datas)
    distances = (np.sum(diff ** p, axis=1)) ** (1 / p)
    sort_distances = np.argsort(distances)
    #print distances
    # print sort_distances

    # 投票法决定分类
    classCount = {}
    for i in range(k):
        label = labels[sort_distances[i]]
        classCount[label] = classCount.get(label, 0) + 1

    maxCount = 0
    maxIndex = -1
    for key, value in classCount.items():
        if value > maxCount:
            maxCount = value
            maxIndex = key
    return maxIndex


if __name__ == '__main__':
    '''
    # example in book
    group = [[5, 1], [4, 4]]
    lables = ['a', 'b']
    print knnClassify([1, 1], group, lables, 1, 1)
    print knnClassify([1, 1], group, lables, 1, 2)
    print knnClassify([1, 1], group, lables, 1, 3)
    print knnClassify([1, 1], group, lables, 1, 4)
    '''

    # example for digit recognizer
    all_data = pd.read_csv('data/digit_datas.csv')
    y = all_data['label'].values
    x = all_data.drop(['label'], axis=1).values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    print 'Data Infomation:'
    print 'Train Data Information: ',x_train.shape, len(y_train)
    print 'Test Data Information: ',x_test.shape, len(y_test)

    matchCount = 0
    accuracy = 0
    print '识别错误的数如下：'
    for i in range(len(x_test)):
        predict = knnClassify(x_test[i], x_train, y_train, 3, 2)
        # print predict,y_test[i]
        if predict == y_test[i]:
            matchCount += 1
        else: # 打印识别错误的数
            print predict, y_test[i]
        accuracy = float(matchCount) / len(x_test)
    print 'accuracy:',accuracy