import json
import requests

def get_json(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
        '537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/'
        '1.63.6788.400 QQBrowser/10.3.2727.400',
        'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'cookie': 'csrftoken=76f536d53d076ca5b23b0979e4d807b1; uuid="w:3677763bfabe4881b6516c4f263168c9"; tt_webid=6663339993463850504; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=169386e218635d-0e247a69a726be-335f4471-100200-169386e218738b; CNZZDATA1259612802=1507270659-1533471388-%7C1551428773; tt_webid=6663339993463850504; __tasessionId=lmd3lna4q1551432234432',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.get(url=url, headers=headers)
    html = response.json()
    return html

def parse_page(url):
    items = get_json(url)
    for item in items['data']:
        print(item['title'])

if __name__ == '__main__':
    url = 'https://www.toutiao.com/api/pc/feed/?category=gallery_old_picture&utm_source=toutiao&max_behot_time=0&as=A155BC6B08C3693&cp=5CB8531639A32E1&_signature=-SRCqgAApaZTCwIqSl4mSfkkQr'
    parse_page(url)

