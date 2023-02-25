from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import json
import os
import subprocess
import re
# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")                #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)
# folderPath = '中文電子書'
# if not os.path.exists(folderPath):
#     os.makedirs(folderPath)



    
listData = []
titleData= []

texttitle = []
print(texttitle)

start = 200 # 設定起始網頁
end = 400

for i in range (start,end,1):
    #前往每個爬取文字的網站
    driver.get(titleData[i])
    
    title = driver.find_element(By.CSS_SELECTOR,'div.page_content>h1')
    t= title.get_attribute('innerText')
    print (t)
    texttitle.append(t)
    # print(texttitle)
# 古騰堡
url = "https://www.gutenberg.org/browse/languages/zh"
Furl = "https://www.gutenberg.org/files"
Turl = 'https://www.gutenberg.org/ebooks'
# 首頁網址
driver.get(url)

# 取得標題跟連結
linkelements = driver.find_elements(By.CSS_SELECTOR,'div.pgdbbylanguage > ul > li > a')
for linkelement in linkelements :
    aTitle = linkelement.get_attribute('innerText')
    aLink = linkelement.get_attribute('href')
    id = aLink.split('ebooks')[1]
    if id == '/20968':
        continue
    if id == '/38580':
        continue
    if id == '/38585':
        continue
    if id == '/49965':
        continue
    Dlink = Furl+id+id+'-0.txt'
    Tlink = Turl+id
    if Dlink == 'https://www.gutenberg.org/files/20968/20968-0.txt':
        continue
    if Dlink == 'https://www.gutenberg.org/files/38580/38580-0.txt':
        continue
    if Dlink == 'https://www.gutenberg.org/files/38585/38585-0.txt':
        continue
    if Dlink == 'https://www.gutenberg.org/files/49965/49965-0.txt':
        continue
    listData.append(Dlink)
    titleData.append(Tlink)
    # print(id)
    # print(aTitle)
    # print(Dlink)
    # print ('='*30)

# 點入

start = 0 # 設定起始網頁
end = 200

for i in range (start,end,1):
    driver.get(titleData[i])
    title = driver.find_element(By.CSS_SELECTOR,'div.page_content>h1')
    t= title.get_attribute('innerText')
    texttitle.append(t)
driver.get('https://www.gutenberg.org/files/25328/25328-0.txt')
Text = driver.find_element(By.CSS_SELECTOR,"pre[style='word-wrap: break-word; white-space: pre-wrap;']")
strText = Text.get_attribute('innerText')
print(Text.get_attribute('innerText'))

reg01 = r'[\u4e00-\u9fa5，。]+'
# reg02 = r'[]'
strText = Text.get_attribute('innerText')
Ftext = re.findall(reg01,strText) #这里是精髓，[\u4e00-\u9fa5]是匹配所有中文的正则，
strFtext =''.join(Ftext)
print(Ftext)
# 經測試發現  20968,38580,38585是空網址
i = 'https://www.gutenberg.org/files/49965/49965-0.txt'

if i in listData :
    print("ture")
else :
    print ("false")

start = 200 # 設定起始網頁
end = 400

for i in range (start,end,1):
    #前往每個爬取文字的網站
    driver.get(listData[i])
    #爬取內文
    Text = driver.find_element(By.CSS_SELECTOR,"pre[style='word-wrap: break-word; white-space: pre-wrap;']")
    strText = Text.get_attribute('innerText')
    #篩選中文
    reg01 = r'[\u4e00-\u9fa5，。]+'
    strText = Text.get_attribute('innerText')
    Ftext = re.findall(reg01,strText) #这里是精髓，[\u4e00-\u9fa5]是匹配所有中文的正则，
    strFtext =''.join(Ftext)
    #寫進檔案
    sleep(0.5)
    myfile = open(texttitle[i]+'.txt','w',encoding='utf-8')
    with open(texttitle[i]+'.txt','w',encoding='utf-8') as file:
        myfile.write(strFtext)
    
