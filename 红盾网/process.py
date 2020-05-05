import requests
import time
import csv
import pymongo
from lxml import etree
from multiprocessing import Pool

"""
本项目只用于学习，不用于获取倒卖任何信息
获取网页所有地区的链接详情页信息
Windows10
Pycharm2018
xpath
多线程
数据库
"""


class RedDum(object):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'}

    """获取页面详情页链接"""

    def get_pages(self, url):
        link_list = []
        response = requests.get(url=url, headers=self.headers)
        items = etree.HTML(response.text)
        hrefs = items.xpath('//*[@class="search-detail"]')
        for href in hrefs[4:]:
            links = href.xpath('./a/@href')
            for link in links:
                link_list.append(link)
        return link_list


    """解析详情页内容"""

    def paser_detail(self, url):
        response = requests.get(url=url, headers=self.headers)
        time.sleep(1)
        items = etree.HTML(response.text)
        titles = items.xpath('//a[@class="name"]')
        for titl in titles:  # 地区
            title = titl.xpath('./text()')[0]
        lis = items.xpath('//*[@id="list-container"]/ul/li')
        for li in lis:
            daima = li.xpath('./div/p[1]/a/span[1]/text()')[0]  # 代码
            person = li.xpath('./div/p[1]/a/span[2]/text()')[0]  # 法人
            address = li.xpath('./div/p[2]/a/span/text()')[0]  # 地址
            data = [title, daima, person, address]
            collection = {
                '地区': title,
                '代码': daima,
                '法人': person,
                '地址': address
            }
            self.mongodb(collection)
            self.save_details('\n'.join(data).replace(',', '').strip())
            print(title, daima, person, address)

    """多线程"""
    def threads_crawl(self):
        link = self.get_pages('https://www.ubaike.cn/')
        pool = Pool()
        process = pool.map(self.paser_detail, link)
        pool.join()
        pool.close()


    def save_details(self, data):
        with open('hongdun1.csv', 'a', encoding='utf-8')as f:
            write = csv.writer(f)
            write.writerow(data)

    def mongodb(self, collection):
        clinet = pymongo.MongoClient('localhost', 27017)
        db = clinet.hongdun
        table = db.hongdun_table
        table.insert_many(collection)

if __name__ == '__main__':
    k = RedDum()
    k.threads_crawl()