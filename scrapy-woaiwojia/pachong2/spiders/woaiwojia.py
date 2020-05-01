# -*- coding: utf-8 -*-
import scrapy
from pachong2.items import Pachong2Item

class WoaiwojiaSpider(scrapy.Spider):
    name = 'woaiwojia'
    allowed_domains = ['bj.5i5j.com']
    start_urls = ['https://bj.5i5j.com/ershoufang/n%s/' % x for x in range(1, 11)]

    def parse(self, response):
        # 获取房源列表信息
        house_list = response.xpath('//ul[@class="pList"]/li')
        for house in house_list:
            item = Pachong2Item()
            item['apartment'] = house.xpath('div[2]/h3/a/text()').extract()
            item['total_price'] = house.xpath('div[2]/div[1]/div/p[1]/strong/text()').extract()

            yield item






