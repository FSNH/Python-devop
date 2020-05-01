# -*- coding: utf-8 -*-
import scrapy
from Scra_Picture.items import ScraPictureItem


class PicSpider(scrapy.Spider):
    name = 'PIC'
    # start_urls = ['https://www.ivsky.com/tupian/ziranfengguang/index_1.html']

    def start_requests(self):
        for i in range(1, 20):
            page_url = 'https://www.ivsky.com/tupian/ziranfengguang/index_{}.html'.format(i)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        items = response.xpath('/html/body/div[3]/div[2]/ul/li')
        # print(items)
        for item in items:
            base_url = 'https://www.ivsky.com'
            html_url = item.xpath('./div/a/@href').extract_first()
            # print(base_url + html_url)
            url = base_url + html_url
            yield scrapy.Request(url=url, callback=self.parse_item)

    def parse_item(self, response):
        selector = response.xpath('/html/body/div[3]/div[4]/ul/li')
        # print(selector)
        for li_item in selector:
            item = ScraPictureItem()
            li_url = li_item.xpath('./div/a/img/@src').extract_first()
            # print(li_url)
            if 'http:' not in li_url:
                pic_url = 'http:' + li_url
            else:
                pic_url = li_url
            # print(pic_url)
            item['pic_url'] = pic_url
            yield item

