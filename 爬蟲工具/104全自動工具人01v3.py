#import
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

#driver
my_options = webdriver.ChromeOptions()
my_options.add_argument("--start-maximized")         #最大化視窗
my_options.add_argument("--incognito")               #開啟無痕模式
my_options.add_argument("--disable-popup-blocking") #禁用彈出攔截
my_options.add_argument("--disable-notifications")  #取消 chrome 推播通知
my_options.add_argument("--lang=zh-TW")  #設定為正體中文

driver = webdriver.Chrome(
    options = my_options,
    service = Service(ChromeDriverManager().install())
)

#city
city = ['臺北', '新北', '宜蘭', '基隆', '桃園', '新竹', '苗栗', '台中', '無縣市', '彰化',
        '南投', '雲林', '嘉義', '台南', '無縣市', '高雄', '無縣市', '屏東', '台東', '花蓮',
        '澎湖', '金門', '連江']
#districts
#ndistrict = [12, 29, 12, 7, 13, 14, 18, 29, 0, 26,
#             13, 20, 19, 37, 0, 38, 0,  33, 16, 13,
#             6, 6, 4]

district = [
    ["中正區", "大同區", "中山區", "松山區", "大安區", "萬華區", "信義區", "士林區", "北投區", "內湖區", "南港區", "文山區"],
    
    ["萬里區", "金山區", "板橋區", "汐止區", "深坑區", "石碇區", "瑞芳區", "平溪區", "雙溪區", "貢寮區", "新店區", "坪林區",
     "烏來區", "永和區", "中和區", "土城區", "三峽區", "樹林區", "鶯歌區", "三重區", "新莊區", "泰山區", "林口區", "蘆洲區",
     "五股區", "八里區", "淡水區", "三芝區", "石門區"],
     
    ["宜蘭市", "頭城鎮", "礁溪鄉", "壯圍鄉", "員山鄉", "羅東鎮", "三星鄉", "大同鄉", "五結鄉", "冬山鄉", "蘇澳鎮", "南澳鄉"],
    
    ["仁愛區", "信義區", "中正區", "中山區", "安樂區", "暖暖區", "七堵區"],
    
    ["中壢區", "平鎮區", "龍潭區", "楊梅區", "新屋區", "觀音區", "桃園區", "龜山區", "八德區", "大溪區", "復興區"
    "大園區", "蘆竹區"],
    
    ["新竹市", "竹北市", "湖口鄉", "新豐鄉", "新埔鎮", "關西鎮", "芎林鄉", "寶山鄉", "竹東鎮", "五峰鄉", "橫山鄉", "尖石鄉",
     "北埔鄉", "峨眉鄉"],
    
    ["竹南鎮", "頭份市", "三灣鄉", "南庄鄉", "獅潭鄉", "後龍鎮", "通霄鎮", "苑裡鎮", "苗栗市", "造橋鄉", "頭屋鄉", "公館鄉",
     "大湖鄉", "泰安鄉", "銅鑼鄉", "三義鄉", "西湖鄉", "卓蘭鎮"],
    
    
    ["中區", "東區", "南區", "西區", "北區", "北屯區", "西屯區", "南屯區", "太平區", "大里區", "霧峰區", "烏日區", "豐原區",
     "后里區", "石岡區", "東勢區", "和平區","新社區", "潭子區", "大雅區", "神岡區", "大肚區", "沙鹿區", "龍井區", "梧棲區",
     "清水區", "大甲區", "外埔區","大安區"],
    
    [],
    
    ["彰化市", "芬園鄉", "花壇鄉", "秀水鄉", "鹿港鎮", "福興鄉", "線西鄉", "和美鎮", "伸港鄉", "員林市", "社頭鄉", "永靖鄉",
     "埔心鄉", "溪湖鎮", "大村鄉", "埔鹽鄉", "田中鎮", "北斗鎮", "田尾鄉", "埤頭鄉", "溪州鄉", "竹塘鄉", "二林鎮", "大城鄉",
     "芳苑鄉", "二水鄉"],
    
    ["南投市", "中寮鄉", "草屯鎮", "國姓鄉", "埔里鎮", "仁愛鄉", "名間鄉", "集集鎮", "魚池鄉", "水里鄉", "信義鄉", "竹山鎮",
     "鹿谷鄉"],
    
    ["斗南鎮", "大埤鄉", "虎尾鎮", "土庫鎮", "褒忠鄉", "東勢鄉",  "臺西鄉", "崙背鄉", "麥寮鄉","斗六市", "林內鄉", "古坑鄉",
     "莿桐鄉", "西螺鎮", "二崙鄉", "北港鎮", "水林鄉", "口湖鄉", "四湖鄉", "元長鄉"],
    
    ['嘉義市', '番路鄉', '梅山鄉', '竹崎鄉', '阿里山鄉', '中埔鄉', '大埔鄉', '水上鄉', '鹿草鄉', '太保市', '朴子市', '東石鄉',
     '六腳鄉', '新港鄉', '民雄鄉', '大林鎮', '溪口鄉', '義竹鄉','布袋鎮'],
    
    ["中西區", "東區", "南區", "北區", "安平區", "安南區", "永康區", "歸仁區", "新化區", "左鎮區", "玉井區", "楠西區", "南化區",
     "仁德區", "關廟區", "龍崎區", "官田區", "麻豆區", "佳里區", "西港區", "七股區", "將軍區", "學甲區", "北門區", "新營區",
     "後壁區", "白河區", "東山區", "六甲區", "下營區", "柳營區", "鹽水區", "善化區", "大內區", "山上區", "新市區", "安定區"],
    
    [],
    
    ['新興區', '前金區', '苓雅區', '鹽埕區', '鼓山區', '旗津區', '前鎮區', '三民區', '楠梓區', '小港區', '左營區', '仁武區', '大社區',
     '岡山區', '路竹區', '阿蓮區', '田寮區', '燕巢區', '橋頭區', '梓官區', '彌陀區', '永安區', '湖內區', '鳳山區', '大寮區', '林園區',
     '鳥松區', '大樹區', '旗山區', '美濃區', '六龜區', '內門區', '杉林區', '甲仙區', '桃源區', '那瑪夏區', '茂林區', '茄萣區'],
    
    [], 
    ['屏東市', '三地門鄉', '霧臺鄉', '瑪家鄉', '九如鄉', '里港鄉', '高樹鄉', '鹽埔鄉', '長治鄉', '麟洛鄉', '竹田鄉', '內埔鄉',
     '萬丹鄉', '潮州鎮', '泰武鄉', '來義鄉', '萬巒鄉', '崁頂鄉', '新埤鄉', '南州鄉', '林邊鄉', '東港鎮', '琉球鄉',  '佳冬鄉', 
     '新園鄉', '枋寮鄉', '枋山鄉', '春日鄉', '獅子鄉', '車城鄉', '牡丹鄉', '恆春鎮', '滿州鄉'],
    
    ['臺東市', '綠島鄉', '蘭嶼鄉', '延平鄉', '卑南鄉', '鹿野鄉',  '關山鎮', '海端鄉', '池上鄉', '東河鄉', '成功鎮', '長濱鄉', '太麻里鄉',
     '金峰鄉', '大武鄉', '達仁鄉'],
    
    ['花蓮市', '新城鄉', '秀林鄉', '吉安鄉', '壽豐鄉', '鳳林鎮', '光復鄉', '豐濱鄉', '瑞穗鄉', '萬榮鄉',
     '玉里鎮', '卓溪鄉', '富里鄉'],
    
    ['馬公市', '西嶼鄉', '望安鄉', '七美鄉', '白沙鄉','湖西鄉'],
    
    ['金沙鎮','金湖鎮', '金寧鄉', '金城鎮', '烈嶼鄉', '烏坵鄉'],
    
    ['南竿鄉', '北竿鄉', '莒光鄉', '東引鄉']
]

