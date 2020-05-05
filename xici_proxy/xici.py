import requests
import csv
import time
from lxml import etree
#https://www.xicidaili.com/nn/2


def get_page(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676."
              "400 QQBrowser/10.4.3469.400"}

    resp = requests.get(url=url, headers=header)
    html = resp.text
    time.sleep(2)
    return html


def parse_page(url):
    source = get_page(url)
    item = etree.HTML(source)
    trs = item.xpath('//*[@id="ip_list"]//tr')
   #print(item)
    for tr in trs[1:]:
        ip = tr.xpath('./td[2]/text()')[0]#获取ip
        port = tr.xpath('./td[3]/text()')[0]#获取端口
        ip = 'https://'+ip+':'+port #代理ip
        local = tr.xpath('./td[4]/a/text()')#获取地区
        if local:
            local = local[0]
        else:
            local = 'null'
        hidden = tr.xpath('./td[5]/text()')[0]#高匿
        kind = tr.xpath('./td[6]/text()')[0]#类型
        check_time = tr.xpath('./td[10]/text()')[0]#最后测试时间
        info = [ip, port, local, hidden, kind, check_time]
        save(info)


#保存为CSV文件
def save(info):
    with open('xici_prox1.csv', 'a',newline='')as f:
        write = csv.writer(f)
        write.writerow(info)



if __name__ == "__main__":
    print('开始爬取。。。')
    for i in range(1, 10):#翻页
        url = "https://www.xicidaili.com/nn/{}".format(i)
        parse_page(url)


