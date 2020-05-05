import requests
import time
import csv
from lxml import etree

"""
获取网页所有地区的链接
"""
"""
类调用
"""


class RedDum(object):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3730.400 QQBrowser/10.5.3805.400'}
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
        #print(link_list)

    """解析详情页内容"""
    def paser_detail(self, url):
        for link in self.get_pages(url):
            response = requests.get(url=link, headers=self.headers)
            time.sleep(1)
            items = etree.HTML(response.text)
            titles = items.xpath('//a[@class="name"]')
            for titl in titles:    #地区
                title = titl.xpath('./text()')[0]
            lis = items.xpath('//*[@id="list-container"]/ul/li')
            for li in lis:
                daima = li.xpath('./div/p[1]/a/span[1]/text()')[0]   #代码
                person = li.xpath('./div/p[1]/a/span[2]/text()')[0]  #法人
                address = li.xpath('./div/p[2]/a/span/text()')[0]    #地址
                data = [title, daima, person, address]
                self.save_details('\n'.join(data).replace(',', '').strip())
                print(title, daima,person,address)

    """保存数据"""
    def save_details(self, data):
        with open('hongdun.csv', 'a', encoding='utf-8')as f:
            write = csv.writer(f)
            write.writerow(data)

if __name__ == '__main__':
    """类调用"""
    k = RedDum()
    k.paser_detail('https://www.ubaike.cn/')