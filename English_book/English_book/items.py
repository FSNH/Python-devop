# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EnglishBookItem(scrapy.Item):
    book_title = scrapy.Field()
    kind = scrapy.Field()
    pub = scrapy.Field()
    content = scrapy.Field()