# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.item import Item
import pymongo
class DaomubijiPipeline(object):

    def open_spider(self, spider):
        # 连接数据库
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        # 创建myspider数据库
        self.db = self.client.daomubiji
    def close_spider(self, spider):
        self.client.close()
    def process_item(self, item, spider):
        collection = self.db.spider.xiaoshuo
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item

