# -*- coding: utf-8 -*-
import scrapy
import json
from so_image.items import SoImageItem

class ImagesSpider(scrapy.Spider):

    name = 'images'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1']
    def parse(self, response):
        item = SoImageItem()
        infos = json.loads(response.body)
        item['count'] = infos['count']
        for url in infos['list']:
            item['title'] = url['group_title']
            item['url'] = url['qhimg_url']
            yield item



