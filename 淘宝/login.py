from selenium import webdriver
from lxml import etree
import time
from selenium.webdriver import ActionChains

browser = webdriver.Firefox()
url = 'https://www.taobao.com/'
browser.get(url)
browser.find_element_by_link_text('亲，请登录').click()
time.sleep(1)
browser.find_element_by_link_text('密码登录').click()
#time.sleep(10)
#username = int(input('请输入账号：'))
#password = str(input('请输入密码：'))
browser.find_elements_by_id('TPL_username_1')[0].send_keys('账号')
browser.find_elements_by_id('TPL_password_1')[0].send_keys('密码')
element = browser.find_element_by_id('nc_1_n1z')
target = browser.find_element_by_xpath('//span[@id="nc_1_n1z"]')
ActionChains(browser).drag_and_drop(element,target).perform()
time.sleep(3)
browser.find_elements_by_id('J_SubmitStatic')[0].click()

