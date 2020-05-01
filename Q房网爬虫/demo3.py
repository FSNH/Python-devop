import requests
import time
from lxml import etree
import csv
#网站爬虫采取了反爬虫措施，这边反反爬虫策略就是添加Cookie头
#爬取Q房源网的详情信息并保存为csv
#爬取具体内容有："小区名称", "户型", "面积", "装修", "楼层", "朝向",
#  "售价", "总价/万", "详情"
#定义spider_page()函数爬取并返回页面信息
def spider_page(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/70.0.3538.110 Safari/537.36',
               'upgrade-insecure-requests': '1',
               'cookie':'qchatid=c389e1db-6e8d-4c5e-b221-09117b8251e4; _ga=GA1.3.615197497.1547710276; CITY_NAME=SHENZHEN; SALEROOMREADRECORDCOOKIE=100451421%23100442428%23100460607; looks=SALE%2C100442428%2C55538%7CSALE%2C100460607%2C56752; cookieId=da1e6738-c45b-4de6-97e1-8c525fb9cfef; sec_tc=AQAAAIF2KnyWFgoA32uMVXQEbAhfgcmz; acw_tc=df6fef1b15606729096611896e68cec0eadb7ce0b82f2162766542d1de; sid=c15a446d-961a-44e5-9cac-3616f5fa0987; language=SIMPLIFIED; JSESSIONID=aaakIkClOr3Fx66yRwFTw; acw_sc__v2=5d05fa8d3b852a2db1045de5b468191b4a1deffc; WINDOW_DEVICE_PIXEL_RATIO=1.100000023841858; _gid=GA1.3.534628977.1560672931; _dc_gtm_UA-47416713-1=1; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1560672931; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1560672931'}

    response = requests.get(url, headers=headers)
    time.sleep(2)#延迟两秒时间
    return response.text

#创建csv保存函数
def csv_data(item):
    with open('fangwo_info1.csv', 'a+', encoding='utf-8', newline='')as csvfile:#newline设置为''可以去点换行
        writer = csv.writer(csvfile)
        writer.writerow(item)

def paser_info(url):
    # 解析页面
    html = spider_page(url)
    selector = etree.HTML(html)#以构造器的形式返回
    house_infos = selector.xpath('//*[@id="cycleListings"]/ul/li')
    for house_info in house_infos:
        name = house_info.xpath('./div[1]/p[1]/a/text()')[0].split(' ', 1)[0]
        xiangq = house_info.xpath('./div[1]/p[1]/a/text()')[0].split(' ', 1)[1]
        style = house_info.xpath('./div[1]/p[2]/span[2]/text()')[0]
        area = house_info.xpath('./div[1]/p[2]/span[4]/text()')[0]
        decotored = house_info.xpath('./div[1]/p[2]/span[6]/text()')[0]
        louceng = house_info.xpath('./div[1]/p[2]/span[8]/text()')[0].strip()
        chaoxiang = house_info.xpath('./div[1]/p[2]/span[10]/text()')[0]
        total = house_info.xpath('./div[2]/span[1]/text()')[0]
        price = house_info.xpath('./div[2]/p/text()')[0]
        info = [name, style, area, decotored, louceng, chaoxiang, price, total, xiangq]
        csv_data(info)
        print("正在爬取", name)#编辑器里打开显示爬取

#创建主函数
def main():
    # 添加csv标题头
    info_title = ["名称", "户型", "面积", "装修", "楼层", "朝向", "售价", "总价/万", "详情"]
    csv_data(info_title)
    urls = ['https://shenzhen.qfang.com/sale/f%s' % x for x in range(1, 10)]
    for url in urls:
        paser_info(url)

# 调用函数运行
if __name__ == '__main__':
    main()