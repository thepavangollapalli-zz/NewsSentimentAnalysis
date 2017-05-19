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
    page = requests.get(link)
    tree = html.fromstring(page.content)

    body = (tree.xpath('//*[@id="story"]/div[2]'))
    if len(body)==0:
        return ""
    else:
        body = body[0]
    data = etree.tostring(body, encoding='utf8', method="xml")
    content = clean_up.clean_html(str(data)) 
    return content

def get_stock_price(link):
    return random.uniform(20, 1000)

def parse(filename):
    # iterates through file, and loads in each url
    # scrapes text and saves it to file
    # returns aggregate score across all articles
    a = Analyzer()
    # print(filename)
    content = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    # print(content)
    if len(content)==0:
        return -1
    articles = content['response']['docs']
    
    if len(articles)==0:
        return -1


    # POSITIVE = []
    # NEGATIVE = []
    scores = list()

    with open('app/assets/sentiments/sentiments.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        # write csv headers
        spamwriter.writerow(['headline', 'timestamp', 'url', 'pos', 'neg', 'agg', 'stock_price'])
        print(min(10, len(articles)))
        for i in range(min(10, len(articles))):
        # for article in articles:
            # pull data for each article
            article = articles[i]
            datetime = str(article['pub_date'])
            link = article['web_url']
            headline = article['headline']['main']
            body = get_text(link)
            
            # print(body)
            if len(body)==0:
                return -1
            
            # getting positive and negative sentiment scores
            
            scores.append(a.analyzer(body))
            # POSITIVE.append(pos_score)
            # NEGATIVE.append(neg_score)

            # dummy instantiation 
            agg = pos_score-neg_score
            stock_price = get_stock_price(link)

            # writing rows into csv file
            row = [headline, datetime, str(link), pos_score, neg_score, agg, stock_price]
            spamwriter.writerow(row)


    agg = a.aggregate(POSITIVE, NEGATIVE)
    return agg

