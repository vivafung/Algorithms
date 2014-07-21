
from pprint import pprint
from time import time
import logging

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline

# Load some categories from the training set
categories = ['alt.atheism','talk.religion.misc']
print("Loading 20 newsgroups dataset for categories:")
print(categories)

data = fetch_20newsgroups(categories=categories)
print("%d documents" % len(data.filenames))
print("%d categories" % len(data.target_names))
print()

parameters = {
    'vect__max_df': (0.5, 0.75, 1.0),
    #'vect__max_features': (None, 5000, 10000, 50000),
    'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
    #'tfidf__use_idf': (True, False),
    #'tfidf__norm': ('l1', 'l2'),
    'clf__alpha': (0.00001, 0.000001),
    'clf__penalty': ('l2', 'elasticnet'),
    #'clf__n_iter': (10, 50, 80),
}

if _name_ == '_main_':
    # find the best parameters for both the feature extraction and the classifier
    grid_search = GridSearchCV(pipeline, parameters, n_jobs = -1)
    grid_search.fit(data.data, data.target)
    best_parameters = grid_search.best_estimator_.get_params()
