import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

s = Service(executable_path='/usr/local/bin/chromedriver')
driver = Chrome(service=s,options=chrome_options)

driver.get('https://bot.sannysoft.com/')
time.sleep(5)
driver.save_screenshot('screenshot.png')
driver.close()
print('运行完成')


