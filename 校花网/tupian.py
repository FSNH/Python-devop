import requests
import re
#正则表达式爬取校花网
# 网址 url = 'http://www.xiaohuar.com'
#分页爬取大学校花图片共16页1094张美图

def get_page(url):
    response = requests.get(url) #获取HTML代码
    html = response.text
    return html

# 图片地址分析
# d/file/20160902/17009a5a0858499cd1dc89fd467b7a02.jpg"
# d/file/20160114/4b3371af750b8eda82de4dcc0a1d06dd.jpg"
# d/file/20160107/776911c54ae5ed4f0fe1c3652ce755da.jpg"
def paser_page(url):
    html = get_page(url)
    # 正则表达式从所打印出的HTML代码中筛选出图图片相同的数据
    img_urls = re.findall(r'/d/file/\d+/\w+\.jpg', html)
    # 运用for 循环将获取到的每个图片地址传给img_url
    for img_url in img_urls:
        # 再次进行网络请求 将获取的图片地址信息与主域名 结合起来 传给一个新的变量
        img_response = requests.get('http://www.xiaohuar.com' + img_url)
        print(img_url)  # 将所得的图片的地址打印出来
        # 将所得信息以二进制的形式存取赋值给一个变量img_data
        img_data = img_response.content
        # 下面开始分割图片的地址并取出右边第一个 并赋值变量名
        tupian = img_url.split('/')[-1]
        #保存图片
        save_pic(img_data, tupian)

def save_pic(content,address):
# 对获取到的图片进行本地保存
    with open('./tupian/' + address, 'wb') as f:
        f.write(content)

#创建主函数
def main():
    for x in range(1, 17):
        url = 'http://www.xiaohuar.com/list-1-%s.html' % x
        paser_page(url)
#调用并运行函数
if __name__ == '__main__':
    main()







