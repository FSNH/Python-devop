import requests
from lxml import etree

# 爬取天堂图片网图片

class Picture(object):

    def __init__(self, url):

        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'
                        }
        self.url = url

    def get_html(self):
        '''
        获取页面图片链接
        :return:
        '''
        resp = requests.get(url=self.url, headers=self.headers)
        return resp.text


    def paser_html(self):
        '''
        解析出详情页url
        :return:
        '''
        item = etree.HTML(self.get_html())
        items = item.xpath('/html/body/div[3]/div[2]/ul/li')
        for detail_url in items:
            #获取详情页url
            detail_urls = detail_url.xpath('./div/a/@href')[0]
            #详情页url具体链接
            detail_urls = 'https://www.ivsky.com' + detail_urls

            '''
            获取详情页的所有图片链接
            :return:
            '''
            resp = requests.get(url=detail_urls, headers=self.headers)
            item = etree.HTML(resp.text)
            try:
                items = item.xpath('/html/body/div[3]/div[4]/ul/li')
            except:
                print('error')
            finally:
                    for pic_url in items:
                    # print(pic_url)
                    pic = pic_url.xpath('.//a/img/@src')[0]
                    if 'http:'not in pic:
                        pic = 'http:' + pic
                    else:
                        pic=pic
                    patter = pic.split('/')[-1]
                    print(pic)
                    url_set = set()
                    if pic not in url_set:
                        resp = requests.get(pic, headers=self.headers)
                        url_set.add(pic)
                        self.save_pic(patter, resp.content)

    def save_pic(self, filename, content):
        with open('D:\爬虫\图片\JPG\\'+filename, 'wb')as f:
            f.write(content)

if __name__ == '__main__':
    for x in range(1, 12):
        url = 'https://www.ivsky.com/tupian/ziranfengguang/index_{}.html'.format(x)
        pic = Picture(url)
        pic.paser_html()