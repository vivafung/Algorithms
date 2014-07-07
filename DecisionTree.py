import numpy as np
import matplotlib.pyplot as plt  
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
    #print (train_x)
    #print (train_y)
    return train_x, train_y


print ("step 1: load data....")
train_x, train_y = loadData()
test_x = train_x
test_y = train_y
print("the size of train_x is: ", train_x.shape)
print("the size of train_y is: ", train_y.shape)


# Fit regression model
MODEL = DecisionTreeRegressor(max_depth = 6,random_state=0)
MODEL.fit(train_x, train_y, sample_mask=None, X_argsorted=None, check_input=True, sample_weight=None)
score_Acc = MODEL.score(train_x, train_y)
feature_importance = MODEL.feature_importances_
print("the feature_importance is: ", feature_importance)
print("the score is: ", score_Acc)

# make importance relative to max importance
feature_importance = 1000. * feature_importance
plt.plot(feature_importance, 'ro')
plt.axis([0, 8, 0, 10])
plt.xlabel('vector')
plt.ylabel('feature_importance')
plt.title('Histogram of feature_importance')
plt.grid(True)
plt.show()