# job15 大類別 生產製造_品管_環衛類
# 所有編號 2維矩陣

# ['經營人資類 1', '行政總務法務類 2', '財會金融專業類 3',  
# '行銷企劃專案管理類 4', '客服門市業務貿易類 5', '餐飲旅遊美容美髮類 6', 
# '資訊軟體系統類 7', '操作技術維修類 10','資材物流運輸類 11',
#  '營建製圖類 12', '傳播藝術設計類 13', '文字傳媒工作類 14',
#  '醫療保健服務類 15', '學術教育輔導類 16', '研發相關類 8', 
# '生產製造品管環衛類 9', '軍警消_保全類 17', '其他職類 18']

job15_list = [['2015001001', '2015001003', '2015001005', '2015001006', '2015001008', '2015001010', '2015001012', '2015001013', '2015001016',
                '2015001002', '2015001004', '2015001007', '2015001009', '2015001011', '2015001015', '2015001014', '2015001017'
                , '2015001018', '2015001019', '2015001020', '2015001021', '2015001022', '2015001023', '2015001024'],
              ['2015002001', '2015002002', '2015002004', '2015002005', '2015002006', '2015002007', '2015002008', '2015002012', '2015002011',
              '2015002010', '2015002009']]

# 中類別名稱
job15_name1 = ['醫療專業類人員', '醫療_保健服務人員']

