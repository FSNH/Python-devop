# -*- coding: utf-8 -*-
import scrapy
from RenSheng.items import RenshengItem


class RenshengSpider(scrapy.Spider):
    name = 'rensheng'
    allowed_domains = ['rensheng5.com']
    start_urls = ['http://www.rensheng5.com/sitemap.html']

    def parse(self, response):
        divs = response.xpath('//div[@class="linkbox"]')[3:6]
        for div in divs:
            book_name = div.xpath("./h3/a/text()").extract_first()
            lis = div.xpath('./ul[@class = "f6"]//li')
            for li in lis:
                kind = li.xpath('./a/text()').extract_first()
                kind_url = li.xpath('./a/@href').extract_first()
                info = {
                    'title': book_name,
                    'kind': kind,
                }
                # print(book_name, kind, kind_url)
                yield scrapy.Request(url=kind_url, meta=info, callback=self.parse_content)

    def parse_content(self, response):
        # print(response.text)
        book_name = response.meta['title']
        kind = response.meta['kind']
        lis = response.xpath('//ul[@class="p7"]//li')
        for li in lis:
            book_title = li.xpath('./a/text()').extract_first()
            book_url = li.xpath('./a/@href').extract_first()
            pub = li.xpath('.//span/text()').extract_first().strip()
            # print('*'*30)
            # print(book_name,kind,book_title, book_url, pub)
            info = {
                'title': book_name,
                'kind': kind,
                'book_title': book_title,
                'pub': pub,
            }

            yield scrapy.Request(url=book_url, meta=info, callback=self.parse_detail)
        # next_url = (response.xpath('//div[@class="pages"]/ul//li')[-3]).xpath('./a/@href').extract_first()
        # if next_url:
        #     print(response.urljoin(next_url))
        #     yield scrapy.Request(url=response.urljoin(next_url), meta=info, callback=self.parse_content)

    def parse_detail(self, response):
        items = RenshengItem()
        items['book_name'] = response.meta['title']
        items['kind'] = response.meta['kind']
        items['book_title'] = response.meta['book_title']
        items['pub'] = response.meta['pub']
        items['author'] = '未详'
        content = response.xpath('//div[@class="artbody"]/p//text()').extract()
        items['content'] = ''.join(content).strip().replace('\u3000\u3000\\', ' ')
        # print(book_name,kind,book_title,pub,author,content)
        # print('*'*50)
        yield items