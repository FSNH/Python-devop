import requests


ses = requests.Session()
user = {

    'phone': '18851153282',
    'password': 'meng320882199501',
    'oneMonth': '1'
}
headers = {
    'Origin': 'https://dig.chouti.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
             AppleWebKit/537.36 (KHTML, like Gecko) \
             Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'}
r1 = ses.get('https://dig.chouti.com', headers=headers)
r1_cook = r1.cookies.get_dict()
print(r1_cook)
url1 = 'https://dig.chouti.com/login'
r2 = ses.post(url=url1, data=user, headers=headers)
r2_cook = r2.cookies.get_dict()
print(r2_cook)
url = 'https://dig.chouti.com/link/vote?linksId=21402116'
#data = {'linksId': '21402116'}
resp = ses.post(url, headers=headers)
html = resp.text
print(html)