from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import json 

# 啟動瀏覽器工具的選項

my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  # 設定為正體中文
my_options.add_argument('blink-settings=imagesEnabled=false') # 不載入圖

driver = uc.Chrome(
    options = my_options,
    # service = Service(ChromeDriverManager().install())
)
# driver = uc.Chrome(options=my_options)

'''爬取搜尋結果'''
links=[]
results = []

print('登入中...')
#发送请求
driver.get("https://s.weibo.com/")
wait = WebDriverWait(driver,5)
# time.sleep(50)
 
 #使用selector去定位搜尋框

s_input = driver.find_element(By.XPATH,'//*[@id="pl_homepage_search"]/div/div[2]/div/input')
s_input.send_keys('寶可夢')
s_input.send_keys(Keys.ENTER)

post=driver.find_elements(By.CSS_SELECTOR,'#pl_feedlist_index > div:nth-child(2) > div > div.card > div > div.content > p')

un=driver.find_elements(By.CSS_SELECTOR,'#pl_feedlist_index > div:nth-child(2) > div > div > div.card-feed > div.content > div.info > div:nth-child(2) > a')

for i in range(len(post)):
    pst= un[i].get_attribute('innerText')
    name=(post[i].get_attribute('innerText'))
    result={
        '微博帳號':name,
        '發文內容':pst
    }
results.append(result)

with open('weibo.json', "w", encoding='utf-8') as file:
    file.write(json.dumps(
        results, ensure_ascii=False, indent=4))