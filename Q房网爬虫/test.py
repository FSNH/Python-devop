import requests

url = 'https://shenzhen.qfang.com/sale/f1'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/70.0.3538.110 Safari/537.36',
               'upgrade-insecure-requests': '1',
               'cookie':'qchatid=c389e1db-6e8d-4c5e-b221-09117b8251e4; _ga=GA1.3.615197497.1547710276; CITY_NAME=SHENZHEN; SALEROOMREADRECORDCOOKIE=100451421%23100442428%23100460607; looks=SALE%2C100442428%2C55538%7CSALE%2C100460607%2C56752; cookieId=da1e6738-c45b-4de6-97e1-8c525fb9cfef; sec_tc=AQAAAIF2KnyWFgoA32uMVXQEbAhfgcmz; acw_tc=df6fef1b15606729096611896e68cec0eadb7ce0b82f2162766542d1de; sid=c15a446d-961a-44e5-9cac-3616f5fa0987; language=SIMPLIFIED; JSESSIONID=aaakIkClOr3Fx66yRwFTw; acw_sc__v2=5d05fa8d3b852a2db1045de5b468191b4a1deffc; WINDOW_DEVICE_PIXEL_RATIO=1.100000023841858; _gid=GA1.3.534628977.1560672931; _dc_gtm_UA-47416713-1=1; Hm_lvt_de678bd934b065f76f05705d4e7b662c=1560672931; Hm_lpvt_de678bd934b065f76f05705d4e7b662c=1560672931'}
response = requests.get(url=url,headers=headers)
print(response.text)
