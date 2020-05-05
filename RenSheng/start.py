from scrapy import cmdline

cmdline.execute(['scrapy', 'crawl', 'rensheng'])
# scrapy crawl spider_name -s JOBDIR=crawls/rensheng  断点续爬

# cmdline.execute('scrapy crawl rensheng -s JOBDIR=crawls/rensheng'.split())