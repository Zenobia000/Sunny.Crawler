from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import undetected_chromedriver as uc

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文
# my_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# my_options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver = uc.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install())
    # cookie=
)


def go():
    driver.get('https://www.mobile01.com/topiclist.php?f=651')


atltes = []
alinks = []
results = []


def insertlink():
    links = driver.find_elements(
        By.CSS_SELECTOR, 'div.c-listTableTd__title >a ')
    links[0].get_attribute('href')

    # 加入所有連結到list
    for i in range(len(links)):
        links = driver.find_elements(
            By.CSS_SELECTOR, 'div.c-listTableTd__title >a ')
        a = links[i].get_attribute('href')
        alinks.append(a)


# 前往link網址
def golink():
    for i in range(0, len(alinks)):
        sleep(0.5)
        driver.get(alinks[i])
        WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located(
            (By.CSS_SELECTOR, 'div.l-docking__title > div > div > h1')))
        innerText()
# 印出評論 排除內文


def innerText():
    for i in range(len(com)):

        title = driver.find_element(
            By.CSS_SELECTOR, ('div > div.l-docking__title'))
        com = driver.find_elements(
            By.CSS_SELECTOR, 'article.u-gapBottom--max.c-articleLimit')
        comment = com[i].text
        result = {
            '連結': title,
            '評論': comment.replace('\n', '')
        }
        results.append(result)


if __name__ == '__main__':
    go()
    insertlink()
    golink()  # +innerText()
