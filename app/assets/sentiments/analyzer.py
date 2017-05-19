#!/usr/bin/python
# import nltk
import re

#define a class that implements sentiment analysis using 

class Analyzer(object): 
    #initialize the Analyzer 
    def __init__(self, positives = "positive-words.txt", negatives = "negative-words.txt"):
        # self.filename = filename
        # self.text = 
        self.p = positives
        self.n = negatives

    #analyze text for positive sentiments returning its score
    def analyze_p(self, text):
        #open the positives file and convert it into a list
        with open(self.p, "r") as positives:
            positives = set(positives.read().split())

        #convert the text inputted (content of articles) into a list
        #remove all punctuation like (,),.,,
        text = (re.sub(r'([^\s\w]|_)+', '', text)).split()

        #calculate the sum of positive words
        sum_p = 0
        for word in text:
            if word in positives:
                sum_p += 1

        #return percentage of positive words in inputted text
        return (sum_p * 1.0 / len(text)) * 100

    #analyze text for negative sentiment returning ts score 
    def analyze_n(self, text):
        #open the negatives file and convert it into a list
        with open(self.n, "r") as negatives:
            negatives = set(negatives.read().split())

        #convert the text inputted (content of articles) into a list
        #remove all punctuation like (,),.,,
        text = (re.sub(r'([^\s\w]|_)+', '', text)).split()

        #calculate the sum of positive words
        sum_n = 0
        for word in text:
            if word in negatives:
                sum_n += 1

        #return percentage of positive words in inputted text
        return (sum_n * 1.0 / len(text)) * 100

        





