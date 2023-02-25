from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json


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
driver = webdriver.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install())
    # cookie=
)
driver.get('https://www.ptt.cc/bbs/Tech_Job/index.html')
results = []
alinks = []
atitle = []
plink_ptitle = []
folderPath = 'C:/Users/student/python_web_scraping-master/ptt'


def links():
    links = driver.find_elements(By.CSS_SELECTOR, '  div.title > a')
    for link in links:
        plink = link.get_attribute('href')
        ptitle = link.get_attribute('innerText')
        rr = {
            ptitle: plink
        }
        plink_ptitle.append(rr)
        alinks.append(plink)
        atitle.append(ptitle)


def reply(i):
    driver.get(alinks[i])
    innerTexts = driver.find_elements(By.CSS_SELECTOR, 'div.push')

    for innerText in innerTexts:
        comment = innerText.get_attribute('innerText')
        c = comment.split('\n')
        fc = c[0].split(':')
        fc[-1]

        cc = comment.split(' ')
        GB = cc[0]
        try:
            User = cc[1]
        except:
            User == None

        innertext = fc[-1]

        result = {
            atitle[i]: alinks[i],
            '留言好壞': GB,
            '留言帳號': User,
            '留言內文': innertext

        }

        results.append(result)


def savejson():
    with open('t.json', 'w', encoding='utf-8') as f:
        f.write(json.dump(results, f, indent=4,
                          sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    links()
    start = int(input('起始頁數(請輸入阿拉伯數字)：'))
    end = int(input('結束頁數(請輸入阿拉伯數字)：'))
    for i in range(start, end):
        reply(i)
    savejson()

print('存好了')
driver.quit()
