from scrapy import cmdline

# cmdline.execute(["scrapy", 'crawl', 'country_or_district', '-s', 'LOG_LEVEL=DEBUG'])
cmdline.execute('scrapy crawl country_or_district'.split(' '))