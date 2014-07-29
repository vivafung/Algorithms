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
        currentlable = featureVec[-1]
        if currentlable not in list(lableCounts.keys()):
            list(lableCounts.keys())[currentlable] = 0
        list(lableCounts.keys())[currentlable] += 1

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


def majorityCnt(classList):  
    classCount={}  
    for vote in classList:  
        if vote not in classCount.keys(): classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)  
    return sortedClassCount[0][0]  


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
            subdata = splitDate(dataset, i, value)
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
    classList = [example[-1] for example in dataset]
    #stop splitting when all the features are the same
    if(classList.count(classList[0]) == len(classList)):
        return classList[0]
    #stop splitting when there is no feature left
    if(len(dataset[0]) == 1):
        return majorityCnt(classList)

    #define the root of tree
    root = bestFeatureSelection(dataset)
    rootLable = lable(root)
    #define the tree
    tree = {rootLable: {}}
    featureValue = [example[root] for example in dataset]
    uniqueFeatureValue = set(featureValue)
    #iteratively generate the decision tree
    for value in uniqueFeatureValue:
        sublables = lable[:]
        tree = createTree(splitDate(dataset, root, value), sublables)

    return tree


def classify(inputTree,featLabels,testVec):  
    firstStr = list(inputTree.keys())[0]  
    secondDict = inputTree[firstStr]  
    featIndex = featLabels.index(firstStr)  
    key = testVec[featIndex]  
    valueOfFeat = secondDict[key]  
    if isinstance(valueOfFeat, dict):  
        classLabel = classify(valueOfFeat, featLabels, testVec)  
    else: classLabel = valueOfFeat  
    return classLabel


def grabTree(filename):
    f = open(filename)
    return pickle.load(f)


def storeTree(tree, filename):
    fw = open(filename, 'w')
    pickle.dump(tree,fw)
    fw.close()


dataSet = [[1, 1, 'yes'],  
               [1, 1, 'yes'],  
               [1, 0, 'no'],  
               [0, 1, 'no'],  
               [0, 1, 'no']]
lables = ['no surfacing','flippers']
createTree(dataSet, lables)
