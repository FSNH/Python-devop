import requests
import time
from lxml import etree
import csv
import pymongo
"""
获取网页所有地区的链接
"""
"""函数调用"""
def get_pages(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',
        'cookie': 'whatsnssid=1fabec2f3d878037; whatsnslastrefresh=1; PHPSESSID=pflo3tmnmu8evmvqgd63jame00; Hm_lvt_373863c10d213ef78db501916c4d69d1=1568011305,1568456580,1568457966,1569418681; Hm_lpvt_373863c10d213ef78db501916c4d69d1=1569418681'}
    link_list = []
    response = requests.get(url=url, headers=headers)
    items = etree.HTML(response.text)
    hrefs = items.xpath('//*[@class="search-detail"]')
    for href in hrefs[4:]:
        links = href.xpath('./a/@href')
        for link in links:
            link_list.append(link)
    return link_list

    #print(link_list)

"""解析详情页内容"""

def paser_detail(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400',
        'cookie': 'whatsnssid=1fabec2f3d878037; whatsnslastrefresh=1; PHPSESSID=pflo3tmnmu8evmvqgd63jame00; Hm_lvt_373863c10d213ef78db501916c4d69d1=1568011305,1568456580,1568457966,1569418681; Hm_lpvt_373863c10d213ef78db501916c4d69d1=1569418681'}
    proxy = {
        "http": "http://49.83.59.101:8118"
        }
    for href in get_pages(url):
        response = requests.get(url=href, headers=headers)
        time.sleep(1)

        items = etree.HTML(response.text)
        titles = items.xpath('//a[@class="name"]')
        for titl in titles:
            title = titl.xpath('./text()')[0]
        lis = items.xpath('//*[@id="list-container"]/ul/li')
        for li in lis:
            daima = li.xpath('./div/p[1]/a/span[1]/text()')[0]
            person = li.xpath('./div/p[1]/a/span[2]/text()')[0]
            address = li.xpath('./div/p[2]/a/span/text()')[0]
            data = [title, daima, person, address]
            collection = {
                '地区': title,
                '代码': daima,
                '法人': person,
                '地址': address
            }
            mongodb(collection)
            save_details('\n'.join(data).replace(',', '').strip())
            print(title, daima, person, address)

def save_details(data):
    with open('hongdun.csv', 'a', encoding='utf-8')as f:
        write = csv.writer(f)
        write.writerow(data)
def mongodb(collection):
    clinet = pymongo.MongoClient('localhost', 27017)
    db = clinet.hongdun
    table = db.hongdun_table
    table.insert_many(collection)


if __name__ == '__main__':
    paser_detail('https://www.ubaike.cn/')