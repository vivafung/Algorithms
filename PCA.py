import numpy as np
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeRegressor
import csv
import sys

def loadData():
    x = []
    y = []
    fileIn = open("C:/Python32/trytrytry.csv")
    for line in fileIn.readlines():
        lineArr = line.strip().split(',')
        x.append([float(lineArr[0]),float(lineArr[1]),float(lineArr[2]),float(lineArr[3]),float(lineArr[4]),float(lineArr[5]),float(lineArr[6]),float(lineArr[7])])
        y.append([float(lineArr[8])])
    fileIn.close
    train_x = np.array(x)
    train_y = np.array(y)
    print (train_x)
    print (train_y)
    return train_x, train_y


print ("step 1: load data....")
train_x, train_y = loadData()
test_x = train_x
test_y = train_y
print("the size of train_x is: ", train_x.shape)
print("the size of train_y is: ", train_y.shape)

pca = PCA()
X_r = pca.fit(train_x).transform(train_x)
print(X_r)
print('explained variance ratio (first two components): %s'
      % str(pca.explained_variance_ratio_))

# Fit regression model

clf_1 = DecisionTreeRegressor(max_depth=2)
clf_2 = DecisionTreeRegressor(max_depth=5)
clf_1.fit(train_x, train_x)
clf_2.fit(train_x, train_x)

# Predict
