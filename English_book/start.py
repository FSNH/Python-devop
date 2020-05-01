from scrapy import cmdline
# cmdline.execute(['scrapy', 'crawl', 'english_book'])
# 断点续爬
cmdline.execute('scrapy crawl english_book -s JOBDIR=crawls/english'.split())