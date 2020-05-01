# -*- coding: utf-8 -*-
import scrapy
from daomubiji.items import DaomubijiItem

class DaomubiSpider(scrapy.Spider):
    name = 'daomubi'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/dao-mu-bi-ji-2']
    def start_requests(self):
        for i in range(1, 9):
            yield scrapy.Request('http://www.daomubiji.com/dao-mu-bi-ji-{}'.format(i), callback=self.parse)
    def parse(self, response):
        item = DaomubijiItem()
        item['title'] = response.xpath('//h1[@class="focusbox-title"]/text()').extract_first()#提取小说名
        items = response.xpath('//article[@class="excerpt excerpt-c3"]')
        for href in items:
            detail_href = href.xpath('./a/@href').extract_first()#提取章节的正文链接
            yield scrapy.Request(url=detail_href, meta={'item': item}, callback=self.get_content)

    def get_content(self, response):
        item = response.meta['item']
        item['section'] = response.xpath('//h1[@class="article-title"]/text()').extract_first()#提取小说的章节名
        pages = response.xpath('//article[@class="article-content"]//p/text()').extract()#解析正文
        item['content'] = ''.join(pages)

        yield item



