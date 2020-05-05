import requests
import csv
from lxml import etree
import threading
# 爬取链家网
# 爬取淮安出租房源信息1120套
# 爬取内容为小区名、户型、面积、价格、地址
# 本次爬取使用xpath进行数据的提取
# 定义huaian_chuzu_house(i)函数进行爬取
def huaian_chuzu_house(i):
    url = 'https://m.lianjia.com/chuzu/ha/zufang/pg%s/?ajax=1' % i
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
        '537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/'
        '537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400',
        'Referer': 'https://m.lianjia.com/ha/',
        'Upgrade-Insecure-Requests': '1'
    }

    response = requests.get(url=url, headers=headers)
    html = response.text

    info_html = etree.HTML(html)
    xiaoqus = info_html.xpath('//div[@class="content__item__main"]')
    for xiaoqu in xiaoqus:
        # 先获取一套房源的信息，包括小区名、朝向、面积、地址、价格
        name = xiaoqu.xpath('.//p[@class="content__item__title"]/text()')[0].strip()
        area = xiaoqu.xpath('.//p[@class="content__item__content"]/text()')[0].strip().split('\n')[0].strip()
        address = xiaoqu.xpath('.//p[@class="content__item__content"]/text()')[0].strip().split('\n')[2].strip()
        price = xiaoqu.xpath('.//p[@class="content__item__bottom"]/text()')[0].strip()
        info = [name, area, address, price]
        save_csv_writer(info)
        # 定义字典保存信息
        rets = {
            "户型": name,
            "面积": area,
            "地址": address,
            "价格元/月": price
        }
        # 打印信息
        print(rets)
def save_csv_writer(item):
    with open('huaian_chuzu_house.csv', 'a+', encoding='utf-8', newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)
# 完成分页爬取56页共1120套房源信息
def main():
    for i in range(56):
        # 创建一个线程
        pl = threading.Thread(huaian_chuzu_house(i))
        pl.start()
        print(i)
# 调用函数
if __name__ == '__main__':
    main()