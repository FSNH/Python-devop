import requests
import time
import csv
from lxml import etree
# 我爱我家房源信息
# 网址：http://bj.5i5j.com/ershoufang
# 爬取信息为：名称、价格、经济人名称
def get_page(url):
    headers = {'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                             '537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/'
                             '537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400',
               'Referer': 'http://bj.5i5j.com/ershoufang/n1/',
               'Cookie':'yfx_c_g_u_id_10000001=_ck19022116084813839206365574151; _ga=GA1.2.172982220.1550736528; ershoufang_BROWSES=41857749%2C42331571; PHPSESSID=c6j2a46p5apju2667pnrhqk2gk; domain=bj; yfx_f_l_v_t_10000001=f_t_1550736528365__r_t_1551407385571__v_t_1551407385571__r_c_2; _gid=GA1.2.1753629442.1551407389; _gat=1; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1550736529,1550759657,1550824470,1551407393; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1551407393; _Jo0OQK=3C360A430707C39DC66841396A856BB9F1CDAFCCCBE5DD3EF55A648ADA5CBA77AEE43F896CA59E44D089FA0454846BD97D221FB8F73A12B808A197E69B45975E9E5C57212F12283777C840763663251ADEB840763663251ADEB8B9BB377FBE15866A593CD374DB85252GJ1Z1dg=='
               }
    response = requests.get(url=url, headers=headers)
    time.sleep(2)
    html = response.text
    return html
def parse(url):
    selector = etree.HTML(get_page(url))
    # 获取房源列表信息
    house_list = selector.xpath('//ul[@class="pList"]/li')
    for house in house_list:
        apartment = house.xpath('div[@class="listCon"]/h3[@class="listTit"]/a/text()')[0]
        total_price = house.xpath('//div[@class="jia"]/p[@class="redC"]/strong/text()')[0]
        detail_url = 'https://bj.5i5j.com' + house.xpath('div[2]/h3/a/@href')[0]
        selector1 = etree.HTML(get_page(detail_url))
        name = selector1.xpath('/html/body/div[3]/div[2]/div[2]/div[3]/ul/li[2]/h3/a/text()')
        if(name):
            name1 = name[0]
        else:
            name1 = 'none'
        info = [apartment, total_price, name1]
        csv_info(info)
        print(apartment, total_price, name)
def csv_info(content):
    with open('info.csv', 'a', encoding='utf-8', newline='')as file:
        write = csv.writer(file)
        write.writerow(content)
def main():
    for x in range(1, 3):
        url = 'https://bj.5i5j.com/ershoufang/n%s' % x
        parse(url)



if __name__ == '__main__':
    main()