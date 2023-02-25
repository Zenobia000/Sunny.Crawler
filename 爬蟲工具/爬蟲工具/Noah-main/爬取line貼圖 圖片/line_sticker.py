from functools import cache
import requests as req
from bs4 import BeautifulSoup as bs
import os, json
from pprint import pprint
from urllib import parse


url = "https://store.line.me/stickershop/author/92843/zh-Hant"

# 隨機取得 User-Agent
from fake_useragent import UserAgent
ua = UserAgent(cache=True) # cache=True 表示從已經儲存的列表中提取

# 建立儲存圖片的資料夾，不存在就新增
folderPath = 'line_stickers_cat_m'
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
    
#放貼圖資訊用
listLineStickers = []

# 自訂標頭
my_headers = {
    'user-agent': ua.random
}


#------

res = req.get(url)
soup = bs(res.text, 'lxml')

# 網址 list
link_list = []

for link in soup.select("li.mdCMN02Li a"):
    link_list.append("https://store.line.me/" + link['href'])
    # pprint(link.select("p.mdCMN05Ttl").get_text())
    
# pprint(link_list)

# for link in soup.select("li.mdCMN02Li  div.MdCMN05Item.mdCMN05Sticker  p.mdCMN05Ttl"):
#     os.makedirs(f"{folderPath}/{link.get_text()}")
#     print(link.get_text())
    

# 根據每個網址 在細部抓圖
# 每個網址放圖片的區域
imginfo = []

for index, link in enumerate(link_list):

    res = req.get(link)
    soup_ = bs(res.text, "lxml")
    li_elements = soup_.select('li.mdCMN09Li.FnStickerPreviewItem')
    for li in li_elements:
        strJson = li['data-preview']
        # pprint(strJson)
        obj = json.loads(strJson)
        imginfo.append(obj)

        
        
# pprint(imginfo)
        
for obj in imginfo:
    os.system(f"curl {obj['staticUrl']} -o {folderPath}/{obj['id']}.png")
    print(f"{obj['id']}, 已下載完成, 連結: {obj['staticUrl']}")