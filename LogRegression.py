import numpy as np
import csv
import sys
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

def sigmoid(X):
    return 1.0/(1 + exp(-X))

# train a logistic regression model using optimized algorithm
# input : train_x is a mat datatype, each row for one sample

def trainLogRegression(train_x, train_y, opts):
    numSamples, numFeatures = shape(train_x)
    alpha = opts['alpha']; maxIter = opts['maxIter']
    weight = ones((numFeatures,1))

    for k in range(maxIter):
        if opts['optimizeType'] == 'gradDescent':
            output = sigmoid(train_x * weights)
            error = train_y - output
            weights = weights + alpha * train_x.transpose() * error
        elif opts['optimizeType'] == 'smoothStocGradDescent':
            dataIndex = range(numSamples)
            for i in range(numSamples):
                alpha = 4.0 / (1.0 + k + i) + 0.01
                randIndex = int(random.uniform(0, len(dataIndex)))
                output = sigmoid(train_x[randIndex, :] * weights)
                error = train_y[randIndex, 0] - output
                weights = weights + alpha * train_x[randIndex, :].transpose() * error
        else:
            raise NameError('Not support optimize method type!')
    print('Congratulations, training complete!')
    return weight
    
def loadData():
    train_x = []
    train_y = []
    fileIn = open("C:/Python32/trytrytry.csv")
    for line in fileIn.readlines():
        lineArr = line.strip().split(',')
        n = len(lineArr)
        for i in range(0,n-2):
            train_x.append([float(lineArr[0])])
        train_y.append([float(lineArr[n-1])])
    fileIn.close
    print (train_x)
    print (train_y)
    return train_x, train_y

print ("step 1: load data....")
train_x, train_y = loadData()
test_x = train_x
test_y = train_y

print ("step 2: training.......")
opts = {'alpha': 0.01, 'maxIter': 20, 'optimizeType': 'smoothStocGradDescent'}
optimalWeights = trainLogRegression(train_x, train_y, opts) 
