import time
from time import sleep
# from selenium import webdriver
# driver=webdriver.Firefox()
#
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#
# binary = FirefoxBinary('path/to/firefox.exe')
# driver = webdriver.Firefox(firefox_binary=binary)
#
#
# driver.get("https://www.bilibili.com/")
# sleep(3)
# driver.quit()

def wait_time(sleep_time):
    a = 0
    for i in range(0,sleep_time+1):
        time.sleep(i-a)
        a=i
        print(f"已经休息了{i}s啦")
        # 翻译插件： ctrl+shift+y翻译    ctrl+shift+x中英文替换
if __name__ == '__main__':
    wait_time(4)