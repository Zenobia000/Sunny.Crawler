from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver as uc
import json
import pandas as pd

urlindex = input('請輸入網址編號 0~6:')

my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文
my_options.add_argument('blink-settings=imagesEnabled=false')  # 不載入圖
my_options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])  # 沒有異常log
my_options.add_extension(
    'C:\Selenium\風傳媒\gighmmpiobklfepjocnamgkkbiglidom-5.3.2-Crx4Chrome.com.crx')
driver = webdriver.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install()))

# sunny 0
# noah 1
# mm 2
# xiong 3
# yen 4
# yuan 5
# kevin 6

links = ['https://www.storm.mg/business',
         'https://www.storm.mg/category/249514',
         'https://www.storm.mg/technology',
         'https://www.storm.mg/category/249516',
         'https://www.storm.mg/category/173479',
         'https://www.storm.mg/category/186729',
         'https://www.storm.mg/category/249515']

url = links[int(urlindex)]
driver.get(url)

alinks = []
results = []


def input_links():
    links = driver.find_elements(
        By.CSS_SELECTOR, '#category_content > div.section_block.no_bottom_line > div > div > div.card_inner_wrapper > a.card_link.link_title')
    for link in links:
        alinks.append(link.get_attribute('href'))


def craw2():
    try:
        in_text = driver.find_element(
            By.CSS_SELECTOR, '#CMS_wrapper')
        in_text = in_text.get_attribute('innerText')
        text = in_text.replace('\n', ' ')
    except:
        text = 'None'
    result = {
        '文章內容': text
    }
    results.append(result)


if __name__ == '__main__':

    while True:

        input_links()
        button = driver.find_element(
            By.CSS_SELECTOR, '#next')

        if button.get_attribute('class') == 'pagination_content pagination_func disabled':
            break
        else:
            button.click()

    for j in range(len(alinks)):
        print(j, alinks[j])
        driver.get(alinks[j])
        sleep(3)
        craw2()

    with open('storm' + urlindex + '.txt', 'w', encoding='utf-8') as fp:
        for r in results:
            fp.write("%s\n" % r)
        print('storm' + urlindex + '.txt 已存檔')

    driver.quit()
