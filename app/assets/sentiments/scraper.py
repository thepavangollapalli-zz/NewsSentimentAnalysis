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
    page = requests.get(link)
    tree = html.fromstring(page.content)
    body = (tree.xpath('//*[@id="story"]/div[2]'))[0]
    data = etree.tostring(body, encoding='utf8', method="xml")
    content = clean_up.clean_html(str(data)) 
    return content

def parse(filename):
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