# 小類別名稱
job15_name2 = [['醫事', '醫事檢驗師', '藥師', '營養師', '公共衛生醫師', '麻醉醫師', '復健技術師', '治療師', '醫事放射師', '牙醫師', '護理師', '獸醫師', '中醫師', '驗光師', '藥學助理', '其他醫療人員', '呼吸治療師', '職能治療師', '物理治療師', '語言治療師', '專科治療師', '牙體治療師', '心理師', '勞工健康服務護理人員'], 

['醫院行政管理人員', '照顧服務員', '按摩_推拿師', '診所助理', '牙醫助理', '放射性設備使用技術員', '醫療設備控制人員', '居家服務督導員', '照顧指導員', '安心服務員', '其他醫療從業人員']
]

# ----------------------------------------------------------------------------------------------------------------------------------------
def inputlink():
    links = driver.find_elements(
        By.CSS_SELECTOR, "li.job-mode__jobname > a"
    )
    for link in links:
        href = link.get_attribute('href')
        alinks.append(href)

    # batterys
    use_selectors = driver.find_elements(
        By.CSS_SELECTOR,
        'ul > li.job-mode__candidates.js-apply-cnt > a > svg > use'
    )
    for use in use_selectors:
        battery = use.get_attribute('xlink:href')[-1]
        batterys.append(battery)
        
    if len(alinks) != len(batterys):
        print("第"+str(i)+"頁有誤！")

