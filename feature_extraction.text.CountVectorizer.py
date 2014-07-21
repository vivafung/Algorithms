from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups

measurements = [
{'city': 'Dubai', 'temperature': 33.6},
{'city': 'London', 'temperature': 12.9},
{'city': 'San Fransisco', 'temperature': 18.5}]

vec = DictVectorizer()
vecArr = vec.fit_transform(measurements).toarray()
print(vecArr)
featureNames = vec.get_feature_names()
print(featureNames)

# Define and load the data
categories = ['alt.atheism']
print("Loading 20 newsgroups dataset for categories:")
print(categories)

data = fetch_20newsgroups(subset='train', categories=categories)

corpus = ['For applications of DFS in relation to specific domains, such as searching for solutions in artificial intelligence or web-crawling, the graph to be traversed is often either too large to visit in its entirety or infinite (DFS may suffer from non-termination). In such cases, search is only performed to a limited depth; due to limited resources, such as memory or disk space, one typically does not use data structures to keep track of the set of all previously visited vertices. When search is performed to a limited depth, the time is still linear in terms of the number of expanded vertices and edges (although this number is not the same as the size of the entire graph because some vertices may be searched more than once and others not at all) but the space complexity of this variant of DFS is only proportional to the depth limit, and as a result, is much smaller than the space needed for searching to the same depth using breadth-first search. For such applications, DFS also lends itself much better to heuristic methods for choosing a likely-looking branch. When an appropriate depth limit is not known a priori, iterative deepening depth-first search applies DFS repeatedly with a sequence of increasing limits. In the artificial intelligence mode of analysis, with a branching factor greater than one, iterative deepening increases the running time by only a constant factor over the case in which the correct depth limit is known due to the geometric growth of the number of nodes per level.']
vectorizer = CountVectorizer(binary = False, max_df = 1, min_df = 1)
X = vectorizer.fit_transform(data)
n = X.shape
print(n)
vecNames = vectorizer.get_feature_names()
print(vecNames)
Arr1 = X.toarray()
print(Arr1)
print(vecNames[117],vecNames[80])
print(Arr1[:,117],Arr1[:,80])

voca1 = vectorizer.vocabulary_.get('infinite')
voca2 = vectorizer.vocabulary_.get('the')
voca3 = vectorizer.vocabulary_.get('of')
print(voca1,voca2,voca3)

bigram_vectorizer = CountVectorizer(ngram_range = (1,2),min_df=1)
X_2 = bigram_vectorizer.fit_transform(data).toarray()
print(X_2)

#TF-IDF term weighting--term-frequency times inverse document-frequency
transformer = TfidfTransformer()
tfidfVal = transformer.fit_transform(Arr1)
Arr2 = tfidfVal.toarray()
print(Arr2)

