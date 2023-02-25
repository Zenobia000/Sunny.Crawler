from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import pandas as pd

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文


driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)

#去薪資工作版
driver.get('https://www.ptt.cc/bbs/Salary/index.html')
#--------------------------------------------------------------------------
#調整要爬的page範圍
range1=int(input('請輸入起始頁數(阿拉伯數字)：'))
range2=int(input('請輸入結束頁數(亂打就重來)：'))
#你要放哪裡
folderPath = r'C:\Selenium\ptt_all'
#爬幾個連結的檔名 (應該可以改成一個input輸入)
filename_innerText = 'page_0_50'
#--------------------------------------------------------------------------

results = []
alinks = []
atitle = []
plink_ptitle = []


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


def reply(j):
    driver.get(alinks[j])
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
    with open(f'{filename_innerText}'+'.json', "w", encoding='utf-8') as file:
        file.write(json.dumps(
            results, ensure_ascii=False, indent=4))
    print("檔案", filename_innerText, "存好了")

    df = pd.read_json(filename_innerText+'.json')
    df.to_csv(filename_innerText+'.csv',
                index=None, encoding="utf_8_sig")




if __name__ == '__main__':
    for i in range(range1,range2):
        driver.find_element(By.CSS_SELECTOR,'#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)').click()
        links()
    sleep(0.5)
    for i in range(len(plink_ptitle)):
        reply(i)
    savejson()

print(filename_innerText + '存好了')
driver.quit()