def craw(i): #by noah
    b = int(batterys[i])
    try:
        # 等待篩選元素出現
        IDN = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                'div.job-header__btn.mb-3 > div > form > input[type=hidden]:nth-child(1)')
            )
        )
    except TimeoutException: #invalid link
        result = {
            '職缺連結':None,
            '職缺類別': None,
            '職位類別': None,
            '職位': None,
            '大職業編號': None, 
            '中職業編號': None,
            '小職業編號': None,     
            '縣市': None,    
            '地區': None,  
            '縣市編碼': None,
            '地區編碼': None,
            '公司連結': None,
            '供需人數': None,
            '職缺編號': None,
            '公司名稱': None,
            '職缺名稱': None,
            '更新日期': None,
            '工作內容': None,
            '職務類別': None,
            '工作待遇': None,
            '工作性質': None,
            '上班地點': None,
            '管理責任': None,
            '上班時段': None,
            '需求人數': None,
            '工作經歷': None,
            '學歷要求': None,
            '科系要求': None,
            '擅長工具': None,
            '工作技能': None,
            '其他條件': None,
            '福利制度': None
        }
        results.append(result)
        return
    
    IDN = driver.find_element(
        By.CSS_SELECTOR, 'div.job-header__btn.mb-3 > div > form > input[type=hidden]:nth-child(1)').get_attribute('value')
    workname = driver.find_element(
        By.CSS_SELECTOR, 'div.job-header__title>h1').get_attribute("innerText")
    workupdate = driver.find_element(
        By.CSS_SELECTOR, 'div.job-header__title>h1>span').get_attribute("innerText")
    work = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]').get_attribute("innerText")
    companymame = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div/div[1]/div/a[1]').get_attribute("innerText")
    company_link = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[1]/div[2]/div/div/div[1]/div/a[1]').get_attribute('href')
    workclass = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div[2]').get_attribute("innerText")
    salary = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/div[2]').get_attribute("innerText")
    xìngzhì = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[4]/div[2]/div').get_attribute("innerText")
    locate = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[5]/div[2]/div').get_attribute("innerText")
    responsibility = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[7]/div[2]').get_attribute("innerText")
    workhr = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[9]/div[2]').get_attribute("innerText")

    try:
        needp = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.job-description-table.row > div:nth-child(10) > div.col.p-0.list-row__data > div'))
        )
        needp = driver.find_element(
            By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[2]/div[12]/div[2]').get_attribute("innerText")

    except:
        needp = driver.find_element(
            By.CSS_SELECTOR, 'div.job-description-table.row > div:nth-child(9) > div.col.p-0.list-row__data > div').get_attribute("innerText")

    experience = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div').get_attribute("innerText")
    Education = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div').get_attribute("innerText")
    DPR = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[2]/div[3]/div[2]/div').get_attribute("innerText")
    tools = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[2]/div[5]/div[2]/div').get_attribute("innerText")
    wskills = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[2]/div[6]/div[2]/div').get_attribute("innerText")
    others = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/p').get_attribute("innerText")
    otherss=others.replace('\n', '')
        
    # Welfare =driver.find_elements(By.CSS_SELECTOR,'div.col > p.r3.mb-0.text-break')
    try:
        Welfare = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.col > p.r3.mb-0.text-break"))
        )
        Welfare = driver.find_elements(
            By.CSS_SELECTOR, 'div.col > p.r3.mb-0.text-break')
    except:
        Welfare = None

    workk = work.replace('\n', '')
    fwork = workk.replace('-', '')
        
    if b == 1:
        people = 2.5
    elif b == 2:
        people = 7.5
    elif b == 3:
        people = 20
    elif b ==4:
        people = 60
    else:
        print("battery wrong")

    if Welfare != None:
        result = {
            '職缺連結':alinks[i],
            '職缺類別': a1, #'經營_人資類'
            '職位類別': a2, #'經營_幕僚類人員' 
            '職位': a3,     #'儲備幹部'
            '大職業編號': a_large, 
            '中職業編號': a_med,
            '小職業編號': a_small,
            '縣市': a4,     #'新北市' 
            '地區': a5,     #'板橋區'
            '縣市編碼': a_city,
            '地區編碼': a_district,
            '公司連結': company_link,
            '供需人數': people,
            '職缺編號': IDN,
            '公司名稱': companymame,
            '職缺名稱': workname,
            '更新日期': workupdate,
            '工作內容': fwork,
            '職務類別': workclass.replace('\n', ''),
            '工作待遇': salary.replace('\n', ''),
            '工作性質': xìngzhì,
            '上班地點': locate,
            '管理責任': responsibility,
            '上班時段': workhr,
            '需求人數': needp,
            '工作經歷': experience,
            '學歷要求': Education,
            '科系要求': DPR,
            '擅長工具': tools.replace('\n', ''),
            '工作技能': wskills,
            '其他條件': otherss.replace('\t',''),
            '福利制度': Welfare[0].get_attribute("innerText").replace('\n', '')
        }

    else:
        result = {
            '職缺連結':alinks[i],
            '職缺類別': a1, #'經營_人資類'
            '職位類別': a2, #'經營_幕僚類人員'
            '職位': a3,     #'儲備幹部'
            '大職業編號': a_large, 
            '中職業編號': a_med,
            '小職業編號': a_small,
            '縣市': a4,     #'新北市' 
            '地區': a5,     #'板橋區'
            '縣市編碼': a_city,
            '地區編碼': a_district,
            '公司連結': company_link,
            '供需人數': people,
            '職缺編號': IDN,
            '公司名稱': companymame,
            '職缺名稱': workname,
            '更新日期': workupdate,
            '工作內容': fwork,
            '職務類別': workclass.replace('\n', ''),
            '工作待遇': salary.replace('\n', ''),
            '工作性質': xìngzhì,
            '上班地點': locate,
            '管理責任': responsibility,
            '上班時段': workhr,
            '需求人數': needp,
            '工作經歷': experience,
            '學歷要求': Education,
            '科系要求': DPR,
            '擅長工具': tools.replace('\n', ''),
            '工作技能': wskills,
            '其他條件': otherss.replace('\t',''),
            '福利制度': Welfare
        }
    results.append(result)
    sleep(1)

