from math import log
import pickle
import operator

def createData():
    dataSet = [[1, 1, 'yes'],  
               [1, 1, 'yes'],  
               [1, 0, 'no'],  
               [0, 1, 'no'],  
               [0, 1, 'no']]
    lables = ['no surfacing','flippers']
    return dataSet, lables

def shannonEnt(dataset):
    dataSize = len(dataset)
    lableCounts = {}
    ShannonEnt = 0.0
    
    #counting the occurance
    for featureVec in dataset:
        currentlable = featureVec
        if currentlable not in lableCounts.keys():
            lableCounts[currentlable] = 0
        lableCounts[currentlable] += 1

    for key in lableCounts:
        #computing probability
        prob = float(lableCounts[key])/dataSize
        #computing shannon Entropy
        ShannonEnt = -prob * log(prob, 2)
    return ShannonEnt

def splitDate(dataset, axis, value):
    newDataSet = []
    for featureVec in dataset:
        if(featureVec[axis] == value):
            newfeatureVec = featureVec[:axis]
            newfeatureVec = newfeatureVec.extend(featureVec[axis+1:])
            newDataSet.append(newfeatureVec)
    return newDataSet

def bestFeatureSelection(dataset):
    #define the base entropy
    numFeature = len(dataset) - 1
    baseEnt = shannonEnt(dataset)
    newEnt = 0.0
    bestFeature = -1
    bestInfoGain = 0.0
    
    for i in range(numFeature):
        #create the list to store the features
        featureList = [example[i] for example in dataset]
        UniqueFeature = set(featureList)

        for value in UniqueFeature:
            subdata = splitDate(dataset)
            tempProb = len(subdata)/len(dataset)
            newEnt = tempProb * shannonEnt(subdata)
            #computing information gain = base entropy - new entropy
            infoGain = baseEnt - newEnt
            #compare and assign new value
            if(infoGain > bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i

    return bestFeature


def createTree(dataset, lable):


def grabTree(filename):
    f = open(filename)
    return pickle.load(f)


def storeTree(tree, filename):
    fw = open(filename, 'w')
    pickle.dump(tree,fw)
    fw.close()
    
