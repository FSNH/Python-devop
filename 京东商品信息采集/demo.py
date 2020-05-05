from selenium import webdriver
import requests
from multiprocessing.pool import Pool
from lxml import etree
#爬取京东商城
browser = webdriver.PhantomJS()

def save(content):
    with open('television.doc', 'a', encoding='gbk')as f:
        f.writelines(content)

def paser_index(url):
    browser.get(url)
    selector = etree.HTML(browser.page_source)
    items = selector.xpath('//li[@class="gl-item"]')
    for item in items:
        price = '商品价格/元：'+item.xpath('.//strong[@class="J_price"]//i/text()')[0]
        title = str(item.xpath('./div/div[3]/a/em/text()')[0]).strip()
        comment = '评论数:'+item.xpath('.//div[@class="p-commit p-commit-n"]//a/text()')[0]
        price_buy = item.xpath('.//span[@class="buy-score"]/em/text()')
        if price_buy:
            price_buy = '商品性价比：'+price_buy[0]
        else:
            price_buy = 'none'
        shop = item.xpath('.//div[@class="p-shop"]/span/a/text()')[0]
        href = 'https:' + item.xpath('.//div[@class="p-img"]/a/@href')[0]
        print(price + '\n', title + '\n', comment + '\n', price_buy + '\n', shop + '\n')
        info = [price, title, comment, price_buy, shop]
        save('\n'.join(info))
        content = get_detail(href)
        detail_paser(content)


def get_detail(url):
    #获取商品详情页
    response = requests.get(url)
    return response.text

def detail_paser(content):
    #解析商品详情页
    details = etree.HTML(content)
    lis = details.xpath('//ul[@class="parameter2 p-parameter-list"]//li')
    for li in lis:
        prodrcts = li.xpath('.//text()')[0]
        save(prodrcts+'\n')
        print(prodrcts)
if __name__ == '__main__':
    #多线程爬取
    print('开始。。。。。。。。。。。。。。。。。。。。。。。。')
    urls = ['https://list.jd.com/list.html?cat=737,794,798&page={}'.format(str(i)) for i in range(1, 3)]
    pool = Pool()
    result = pool.map(paser_index, urls)
    pool.close()
    pool.join()
