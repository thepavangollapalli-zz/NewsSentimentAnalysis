import csv
import numpy as np
import time

class Parser(object):

    # Creates a Parser object
    # filename: the name of the csv file to be parsed
    def __init__(self, filename):
        self.filename = filename
        self.columns = None
        self.features = None
        self.labels = None


    def get_columns(self):
        with open(self.filename, 'rt') as feature_file:
            feature_reader = csv.reader(feature_file)
            vector = next(feature_reader)
            return vector[0][2:]
        
    # Instantiates the columns, features, and labels fields by
    # parsing the csv
    def parse(self):
        def make_count(a):
            if a == "":
                return 0
            elif a == "true":
                return 1
            else:
                return 0

        def make_bool(a):
            if a == "REAL":
                return 1
            else:
                return 0
            
        with open(self.filename, 'rt') as feature_file:
            feature_reader = csv.reader(feature_file)

            #separates each row into (label, feature) tuples
            print("Separating features...")
            vector = [(row[1], row[2:]) for row in feature_reader]

            #The column headings (i.e., "title:Trump")
            self.columns = vector[0][1]
            
            vector = vector[1:]
            
            #unzips the tuples to make a label set and a feature set
            print("Unzipping labels...")
            (labels, features) = (np.array([make_bool(a)  for (a, b) in vector]),
                                  np.array([[make_count(x) for x in b] for (a, b) in vector]))

            #All feature, label vectors without the column headings
            self.features = features
            self.labels = labels

    # Gets the data split between a train set and a test set
    # Train percentage set to 85% by default (don't now how we should split it, just guessed lol)
    # Returns a dict with "train", "test", and "columns" as its entries. Traind and test are lists
    #         of tuples of (feature vector, label) and columns is the column headings of each
    #         feature vector (i.e., title:trump)
    def get_split_data(self, train_percentage=0.85):
        #check if train_percentage is valid
        if(train_percentage > 1.0 or train_percentage < 0.0):
            print("Invalid train percentage")
            return

        #find the index of the split
        index = int(float(len(self.labels)) * train_percentage * (2.0 / 3.0))
        end = int(float(len(self.labels)) * (2.0 / 3.0))
        
        print("Splitting data into")
        print("  - {} train pairs".format(index))
        print("  - {} test pairs".format(end - index))
        print("  - {} final testing pairs".format(len(self.labels) - end))
        #split into train and test, return a dictionary with relevant info
        data = dict()
        data["train"] = (self.features[:index], self.labels[:index])
        data["test"] = (self.features[index:end], self.labels[index:end])
        data["final"] = (self.features[end:], self.labels[end:])
        data["columns"] = self.columns
        return data
 
    # Returns the number of columns in the dataset
    # (i.e., the length of the feature vector)
    def num_columns(self):
        return len(self.columns)
    
    # Returns the number of rows in the dataset
    # (i.e., the number of feature vectors)
    def num_rows(self):
        return len(self.labels)
