# Load libraries
import csv
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
filename = "football.csv"
dataset = pandas.read_csv(filename, index_col=0)

# histogram
# dataset[['TmScore', 'OppScore', 'TotYdOff', 'TotYdDef']].hist()
# plt.show()

# scatter plot matrix
# scatter_matrix(dataset[['TmScore', 'OppScore', 'TotYdOff', 'TotYdDef']])
# plt.show()

# pandas before the addition
print(dataset[['Date', 'TwtCount']])

# general form of the dictionary
tweetdict = {"0/0/0000": 0}

# finds count of tweets and fills dataset with values
with open('tweets.csv', newline='') as csvfile:
    tweetreader = csv.reader(csvfile)
    for row in tweetreader:
        key = ''.join(row).split(' ')[0]
        if key in tweetdict:
            tweetdict[key] = tweetdict.get(key) + 1
        else:
            tweetdict[key] = 1

    for index, row in dataset.iterrows():
        if row['Date'] in tweetdict:
            dataset.loc[index, 'TwtCount'] = tweetdict[row['Date']]
            print(row['TwtCount'])

    print(dataset[['Date', 'TwtCount']])
