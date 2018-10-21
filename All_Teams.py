import csv
import pandas
import codecs
from datetime import datetime
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

# creates dataset from file
filename = "allFootball.csv"
wholeSchedule = pandas.read_csv(filename, index_col=0)

# general form of the dictionary
tweetdict = {"9-1-2017": 0}

# List for Tweets
tweetlist = []

# finds count of tweets and fills dataset with values
with open('tweets2017.txt', "r") as file:
    # adds all values to the dictionary to count total num of tweets
    for line in file:
        key = line.split(' ')[0]
        if key in tweetdict:
            tweetdict[key] = tweetdict.get(key) + 1
        else:
            tweetdict[key] = 1

    # start at day 8 since 31st was a Sunday
dayCount = 8
weekCount = 16
totalTweets = 0
# adds in every day with tweet count
for k in tweetdict:
    totalTweets += tweetdict.get(k)
    dayCount -= 1
    if dayCount == 0:
        tweetlist.append(totalTweets)
        totalTweets = 0
        dayCount = 7
        weekCount -= 1

# reverses tweetlist to put it in correct order
tweetlist.reverse()

# adds total tweets, separate index for tweetList
tIndex = 0
for index, row in wholeSchedule.iterrows():
    wholeSchedule.loc[index, 'TwtCount'] = tweetlist[tIndex]
    tIndex += 1
    if tIndex >= 17:
        tIndex = 0

print(wholeSchedule[['Day', 'TwtCount']])

# histogram
# wholeSchedule[['Tm', 'Opp', 'TotYdOff', 'TwtCount']].hist()
# plt.show()

# scatter plot matrix
# scatter_matrix(wholeSchedule.groupby(['Team', 'New England Patriots'])[['Tm', 'Opp', 'TotYdOff', 'TwtCount']])
# plt.show()

columns = ['Week', 'Points Scored', 'Points Let', 'Offensive Yards', 'Num Tweets']
weeklyChange = pandas.DataFrame(columns=columns)

for weekIndex in range(1, 17):
    pointsScored = 0
    pointsLet = 0
    offensiveYards = 0
    numTweets = tweetlist[weekIndex - 1]
    for team in wholeSchedule:
        if team.index == weekIndex:
            pointsScored += team['Tm']
            pointsLet += team['Opp']
            offensiveYards += team['TotYdOff']
    weeklyChange.loc[weekIndex] = [weekIndex, pointsScored, pointsLet, offensiveYards, numTweets]

print(weeklyChange.head())

# histogram
# weeklyChange[['Points Scored', 'Points Let', 'Offensive Yards', 'Num Tweets']].hist()
# plt.show()
