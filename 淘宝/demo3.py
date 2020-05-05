from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

# 你的账户密码
username = "账号"
password = "密码"

options = webdriver.ChromeOptions()
options.add_argument("--window-position=0,0")
options.add_argument("--window-size=1280,960")
# options.add_argument('--proxy-server=https://101.27.22.17:61234')
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Firefox()
# driver.maximize_window()
# driver.delete_all_cookies()
driver.get("https://login.taobao.com/member/login.jhtml")
driver.implicitly_wait(5)


def get_track_from_GM():
    file = open("human2.gms")
    # 这是滑块的位置，需要自己调整
    x, y = 1176, 413
    res = []
    while True:
        line = file.readline().strip()

        if not line:
            break

        data = line.split(" ")
        pos = (int(data[0]) - x, int(data[1]) - y, random.randint(0, 10) * 0.01)
        res.append(pos)

    file.close()
    return res


def Login_by_Account():
    while True:
        url = driver.current_url
        if not url.startswith("https://login.taobao.com"):
            break

        # 填写用户名和密码
        driver.find_element_by_id("TPL_username_1").clear()
        driver.find_element_by_id("TPL_password_1").clear()
        driver.find_element_by_id("TPL_username_1").send_keys(username)
        driver.find_element_by_id("TPL_password_1").send_keys(password)

        # 处理验证
        text = driver.find_element_by_id("nc_1__scale_text").text

        if not text or text == "验证通过":
            pass
        elif text.startswith("请按住滑块"):
            slider = driver.find_element_by_id("nc_1_n1z")
            print(slider.location)

            action = ActionChains(driver)
            action.click_and_hold(slider).perform()
            action.reset_actions()

            res = get_track_from_GM()

            for i in res:
                action.move_by_offset(i[0], i[1]).perform()
                action.reset_actions()
                time.sleep(i[2])

            action.release().perform()
            action.reset_actions()
        else:
            print("[ERROR]文本内容是:" + text)
            break

        # 点击登陆按钮
        driver.find_element_by_id("J_SubmitStatic").click()
        time.sleep(5)

    cookies = driver.get_cookies()

    res = ""
    for cookie in cookies:
        res += cookie.get('name') + '=' + cookie.get('value') + ';'

    res = res[:-1]
    print(res)

    driver.quit()


if __name__ == '__main__':
    Login_by_Account()

