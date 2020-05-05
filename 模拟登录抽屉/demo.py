import requests
import time
from lxml import etree
#用xpath爬取抽屉网
#翻页爬取抽屉网的段子
#爬取内容为段子的作者、点赞数、评论数、内容

#创建保存函数
def save_info(contents):
    with open('./段子.doc', 'a', encoding='utf-8', newline='\n')as f:
        f.write(contents+'\n')

# 创建函数获取页面
def get_page(url):
    headers = {
                'Origin': 'https://dig.chouti.com',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                 AppleWebKit/537.36 (KHTML, like Gecko) \
                 Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'
                }
    try:
        resp = requests.get(url, headers=headers)
        page_source = resp.text
        return page_source
    except:
        print("出错了")

# 创建解析函数
def paser_page(url):
    html = get_page(url)
    selector1 = etree.HTML(html)
    items = selector1.xpath('//*[@class="news-content"]')
    for item in items:
        content = item.xpath('./div[1]/a/text()')[0].strip()
        name = item.xpath('./div[2]/a[4]/b/text()')[0].strip()
        zan_number = item.xpath('./div[2]/a[1]/b/text()')[0].strip()
        comments = item.xpath('./div[2]/a[2]/b/text()')[0].strip()
        # 创建列表
        info = [name,  zan_number, comments, content]
        # 创建字典
        info_dic = {
            "作者": name,
            "点赞数": zan_number,
            "评论数": comments,
            "内容": content
        }
        #将列表转化为str进行保存
        save_info('\t'.join(info))
        # 编辑器中以字典形式显示
        print(info_dic)

# 创建主函数
def main():
    info_title = ["作者", "点赞数", "评论数", "内容"]
    save_info('\t'.join(info_title))
    urls = ['https://dig.chouti.com/r/scoff/hot/%s' % x for x in range(1, 4)]
    for i, url in enumerate(urls):
        paser_page(url)
        print(i)
        time.sleep(2)

# 调用函数并运行
if __name__ == '__main__':
    main()
