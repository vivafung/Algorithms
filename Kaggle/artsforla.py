import csv as csv
import sys
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def main():
	df = pd.read_csv("Downloads/schools.csv")
	print df.info()
	print df.describe()

if __name__ == "__main__":
	main()