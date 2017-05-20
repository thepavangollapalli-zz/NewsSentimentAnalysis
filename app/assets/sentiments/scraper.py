# should scrape all article's contents and write it to a txt
import json
import codecs
import time
import requests
import clean_up
from lxml import html
from lxml import etree
import requests
import csv
from analyzer import Analyzer
from sent_analyze import BayesClassify
import random

def get_text(link):
    # inspired by hitchhiker's
    # scrapes article's text
    # get the raw html content
    page = requests.get(link)
    tree = html.fromstring(page.content)

    # get the main article content
    body = (tree.xpath('//*[@id="story"]/div[2]'))
    
    # catch errors
    if len(body)==0:
        return ""
    body = body[0]
    # convert article content to string
    data = etree.tostring(body, encoding='utf8', method="xml")
    # clean up article content
    content = clean_up.clean_html(str(data)) 
    return content

def get_stock_price(link):
    # currently returning random value for proof of concept
    return random.uniform(20, 1000)

def parse(filename):
    # iterates through file, and loads in each url
    # scrapes text and saves it to file
    # returns aggregate score across all articles
    a = BayesClassify() # object that calculates Sentiment Score

    # loads in json in correct encoding from filename
    content = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    
    # if(len(content)==0): # if file is empty
        # return -1

    # check if articles present
    if not content || not content['response'] || not content['response']['docs']:
        return -1

    # get list of articles
    articles = content['response']['docs']
    
    if(len(articles)==0): # if no articles
        return -1


    POSITIVE = []
    NEGATIVE = []
    SCORES = list()

    with open('app/assets/sentiments/sentiments.csv', 'w+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        # write csv headers
        spamwriter.writerow(['headline', 'timestamp', 'url', 'pos', 'neutral', 'neg', 'stock_price'])
        # spamwriter.writerow([min(10, len(articles))])
        for i in range(min(10, len(articles))):
            # pull data for each article
            article = articles[i]
            datetime = str(article['pub_date'])
            link = article['web_url']
            headline = article['headline']['main']
            body = get_text(link)
            
            if(len(body)==0): # error checking
                return -1
            
            comp = 0
            pos = 0
            neg = 0
            neu = 0
            # getting positive, neutral and negative sentiment scores
            ss = a.analyzer(body)
            for k in sorted(ss):
                if(k == 'compound'):
                    SCORES.append(ss[k])
                    comp = ss[k] * 100
                elif(k == "neg"):
                    NEGATIVE.append(ss[k])
                    neg = ss[k] * 100
                elif(k == "neu"):
                    neu = ss[k] * 100
                else:
                    pos = ss[k] * 100
                    POSITIVE.append(ss[k])
                # print('{0}: {1}, '.format(k, ss[k]), end='')

            # SCORES.append((pos, neu, neg))
            # POSITIVE.append(pos_score)
            # NEGATIVE.append(neg_score)

            # dummy instantiation 
            # agg = pos-neg
            stock_price = get_stock_price(link)

            # writing rows into csv file
            row = [headline, datetime, str(link), pos, neu, neg, stock_price]
            # spamwriter.writerow([min(10, len(articles))])
            spamwriter.writerow(row)


    agg = a.aggregate(SCORES)
    # returns aggregated list of (POSITIVE, NEUTRAL, NEGATIVE) scores
    return agg

