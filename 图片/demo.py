import requests
import pymongo
from lxml import etree

def get_pics():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'}
    for x in (1, 12):
        url = 'https://www.ivsky.com/tupian/ziranfengguang/index_{}.html'.format(x)

        resp = requests.get(url, headers=headers)
        item = etree.HTML(resp.text)
        items = item.xpath('/html/body/div[3]/div[2]/ul/li')
        for detail_url in items:
            detail_urls = detail_url.xpath('./div/a/@href')[0]
            detail_urls = 'https://www.ivsky.com' + detail_urls
            resp = requests.get(url=detail_urls, headers=headers)
            item = etree.HTML(resp.text)
            title = item.xpath('/html/body/div[3]/div[3]/div[1]/h1/text()')[0]
            items = item.xpath('/html/body/div[3]/div[4]/ul/li')
            for pic_url in items:
                pic = pic_url.xpath('.//a/img/@src')[0]
                pic = 'http:' + pic
                patter = pic.split('/')[-1]
                print(pic)
                pic_con = requests.get(url=pic, headers=headers)
                tupian = {
                    title: pic_con.content
                }
                client = pymongo.MongoClient(host='localhost', port=27017)
                db = client.picture
                collection = db.pic
                collection.insert_one(tupian)

                # with open('D:\爬虫\JPG\\' + patter, 'wb')as f:
                #     f.write(pic_con.content)

if __name__ == '__main__':
    get_pics()