#main
for i in range(1, len(city)):
    
    city_id = i+1
    city_str = "0"+str(city_id) if city_id<10 else str(city_id)
    print('city='+ str(i+1), end =", ")

    for j in range(len(district[i])):
        district_id = j+1
        district_str = "0"+str(district_id) if district_id<10 else str(district_id)
        print('area='+ str(j+1), end ="; ")

        for jobi in range(len(job15_list)):
            print('career_mid='+ str(jobi+1), end ="; ")

            for jobj in range(len(job15_list[jobi])):
                if jobj == len(job15_list[jobi]):
                    print("") 
                print('career_small='+ str(jobj+1), end =", ")

                job_num = job15_list[jobi][jobj]
                url= 'https://www.104.com.tw/jobs/search/?ro=0&jobcat='+job_num+'&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=60010'+city_str+'0'+district_str+'&order=16&asc=0&page=1&mode=l&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
                driver.get(url)
                sleep(0.5)
            
                #total links
                totallinks_str = driver.find_elements(
                    By.CSS_SELECTOR,'#js-job-tab > li.b-nav-tabs__active > span')[0].text
                totallinks_num = int(totallinks_str[1:-1])   # (17) -> 17, final page
            
                alinks = []
                batterys = []
                results = []
            
                a1 = '醫療保健服務類' #手動改
                a2 = job15_name1[jobi]
                a3 = job15_name2[jobi][jobj]
                a_large = 13 #手動改
                a_med = int(job_num[5:7])
                a_small = int(job_num[8:])
                a4 = city[i]
                a5 = district[i][j]
                a_city = city_id
                a_district = district_id
            
                for page in range(1, 101): #suppose 100 pages
                    try: 
                        check_if_there_is_link = WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located(
                                (By.CSS_SELECTOR, 'li.job-mode__jobname > a')))
                    except TimeoutException: #no links, it's last page
                        break
                        
                    # not last page
                    inputlink()
                
                #run all alinks to get job detail
                for l, link in enumerate(alinks[:totallinks_num]):
                    driver.get(link)
                    print("#" + str(l+1), end= ", ")
                    sleep(0.2)
                    craw(l)
                    if link == alinks[totallinks_num-1]:
                        print('')
              
                #save json
                filename_innerText = job_num+'_'+city_str+district_str+'.json'
                with open(f'C:/Users/xdxd2/Sunny_VS_worksapce/Sunny_python/專案/人力銀行/爬蟲資料/2015/{filename_innerText}', "w", encoding='utf-8') as file:
                    file.write(json.dumps(results, ensure_ascii=False, indent=4))
                print("檔案: ", filename_innerText, "下載完畢")

driver.quit()



