from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

username = "username"
password = "password"

options = webdriver.ChromeOptions()
options.add_argument("--window-position=0,0")
options.add_argument("--window-size=1280,960")
#options.add_argument('--proxy-server=https://101.27.22.17:61234')
driver = webdriver.Chrome(chrome_options=options)
#driver.maximize_window()
#driver.delete_all_cookies()
driver.get("https://login.taobao.com/member/login.jhtml")
driver.implicitly_wait(5)

def Login_by_qcode():
    qcode = driver.find_element_by_id("J_Static2Quick")

    action = ActionChains(driver)
    action.reset_actions()
    action.move_to_element(qcode)
    action.move_by_offset(20, -20).click()
    action.perform()

    while True:
        url = driver.current_url

        if not url.startswith("https://login.taobao.com"):
            cookies = driver.get_cookies()
            res = ""
            for cookie in cookies:
                res += cookie.get('name')+'='+cookie.get('value')+';'

            res = res[:-1]
            print (res)
            break

        try:
            refresh = driver.find_element_by_class_name("J_QRCodeRefresh")
            refresh.click()
        except:
            pass

        time.sleep(6)

    driver.quit()

if __name__ == '__main__':
    Login_by_qcode()

