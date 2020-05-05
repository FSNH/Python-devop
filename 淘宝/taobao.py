
from lxml import etree
from selenium import webdriver
import time
import csv

#selenium+xpath爬取整站任意商品
browser = webdriver.Firefox()
global k
 
def get_info(url,count):
    count+=1
    browser.get(url)
    html = browser.page_source
    selector = etree.HTML(html)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        goods_name = info.xpath('.//a/img/@alt')[0]
        price = info.xpath('.//div[@class="price g_price g_price-highlight"]//strong/text()')[0]
        shop_name = info.xpath('.//div[@class="shop"]/a//span[2]/text()')[0]
        location = info.xpath('.//div[@class="location"]/text()')[0]
        sell_number = info.xpath('.//div[@class="deal-cnt"]/text()')[0]
        good_href = info.xpath('.//a/@href')[0]
        goods_info = [goods_name, price, shop_name, location, sell_number, good_href]
        save(goods_info)
        print(
                goods_name+'\n',
                price+'\n',
                shop_name+'\n',
                location+'\n',
                sell_number+'\n',
                good_href+'\n',
            )

    
    if count<=k:
        get_page(url,count)
    else:
        pass

def get_page(url,count):
    browser.get(url)
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()
    time.sleep(5)
    get_info(browser.current_url,count)

def save(iten):
    with open('ptoducts.csv','a+',encoding='utf-8',newline='')as f:
        writer = csv.writer(f)
        writer.writerow(iten)

if __name__ == '__main__':
    save(['名称', '价格/元', '店铺名', '地区', '销量'])
    url = 'https://www.taobao.com/'
    browser.get(url)
    browser.implicitly_wait(5)
    browser.find_element_by_id('q').clear()
    time.sleep(10)
    namekeys = str(input('请输入要搜索的商品：'))
    k = int(input('请输入爬取页数：')) 
    browser.find_element_by_id('q').send_keys(namekeys)
    browser.find_element_by_class_name('btn-search').click()
    time.sleep(20)
    get_info(browser.current_url,1)