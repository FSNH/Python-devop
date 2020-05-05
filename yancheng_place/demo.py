import requests
from lxml import etree
from multiprocessing.pool import Pool
headers = {
    'Referer': 'https://yancheng.cncn.com/jingdian/dazonghu/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400'
}
def save(content):#存储文件
    with open('盐城景区.doc', 'a')as f:
        f.write(content+'\n')

def get_detail(href):#获取详情页
    response = requests.get(href, headers=headers)
    return response.text

def paser_pages(resp):#解析详情页
    infos = []
    info = etree.HTML(resp)
    title = info.xpath('//h1/text()')[0]#获取标题
    infos.append(title)
    #print(title)
    dls = info.xpath('//div[@class="type"]//dl')#获取详情页信息
    for dl in dls:
        detail = dl.xpath('.//text()')
        detail = str(''.join(detail)).replace('\xa0', '').strip()
        infos.append(detail)
        #print(detail)
    save('\n'.join(infos))

def get_pages(url):#首页
    response = requests.get(url, headers=headers)
    # print(response.text)
    selector = etree.HTML(response.text)
    items = selector.xpath('//div[@class="city_spots_list"]/ul//li')
    for item in items:
        #获取详情页url
        href = item.xpath('./a/@href')[0]
        #print(href)
        res = get_detail(href)
        paser_pages(res)

if __name__ == '__main__':
    #多线程爬取
    page_href = ['https://yancheng.cncn.com/jingdian/1-{}-0-0.html'.format(str(i)) for i in range(1, 6)]
    pool = Pool()
    result = pool.map(get_pages, page_href)
    pool.close()
    pool.join()


