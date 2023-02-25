# 導入 模組(module) 
import requests 
# 導入 BeautifulSoup 模組(module)：解析HTML 語法工具
import bs4

# 文章連結
URL = "https://www.ptt.cc/bbs/sex/M.1665920643.A.057.html"
# 設定Header與Cookie
my_headers = {'cookie': 'over18=1;'}
# 發送get 請求 到 ptt 八卦版
response = requests.get(URL, headers = my_headers)


#  把網頁程式碼(HTML) 丟入 bs4模組分析
soup = bs4.BeautifulSoup(response.text,"html.parser")

## PTT 上方4個欄位
header = soup.find_all('span','article-meta-value')

# 作者
author = header[0].text
# 看版
board = header[1].text
# 標題
title = header[2].text
# 日期
date = header[3].text


## 查找所有html 元素 抓出內容
main_container = soup.find(id='main-container')
# 把所有文字都抓出來

all_text = main_container.text
pre_text = all_text.split('--')[0]
texts = pre_text.split('\n')
contents = texts[2:]
print(contents)
# content = '\n'.join(contents)
# # 顯示
# print('作者：'+author)
# print('看板：'+board)
# print('標題：'+title)
# print('日期：'+date)
# print('內容：'+content)