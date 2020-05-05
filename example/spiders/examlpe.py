# -*- coding: utf-8 -*-
import scrapy
# scrapy 爬取盗墓笔记
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class ExamlpeSpider(CrawlSpider):
    name = 'examlpe'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://daomubiji.com']

    rules = (

        Rule(LinkExtractor(allow=('qi-xing-lu-wang-',)), callback='parse_item'),
    )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//h1[@class="article-title"]/text()').get()
        item['name'] = response.xpath('//span[@class="item item-1"]/text()').get()
        item['description'] = response.xpath('//article[@class="article-content"]//p/text()').get()
        return item
