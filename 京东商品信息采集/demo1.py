from selenium import webdriver
browser = webdriver.PhantomJS()
browser.get('https://list.jd.com/list.html?cat=737,794,798')
print(browser.page_source)