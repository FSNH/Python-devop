# -*- coding: utf-8 -*-

# Scrapy settings for pachong2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pachong2'

SPIDER_MODULES = ['pachong2.spiders']
NEWSPIDER_MODULE = 'pachong2.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 2
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/'
                '537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/'
                '537.36 Core/1.63.6788.400 QQBrowser/10.3.2727.400',
  'Referer': 'https://bj.5i5j.com/ershoufang/n1/?wscckey=3af98ca61d541c63_1550824465',
  'Cookie': 'yfx_c_g_u_id_10000001=_ck19022116084813839206365574151; _ga=GA1.2.172982220.1550736528; _gid=GA1.2.262368544.1550736528; _Jo0OQK=1EF60A430707C39DC66841396A856BB9F1CDAFCCCBE5DD3EF55A648ADA5CBA77AEE43F896CA59E44D089FA0454846BD97D281B9CBA503EBFB1655D4D98FAB359BC6C57212F12283777C840763663251ADEB840763663251ADEB55B9636F868E3ABE2350674422DE2517GJ1Z1Pg==; PHPSESSID=1sa6iff0gbok9mts9t6mgt4l2e; domain=bj; yfx_f_l_v_t_10000001=f_t_1550736528365__r_t_1550736528365__v_t_1550759656352__r_c_0; Hm_lvt_94ed3d23572054a86ed341d64b267ec6=1550736529,1550759657; ershoufang_BROWSES=41857749%2C42331571; _gat=1; Hm_lpvt_94ed3d23572054a86ed341d64b267ec6=1550760880'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pachong2.middlewares.Pachong2SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pachong2.middlewares.Pachong2DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pachong2.pipelines.Pachong2Pipeline': 300,
   # 'scrapy.pipelines.images.ImagesPipeline': 1
}
# IMAGES_STORE = 'D:\\pics'
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
