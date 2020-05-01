import requests
import time
from lxml import etree
import csv
from multiprocessing.dummy import Pool as pl
#多线程爬虫
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/70.0.3538.110 Safari/537.36',
           'cookie':'acw_tc=df6fef1815477102230532021e7fe39885753c03285576726532515c34; qchatid=c389e1db-6e8d-4c5e-b221-09117b8251e4; WINDOW_DEVICE_PIXEL_RATIO=0.8999999761581421; _ga=GA1.3.615197497.1547710276; sid=949843ed-c329-4fd5-a705-2e7b714dd295; '
                    '_gid=GA1.3.1777438499.1550133959;'
                    ' CITY_NAME=SHENZHEN; SALEROOMREADRECORDCOOKIE=100451421%23100442428%23100460607; looks=SALE%2C100442428%2C55538%7CSALE%2C100460607%2C56752; sec_tc=AQAAABBhjGC3RggAt9QQ9FAaG1xouNgw; acw_sc__v2=5c6570ca4d965b68254e6cbe3f24506534183b6c; '
                    'JSESSIONID=aaaYg3hRQG28n5atkqSJw; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1547710276,1550133958,1550150022,1550151888; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1550151902; cookieId=247b30e2-73f7-49ea-96e6-5613975ab09f'
           }

def download(url):  #定义下载函数
    html = requests.get(url=url, headers=headers)
    time.sleep(3)
    return etree.HTML(html.text)
def data_writer(item):  #定义数据写入保存函数
    with open('qfang_ershoufang.csv', 'a+', encoding='utf-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(item)

def spider(url):  #定义爬取函数
    selector = download(url)
    house_list = selector.xpath("//*[@id='cycleListings']/ul/li")
    for house in house_list:
        apartment = house.xpath("div[1]/p[1]/a/text()")[0]
        house_layout = house.xpath("div[1]/p[2]/span[2]/text()")[0]
        area = house.xpath("div[1]/p[2]/span[4]/text()")[0]
        region = house.xpath("div[1]/p[3]/span[2]/a[1]/text()")[0]
        total_price = house.xpath("div[2]/span[1]/text()")[0]
        house_url = ('https://shenzhen.qfang.com'+house.xpath("div[1] / p[1] / a/@href")[0])
        sel = download(house_url)
        house_years = sel.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[2]/div/ul/li[3]/div/text()')[0]
        mortgage_info = sel.xpath('//*[@id="scrollto-1"]/div[2]/ul/li[2]/div/ul/li[5]/div/text()')[0]
        item = [apartment, house_layout, area, region, total_price, house_years, mortgage_info]
        print('正在抓取', apartment)
        data_writer(item)
if __name__ == "__main__":
    pre_url = 'https://shenzhen.qfang.com/sale/f'
    pool = pl(4)
    house_url = [pre_url+str(x) for x in range(1, 3)]
    pool.map(spider, house_url)
    pool.close()
    pool.join()
