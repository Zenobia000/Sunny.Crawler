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
# my_options.add_experimental_option(
#     "excludeSwitches", ['enable-automation', 'enable-logging'])  # 沒有異常log
driver = uc.Chrome(
    options=my_options,
    # service=Service(ChromeDriverManager().install())
)
# driver = uc.Chrome(options=my_options)

tmpcomment = set()
results = []
results = []

# 去Dcard科技版
# driver.get('https://www.dcard.tw/f/tech_job/p/240646522')
# --------------------------------------------------------------------------
folderPath_r = r'C:\Selenium\dcard\Dcard_links_new.json'
# 讀檔
file = open(folderPath_r, 'r', encoding='utf-8')
all_links = json.load(file)

# 調整要爬的page範圍
print('=======================================')
start = input('起始頁數:')
end = input('結束頁數:')
print('=======================================')
# 你要放哪裡
folderPath_w = 'C:/Selenium/dcard/'
filename_innerText = 'Dcard_V1'+start+'_'+end
# --------------------------------------------------------------------------


def end_craw():
    title = driver.find_element(
        By.CSS_SELECTOR, 'div > h1').get_attribute('innerText')
    # 內文
    try:
        txt = driver.find_element(By.CSS_SELECTOR, 'article > div.atm_lo_c0ivcw.atm_le_1ad2xrm.cgmw135 > div > div').get_attribute(
            'innerText').replace('\n', '')
    except:
        txt= driver.find_element(By.CSS_SELECTOR,'#__next > div > div.f1og407v > div > div > div > div > article > div.atm_lo_c0ivcw.atm_le_1ad2xrm.cgmw135 > div > a > div > div.m1vig5f1 > div >div').get_attribute('innerText').replace('\n', '')
    
    date = driver.find_element(
        By.CSS_SELECTOR, ' div.atm_c8_3rwk2t.atm_9s_1txwivl.atm_h_1h6ojuz.atm_h3_1fwxnve.i1ym7go5 > div:nth-child(2)').get_attribute('innerText')

    try:
        HC_total = driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div[5]/div/div/div[1]').get_attribute('innerText')
        HC_totals = HC_total.replace('\n', ' ').split(' ')
    except: 
        HC_total=driver.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div[2]/div/div/div/div/div[6]/div/div/div[1]').get_attribute('innerText')
        HC_totals = HC_total.replace('\n', ' ').split(' ')
    try:
        tickets = driver.find_element(
            By.CSS_SELECTOR, '#__next > div  div:nth-child(4) > div > ul').get_attribute('innerText')
        ticket = tickets.replace('\n', ',')
    except:
        print('ticket沒標籤')
        ticket = 'None'
    result = {
        '文章標題': title,
        '發文內容': txt,
        '發文時間': date,
        '文章標籤': ticket,
        '愛心數量': HC_totals[0],
        '留言數量': HC_totals[-1],
        '內文留言': ''
    }
    # tmp.add(result)
    results.append(result)



def craw_1():
    try:
        WebDriverWait(driver, 3).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, '#dcard-comment-anchor > div > div > div.atm_l8_1077ktj.c34rbji > section > div > div > div > div > div > div > div > div >span')))
        comments = driver.find_elements(
            By.CSS_SELECTOR, '#dcard-comment-anchor > div > div > div.atm_l8_1077ktj.c34rbji > section > div > div > div > div > div > div > div > div >span')
        for comment in comments:
            commentss = comment.get_attribute('innerText')
            commentsss = commentss.replace('\n', '')
            commentssss = [commentsss]
            tmpcomment.update(commentssss)
    except:
        commentssss='None'
        tmpcomment.update(commentssss)


def btntest():
    btn = driver.find_elements(
        By.CSS_SELECTOR, '#dcard-comment-anchor > div > div > div.atm_l8_1077ktj.c34rbji > section > div > div > div > div > div > button')

    for i in range(len(btn)):
        try:
            btn[i].click()
            sleep(2)
            craw_1()
        except:
            continue


def finally_scroll():

    innerHeight = driver.execute_script(
        'return window.document.documentElement.scrollHeight;'
    )
    innerHeight += 800
    driver.execute_script(f'''
        window.scrollTo({{
            top: {innerHeight}, 
            behavior: 'smooth' 
        }});
    ''')


def f_btntest():
    btn = driver.find_elements(
        By.CSS_SELECTOR, '#dcard-comment-anchor > div > div > div.atm_l8_1077ktj.c34rbji > section > div > div > div > div > div > button')

    for i in range(len(btn)):
        try:
            btn[i].click()
            sleep(2)
            craw_1()
            finally_scroll()
        except:
            continue


def scroll_D():
    innerHeight = 0
    offset = 0
    count = 0
    limit = 1

    # 在捲動到沒有元素動態產生前，持續捲動
    while count <= limit:
        # offset = driver.execute_script(
        #     'return window.document.documentElement.scrollHeight;'
        # )
        sleep(2)

        btntest()
        sleep(1)
        craw_1()
        offset += 800
        driver.execute_script(f'''
            window.scrollTo({{
                top: {offset}, 
                behavior: 'smooth' 
            }});
        ''')
        # 透過執行 js 語法來取得捲動後的當前總高度
        innerHeight = driver.execute_script(
            'return window.document.documentElement.scrollHeight;'
        )
        if offset >= innerHeight:
            count += 1


def savejson():
    with open(f'{folderPath_w}{filename_innerText}'+'.json', "a", encoding='utf-8') as file:
        file.write(json.dumps(
            results, ensure_ascii=False, indent=4))
    print("檔案", filename_innerText, "存好了")

    df = pd.read_json(f'{folderPath_w}{filename_innerText}.json')
    df.to_csv(f'{folderPath_w}{filename_innerText}'+'.csv',
              index=None, encoding="utf_8_sig")


results_num = 0

if int(start) <= 0:
    print('起始頁數是1喔，笨蛋')
    driver.quit()
else:
    for num in range(int(start)-1, int(end)):
        try:
            driver.get(all_links[num])
            print('目前在第'+str(num)+'頁')
            print(all_links[num])
            sleep(3)
            end_craw()
            scroll_D()
            btntest()
            f_btntest()
            finally_scroll()
            craw_1()
            for commentt in tmpcomment:
                commentt.replace('', 'None')
                results[results_num]['內文留言'] = results[results_num]['內文留言']+commentt
            tmpcomment = set()
            results_num += 1
        except:
            continue #繼續下一個循環

savejson()
print('我存完了，我離開了')
# driver.quit()
