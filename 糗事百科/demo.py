from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re
import requests
from pyquery import PyQuery as pq

browser = webdriver.Firefox()
browser.get('https://www.qiushibaike.com/text/')
time.sleep(1)
html = browser.page_source
browser.close()
# f = open('file1.html', 'r', encoding='utf-8')
# html = f.read()
print(html)
def get_url(url):
    resp = requests.get(url)
    html = resp.text
    return html
def paser_html(html):
    list_title=[]
    bs = BeautifulSoup(html, 'lxml')
    for title in bs.find_all(name='h2'):
        for tit in title:
            return list_title.append(tit)
            #return tit.strip()
    # for contents in bs.find_all(class_='content'):
    #     for span in contents:
    #         for cont in span:
    #             return cont


if __name__ =='__main__':
    url = 'https://www.qiushibaike.com'
    html = get_url(url)
    con = paser_html(html)




