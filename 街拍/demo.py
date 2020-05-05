import requests
from urllib.parse import urlencode
import json
headers = {
        'user-agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
        '537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/'
        '1.63.6788.400 QQBrowser/10.3.2727.400',
    }
def get_html(offset):

    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json()
    except requests.ConnectionError:
        return None

if __name__ == '__main__':
    offset = [i*20 for i in range(5)]
    for i in offset:
        json = get_html(i)
        url_list = []
        for item in json.get('data'):
            title = item.get('title')
            print(item.get('title'))
            if item.get('image_list'):
                for items in item.get('image_list'):
                    image = items.get('url')
                    #print(items.get('url'))
                    url_list.append(image)
                with open('file.txt', 'a+', encoding='utf-8')as f:
                    f.write("标题:"+title+'\n'+"url:"+image+'\n')

        for url_image in url_list:
            url1 = 'http:' + url_image+'.jpg'  #构造图片格式
            response = requests.get(url=url1, headers=headers, stream=True)
            images = response.content
            print(url1)

            tupian = url1.split('/')[-1]  #取地址的最后为图片名 保存
            with open('D:\爬虫\街拍\jpg'+'\\'+tupian, 'wb+')as f:
                f.write(images)
