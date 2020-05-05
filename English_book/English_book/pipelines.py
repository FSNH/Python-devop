# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class EnglishBookPipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='localhost', user='root', password='294419', db='magzines',
                                       port=3306)  # db要和建的数据库名称对应上
        self.cursor = self.connect.cursor()
        self.insert_detail = 'insert into f_tushu_info(kind_id,book_title,pub,brief,content)' \
                             'VALUES (%s,%s,%s,%s,%s)'

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        # 表的名字要和建的表名对应
        self.cursor.execute(
            self.insert_detail,
            (item['kind'], item['book_title'], item['pub'], item['content'][:100],item['content']))
        self.connect.commit()
        return item

        # 关闭数据库

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

