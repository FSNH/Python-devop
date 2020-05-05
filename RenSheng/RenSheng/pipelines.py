# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import csv


class RenshengPipeline(object):
    # 保存文件为txt
    # def process_item(self, item, spider):
    #     with open(r'F:\books\\'+item['book_title']+'.txt', 'w+', encoding='utf-8')as f:
    #         f.write(item['book_title']+'\n'+item['book_name']+'\n'+item['kind']+'\n'+item['pub']+'\n'+item['content'])
    #     return item

    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='294419', db='magzines',
                                       port=3306)  # db要和建的数据库名称对应上
        self.cursor = self.connect.cursor()
        self.insert_cinfo = 'insert into c_tushu_info(kind_id, kind_branch,book_title,pub,author,brief,content)' \
                           'VALUES (%s,%s,%s,%s,%s,%s,%s)'


    def process_item(self, item, spider):
        # 往数据库里面写入数据
        # 表的名字要和建的表名对应
         self.cursor.execute(self.insert_cinfo, (item['book_name'],item['kind'],item['book_title'],
           item['pub'],item['author'],item['content'][:100],item['content']))
         self.connect.commit()
         return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()



