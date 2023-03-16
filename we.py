from time import sleep
from selenium import webdriver
driver=webdriver.Firefox()

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('path/to/firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)


driver.get("https://www.bilibili.com/")
sleep(3)
driver.quit()