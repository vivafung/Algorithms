import csv
from sklearn.ensemble import RandomForestClassifier
import numpy

def read_csv(file_path, has_header = True):
    with open(file_path) as f:
        if has_header:
            f.readline()
            data = []
            for line in f:
                line = line.strip().split(',')
                data.append([x for x in line])
    return data


def write_csv(file_path, data):
    with open(file_path, 'w') as f:
        for line in data:
            f.write(','.join(line)+'\n')
    

def loaddata():
    input_file_path = "C:\Python32\A2PW1.csv"
    data = read_csv(input_file_path, has_header = True)
    print(data)
    output_file_path = "C:\Python32\pythontoday.csv"
    out = write_csv(output_file_path, data)

def main():
    #Loading the training set and test set
    path1 = "C:\Python32\A2PW1.csv"
    path2 = "C:\Python32\A2PW3.csv"
    train = read_csv(path1, has_header = True)
    target = [x[0] for x in train]
    train = [x[1:] for x in train]
    test = read_csv(path2, has_header = True)
    test = [x[1:] for x in test]
    print('The training set is:')
    print(train)
    print('The test set is:')
    print(test)

    #create the model
    rf = RandomForestClassifier(n_estimators = 100)
    #throw the data into model
    rf.fit(train, target)
    predicted_probs = rf.predict_log_proba(test)
    print(predicted_probs)
    output_file_path = "C:\Python32\pythontoday.txt"
    numpy.savetxt(output_file_path, predicted_probs,delimiter=',',fmt='%1.4e')

    newArr = rf.fit_transform(test,target)
    print('newArr becomes: ',newArr)
    
if __name__ == "__main__":
    main()
