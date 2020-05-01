# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ScraPicturePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
            image_url = item['pic_url']
            yield scrapy.Request(image_url)

    # def item_completed(self, results, item, info):
    #     # 修改名称
    #     image_paths = [x['path'] for ok, x in results if ok]
    #     return item