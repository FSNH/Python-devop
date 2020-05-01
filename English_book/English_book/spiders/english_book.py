# -*- coding: utf-8 -*-
import scrapy
from English_book.items import EnglishBookItem



class EnglishBookSpider(scrapy.Spider):
    name = 'english_book'
    allowed_domains = ['http://m.enread.com/index.php']
    start_urls = ['http://m.enread.com/index.php?catid=7&mid=2']
    count = 1

    def parse(self, response):
        # print(response.text)
        items = response.xpath('//div[@class="cat_block"]/ul//li[@class="item_li"]')
        # print(items)
        for item in items:
            detail_url = item.xpath('./a/@href').extract_first()
            # print(response.urljoin(detail_url))
            yield scrapy.Request(url=response.urljoin(detail_url), callback=self.parse_content, dont_filter=True)
        if self.count < 2:
            next_url = response.xpath('//div[@id="pager"]/a/@href').extract_first()
            self.count = self.count+1
            # print(next_url)
            if next_url:
                yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse, dont_filter=True)

        else:
            next_url = response.xpath('//div[@id="pager"]//a[2]/@href').extract_first()
            if next_url:
                # print(next_url)
                yield scrapy.Request(url=response.urljoin(next_url), callback=self.parse, dont_filter=True)

    def parse_content(self, response):
        # print(response.text)
        item = EnglishBookItem()
        item['kind'] = response.xpath('//div[@id="nav"]//a[2]/text()').extract_first()
        item['book_title'] = response.xpath('//div[@class="arc_content"]/h1[@class="h1title"]/text()').extract_first()
        item['pub'] = response.xpath('//div[@class="info"]/text()').extract_first().split(' ')[0].replace('时间：', ' ').strip()
        item['content'] = ''.join(response.xpath('//div[@class="HJHuaCi"]//div/text()').extract()).strip()
        # print('*'*30)
        # print(kind,book_title,pub,content)
        yield item
