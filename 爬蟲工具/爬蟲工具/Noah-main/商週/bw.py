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


# 啟動瀏覽器工具的選項

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
driver = webdriver.Chrome(
    options=my_options,
    service=Service(ChromeDriverManager().install()))

urlindex=input('請輸入網址編號 0~15:')

# sunny 0,1
# noah 2,3
# mm 4,5
# xiong 6,7
# yen 8,9
# yuan 10,11,12
# kevin 13,14,15

links=['https://www.businessweekly.com.tw/channel/world/0000000317',
       'https://www.businessweekly.com.tw/channel/china/0000000318',
       'https://www.businessweekly.com.tw/channel/insight/0000000320',
       'https://www.businessweekly.com.tw/channel/trends/0000000321',
       'https://www.businessweekly.com.tw/channel/people/0000000322',
       'https://www.businessweekly.com.tw/channel/money/0000000323',
       'https://www.businessweekly.com.tw/channel/realestate/0000000324',
       'https://www.businessweekly.com.tw/channel/digitaltransformation/0000000327',
       'https://www.businessweekly.com.tw/channel/Innovation/0000000328',
       'https://www.businessweekly.com.tw/channel/marketing/0000000329',
       'https://www.businessweekly.com.tw/channel/leadership/0000000330',
       'https://www.businessweekly.com.tw/channel/careerplanning/0000000332',
       'https://www.businessweekly.com.tw/channel/entrepreneurship/0000000333',
       'https://www.businessweekly.com.tw/channel/selfgrowth/0000000334',
       'https://www.businessweekly.com.tw/channel/englishlearning/0000000335',
       'https://www.businessweekly.com.tw/channel/education/0000000336']

url=links[int(urlindex)]

driver.get(url)

alinks=[]
results=[]

def scroll():
    '''
    innerHeight => 瀏覽器內部的高度
    offset => 當前捲動的量(高度)
    count => 累計無效滾動次數
    limit => 最大無效滾動次數
    '''
    innerHeight = 0
    offset = 0
    count = 0
    limit = 3
    
    # 在捲動到沒有元素動態產生前，持續捲動
    while count <= limit:
        # 每次移動高度
        offset += 2000

        # offset = driver.execute_script(
        #     'return window.document.documentElement.scrollHeight;'
        # )

        '''
        或是每次只滾動一點距離，
        以免有些網站會在移動長距離後，
        將先前移動當中的元素隱藏

        例如將上方的 script 改成:
        offset += 600
        '''

        # 捲軸往下滑動
        driver.execute_script(f'''
            window.scrollTo({{
                top: {offset}, 
                behavior: 'smooth' 
            }});
        ''')
        
        # 強制等待，此時若有新元素生成，瀏覽器內部高度會自動增加
        sleep(3)
        
        # 透過執行 js 語法來取得捲動後的當前總高度
        innerHeight = driver.execute_script(
            'return window.document.documentElement.scrollHeight;')
        try:
            # 元素
            button = driver.find_element(
                By.CSS_SELECTOR, 'button#LoadMore5')
            button.click()
        except:
            pass

        # 經過計算，如果滾動距離(offset)大於等於視窗內部總高度(innerHeight)，代表已經到底了
        if offset >= innerHeight:
                count += 1

def input_links():
    links = driver.find_elements(
        By.CSS_SELECTOR, '#Copy-flag > figcaption > div.Article-content.d-xs-flex > a')
    # for i in links:
    #     print(i.get_attribute('href'))
    for link in links:
        alinks.append(link.get_attribute('href'))

def craw2():
    try:
        in_text = driver.find_element(By.CSS_SELECTOR, 'section.row.no-gutters.position-relative > div.Single-left-part.col-xs-12.col-md-7.col-lg-8 > section.Single-article > div.Single-article.WebContent')
        in_text = in_text.get_attribute('innerText')
        text = in_text.replace('\n', ' ')
    except:
        text = 'None'
    result = {
        '文章內容': text
    }
    results.append(result)

if __name__ == '__main__':
    scroll()
    input_links()
    print('總頁數:')
    print(len(alinks))
    for j in range(len(alinks)):
        print(j, alinks[j])
        driver.get(alinks[j])
        sleep(5)
        craw2()

    with open('businessweekly' + urlindex + '.txt','w', encoding='utf-8') as fp:
        for r in results:
            fp.write("%s\n" % r)
        print('businessweekly' + urlindex + '.txt 已存檔')

    driver.quit()