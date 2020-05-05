import requests
import re
import json
#正则表达式爬取猫眼电影
#网址http://maoyan.com
#爬取猫眼电影排行前一百名电影
#爬去排名、图片、片名、演员、时长、得分

#定义页面获取函数
def get_one_page(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko)Chrome/"
                     "63.0.3239.26 Safari/537.36 Core/1.63.5514.400 "
                     "QQBrowser/10.1.1660.400"
}
    response = requests.get(url, headers=headers )
    if response.status_code == 200:
        return response.text
    return None

#定义解析函数
def paser_one_page(html):
    # 正则表达式
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name"><a'
        +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?'
        +'integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip() + item[6].strip()
        }
#保存函数
def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8')as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')

#主函数
def main(offset):
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in paser_one_page(html):
        print(item)#编辑器中显示
        write_to_file(item)#保存到本地

#调用主函数并运行
if __name__ =='__main__':
    for i in range(10):
        main(i*10)