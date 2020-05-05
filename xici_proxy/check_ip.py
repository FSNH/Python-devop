import requests
import csv
import random
#读取IP地址
def reader_ip():
    proxy = {}
    with open('xici_prox1.csv','r')as f:
        reader=csv.reader(f)
        for row in reader:
            #print(row[0])
            yield row[0]
   #遍历ip  
for prox in reader_ip():
    proxy = {}
    proxy['https:']=prox#加入字典中
    print(proxy)
    #测试ip地址是否可用，可用返回200
    try:
        response = requests.get('http://www.baidu.com',proxies =proxy )
    except:
        print('出错了')
    state = response.status_code
    print(state)
    
    