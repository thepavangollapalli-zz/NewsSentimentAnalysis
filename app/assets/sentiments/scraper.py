# should scrape all article's contents and write it to a txt
import json
import codecs
import time
import requests
import clean_up
from lxml import html
from lxml import etree
import requests

def get_text(link):
    # inspired by hitchhiker's
    # scrapes article's text
    page = requests.get(link)
    tree = html.fromstring(page.content)
    body = (tree.xpath('//*[@id="story"]/div[2]'))[0]
    data = etree.tostring(body, encoding='utf8', method="xml")
    content = clean_up.clean_html(str(data)) 
    return content

def parse(filename):
    # iterates through file, and loads in each url
    # scrapes text and saves it to file
    # returns dictionary with key=headline, value=body of article
    content = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
    articles = content['response']['docs']
    text_articles = dict()
    for article in articles:
        link = article['web_url']
        body = get_text(link)   
        headline = article['headline']['main']
        FILE = headline + ".txt"
        f = open(FILE, "w")
        f.write(body)
        f.close()
        text_articles[headline] = body
    return text_articles

