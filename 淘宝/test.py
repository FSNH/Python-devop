from lxml import etree
import csv

def content():
    with open(r'D:\爬虫\淘宝\hello.html','r',encoding='utf-8')as f:
        return f.read()

def get_info():
    html = content()
    selector = etree.HTML(html)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        goods = info.xpath('div/div/div/a/img/@alt')[0]
        price = info.xpath('div[2]/div/div/strong/text()')[0]
        sell = info.xpath('div[2]/div/div[@class="deal-cnt"]/text()')[0]
        if sell:
            sells = sell[0]
        else:
            sells = 0

        shop = info.xpath('div[2]/div[3]/div/a/span[2]/text()')[0]
        address = info.xpath('div[2]/div[3]/div[@class="location"]/text()')[0]
        taobao_info = [goods, price, sell, shop, address]
        save(taobao_info)
        print(goods + '\n',
              price + '\n',
              sell + '\n',
              shop + '\n',
              address + '\n'
            )
def save(iten):
    with open('taobao.csv', 'a+',encoding='utf-8',newline='')as f:
        writer = csv.writer(f)
        writer.writerow(iten)
             
if __name__ == '__main__':
    save(['名称','价格/元','销售量','店铺','地址'])
    get_info()