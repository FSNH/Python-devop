import requests
from lxml import etree
import csv
import time
#爬取链家房源经纪人信息
#有xpath解析爬取：人名，负责区域
#定义csv保存函数
def save_csv_writer(item):
    with open('lianjia_jingjiren.csv', 'a+', encoding='utf-8', newline='')as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(item)
#定义链家经纪人主函数
def lianjia_spider(list_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64)\
                AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
    try:
        response = requests.get(list_url, headers=headers)
    except:
        print('出错了')
    time.sleep(5)
    content = response.text
    #解析页面
    html = etree.HTML(content)
    #爬取每一位经纪人的信息整段代码
    agent_list = html.xpath('//li[@class="pictext flexbox box_center_v lazyload_ulog"]')
    for agent in agent_list:
        # name//*[@id="page-0---6a004ab5-9bcd-4bac-4800-99870c90b5e3"]/section[1]/div[2]/div/div[3]/ul/li[1]/div/div[2]/div[1]/span[1]/a[1]
        # region//*[@id="page-0---6a004ab5-9bcd-4bac-4800-99870c90b5e3"]/section[1]/div[2]/div/div[3]/ul/li[1]/div/div[2]/div[2]/span[3]
        agent_name = agent.xpath('div/div[2]/div[1]/span[1]/a[1]/text()')[0]
        agent_region = agent.xpath('div/div[2]/div[2]/span[3]/text()')[0]
        info = [agent_name, agent_region]
        print('正在爬取', agent_name, agent_region)
        save_csv_writer(info)       #调用保存函数并保存数据为csv格式
# 创建主函数
def main():
    for i in range(100):
        # 构造url格式
        url = ('https://m.lianjia.com/ha/jingjiren/?page_size=15&_t=1&offset='+str(i*15))
        lianjia_spider(url)
        print('正在爬取', i)
#调用函数
if __name__ =="__main__":
    main()