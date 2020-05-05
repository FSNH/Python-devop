from selenium import webdriver
import time
from lxml import etree
import csv
# options = webdriver.FirefoxOptions()
# options.set_headless()
driver = webdriver.Firefox()#火狐浏览器模拟请求
#driver.maximize_window()

def get_info(url, page):#页面请求解析函数
    page = page+1#爬取页数加一
    driver.get(url)
    driver.implicitly_wait(10)#隐式等待10秒
    selector = etree.HTML(driver.page_source)
    with open('hello.html', 'w+', encoding='utf-8')as f:
        f.write(driver.page_source)
    infos = selector.xpath('//div[@class="item J_MouserOnverReq  "]')
    for info in infos:
        goods = info.xpath('div/div/div/a/img/@alt')[0]#商品名称
        price = info.xpath('div[2]/div/div/strong/text()')[0]#价格
        sell = info.xpath('div[2]/div/div[@class="deal-cnt"]/text()')[0]#销量
        if sell:#判断销量是否为空
            sells = sell[0]
        else:
            sells = 0
           
        shop = info.xpath('div[2]/div[3]/div/a/span[2]/text()')[0]#店铺
        address = info.xpath('div[2]/div[3]/div[@class="location"]/text()')[0]#地址
        taobao_info = [goods, price, sell, shop, address] #创建商品列表
        save(taobao_info)#调用函数保存为csv

        #控制台输出
        print(goods+'\n',
              price+'\n',
              sell+'\n',
              shop+'\n',
              address+'\n'
              )
       
    if page <= 2:#判断当前页数，只爬取两页
        NextPage(url, page)#调用翻页函数
    else:
        pass

def save(iten):#保存函数
    with open('taobao.csv', 'a+',encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(iten)

def NextPage(url, page):#翻页函数
    driver.get(url)#请求当前页面url
    driver.implicitly_wait(5)#隐式等待5秒
    driver.find_element_by_xpath('//a[@trace="srp_bottom_pagedown"]').click()#点击翻页
    time.sleep(4)#等待4s加载
    get_info(driver.current_url, page)#再次传入下一页的当前url,调用函数并解析页面

if __name__ == '__main__':
    save(['名称','价格/元','销售量','店铺','地址'])#写入标题头
    url = 'https://taobao.com'#首页url
    driver.get(url)#请求首页面
    driver.implicitly_wait(10)
    driver.find_element_by_id('q').clear()#清空搜索框
    driver.find_element_by_id('q').send_keys('男士短袖')#输入搜索内容
    driver.find_element_by_class_name('btn-search').click()#点击搜索
    time.sleep(20)#延迟20s登录
    get_info(driver.current_url, 1)#获取页面的当前url传入解析函数，请求并解析页面
    
