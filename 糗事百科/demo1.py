from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from lxml import etree
browser = webdriver.Firefox()
browser.get('https://www.qiushibaike.com/text/')
time.sleep(1)
html = browser.page_source
selector = etree.HTML(html)

items = selector.xpath('//*[@id="qiushi_tag_121534095"]')
for item in items:
    # /html/body/div[3]/div/div[1]/div[2]/div[1]/a[2]/h2
    title = item.xpath('/html/body/div[3]/div/div[1]/div[2]/div[1]/a[2]/h2/text()')[0]
    # /html/body/div[3]/div/div[1]/div[2]/a[1]/div/span
    content = item.xpath('/html/body/div[3]/div/div[1]/div[2]/a[1]/div/span/text()')[0]
    # /html/body/div[3]/div/div[1]/div[2]/div[2]/span[1]/i
    haoxiao = item.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/span[1]/i/text()')[0]
    # /html/body/div[3]/div/div[1]/div[2]/div[2]/span[2]/a/i
    comments = item.xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/span[2]/a/i/text()')[0]
    info = [title, content, haoxiao, comments]
    print(title,content)

# browser.close()