from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver as uc
import json
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from opencc import OpenCC


my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文
# my_options.add_argument('blink-settings=imagesEnabled=false')  # 不載入圖
my_options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])  # 沒有異常log
driver = webdriver.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install())
)

results = []
alinks = []

driver.get('https://medium-rare.pages.dev/')
sleep(5)
key = input('請輸入關鍵字:')


def input_search(key):
    search = driver.find_element(
        By.CSS_SELECTOR, '#__next > div > div > div > div:nth-child(1) > div')
    search.click()
    sleep(1)
    input_txt = driver.find_element(
        By.CSS_SELECTOR, '#chakra-modal--body-\:Rl5t6\: > div.css-1wvh9i1 > div > input')

    input_txt.send_keys(key)
    join = driver.find_element(
        By.CSS_SELECTOR, '#chakra-modal--body-\:Rl5t6\: > div.css-1wvh9i1 > div > div')
    join.click()
    search2 = driver.find_element(
        By.CSS_SELECTOR, '#chakra-modal--body-\:Rl5t6\: > div.css-yvxjvp > button')
    search2.click()
    sleep(3)
# WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located(
#         (By.CSS_SELECTOR, "#__next > div > div.Content_content__2kcTh.css-0 > div > div:nth-child(1) > a > div > div > div > div.Card_name__9AeZO.css-0"))
# )


def next():
    for i in range(30):
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#__next > div > div.Content_content__2kcTh.css-0 > div > div.Home_state__p7_H8.css-0 > button"))
            )
            more = driver.find_element(
                By.CSS_SELECTOR, '#__next > div > div.Content_content__2kcTh.css-0 > div > div.Home_state__p7_H8.css-0 > button')
            more.click()
        except:
            break


def input_links():
    links = driver.find_elements(
        By.CSS_SELECTOR, '#__next > div > div.Content_content__2kcTh.css-0 > div > div > a')
    # for i in links:
    #     print(i.get_attribute('href'))
    for link in links:
        alinks.append(link.get_attribute('href'))


def craw2():
    cc = OpenCC('s2tw')
    try:
        in_text = driver.find_element(By.CSS_SELECTOR, 'div > section')
        in_text = in_text.get_attribute('innerText')
        text = in_text.replace('\n', '')
        text = cc.convert(text)
    except:
        text = 'None'
    result = {
        '文章內容': text
    }
    results.append(result)


if __name__ == '__main__':
    input_search(key)
    next()
    input_links()
    for i in range(len(alinks)):
        print(alinks[i])
        print(i)
        driver.get(alinks[i])
        sleep(5)
        craw2()

with open(f'{key}'+'.json', "w", encoding='utf-8') as file:
    file.write(json.dumps(
        results, ensure_ascii=False, indent=4))

df = pd.read_json(f'{key}'+'.json')
df.to_csv(f'{key}'+'.txt',
          encoding="utf_8_sig", sep='\t', index=False)
