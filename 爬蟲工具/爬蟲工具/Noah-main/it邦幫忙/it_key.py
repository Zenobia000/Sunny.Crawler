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
from selenium.webdriver.common.keys import Keys

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
driver = webdriver.Chrome(
    options=my_options,
    # service=Service(ChromeDriverManager().install())
)

key1 = ['3G', '3ds-Max', '3ds-Max-Design', '6-Sigma', 'A+',
        'ABAQUS', 'ADA', 'ADC', 'ADO', 'ADSL',
        'AIX', 'AJAX', 'ANSI-SQL', 'ARM', 'AS/400',
        'ASIC', 'ASP', 'ASP.NET', 'ATL', 'AWS',
        'Access', 'ActionScript', 'ActiveX', 'Adabas', 'Adobe-Acrobat',
        'Adobe-Animate', 'Adobe-InDesign', 'Adobe-Photoshop', 'Adobe-XD', 'AdvanceLink',
        'After-Effects', 'Alexa', 'Android', 'Angular', 'AngularJS',
        'Apache-SOAP', 'Apple', 'ArcGis', 'ArcView', 'Assembly',
        'Authorware', 'AutoCAD', 'AutoCad-2D', 'AutoCad-3D', 'Avaya',
        'Axure-RP', 'BGP', 'BS7799', 'Baan', 'Banyan',
        'Base', 'BizTalk', 'Blender', 'Bluetooth', 'Bridges',
        'Bugzilla', 'C', 'C#', 'C++', 'C++.Net',
        'C++test', 'CA', 'CADAM', 'CAM', 'CASE',
        'CC-Mail', 'CDMA', 'CGI', 'CICS', 'CIM']
key2 = ['COBOL', 'COM/DCOM', 'CORBA', 'CPLD', 'CSS',
        'CVS', 'Cadence-Allegro', 'Calc', 'Catia', 'Checkpoint',
        'Cinema-4D', 'Circuit-Design', 'Cisco', 'Citrix', 'ClearCase',
        'ClearQuest', 'Clipper', 'CodeTest', 'Cognos', 'Cold-Fusion',
        'CoolDraw', 'CorelDraw', 'D3.js', 'DB2', 'DDK',
        'DEC/VAX', 'DHCP', 'DHTML', 'DNS', 'DOS',
        'DSP', 'DVB數位視頻廣播', 'DVR數位視頻錄像', 'Dart', 'Data-Architect',
        'Data-Guard', 'Data-Marts', 'Data-Modeling', 'DataStage', 'Database-Administrator',
        'Database-Management', 'Dbase', 'Delphi', 'Developer/-Designer-2000', 'DirectX',
        'Django', 'Domino', 'Draw', 'Dreamweaver', 'Drivers',
        'EDA', 'EDI', 'EJB', 'EMC/EMI', 'ERwin',
        'ETL', 'Electronic-Payment', 'Ethernet', 'Excel', 'FORTRAN',
        'FPGA', 'FTP', 'Figma', 'FileNet', 'Firebase',
        'Firewall', 'Fireworks', 'Firmware', 'Flash', 'Flex']
key3 = ['Flutter', 'Focus', 'Fortify', 'Fox-Pro', 'FoxBASE+',
        'FoxPro-2', 'FrameMaker', 'FreeBSD', 'FrontPage', 'GIS',
        'GPRS', 'GPS全球定位系統', 'GSM', 'Games', 'Ghost',
        'Git', 'Github', 'Go', 'Google-Analytics', 'Google-Data-Studio',
        'Google-Display-Network', 'Google-Tag-Manager', 'Google-Trend', 'Graphics', 'HP-Open-View',
        'HP-UX', 'HTML', 'HTTP', 'Hive', 'Hubs',
        'Hubs/-Routers', 'Hyperion-(Brio)', 'IATF16949', 'IDS', 'IE工業工程',
        'IIS', 'IMS', 'IPS', 'ISAPI', 'ISDN',
        'ISO-14000', 'ISO-45001', 'ISO-9000', 'Illustrator', 'Impress',
        'InVision', 'Informatica', 'Informix', 'Ingres', 'Internet-Explorer',
        'Intrusion', 'Inventor', 'J2EE', 'J2ME', 'J2SE',
        'JCL', 'JDBC', 'JMS', 'JSF', 'JSP',
        'Jasmine', 'Java', 'JavaScript', 'Jenkins', 'Juniper',
        'Junit', 'Kotlin', 'LAN', 'LDAP', 'LabVIEW']
key4 = ['LanManager', 'LanServer', 'Lantastic', 'Lease-Lines', 'LibreOffice-Writer',
        'Linux', 'Load-Balancing', 'LoadRunner', 'Lotus-Notes', 'LotusScript',
        'MAYA', 'MCU', 'MES', 'MFC', 'MIDI',
        'MMS', 'MPLS', 'MQSeries', 'MRP', 'MS-SQL',
        'MVS', 'Mac-OS', 'Mac/Macintosh', 'Macromedia-Director', 'Mainframe',
        'Mantis', 'MapGIS', 'Math', 'Matlab', 'MicroStrategy',
        'Microsoft-Dynamics-AX', 'Microsoft-Exchange', 'Microsoft-Photo-Editor', 'Microsoft-SharePoint', 'Microsoft-SmartPhone',
        'Mindnode', 'Mobile-Network', 'Mobile-phone', 'Motion-Builder', 'Multimedia-Builder',
        'MySQL', 'NDS/Novell-Directory-Services', 'Navision', 'NetWare', 'Netbios',
        'Network-Cards', 'Node.js', 'ODBC', 'OLAP', 'OOAD',
        'OOP', 'OS-X', 'OS/2', 'OS/390', 'OS/400',
        'OSPF', 'Objective-C', 'OmniGraffle', 'OneNote', 'OrCAD',
        'Oracle', 'Oracle ERP', 'Oracle Financials', 'Oracle Forms', 'Outlook',
        'P-CAD', 'PABX', 'PADS', 'PBX', 'PCBA']
key5 = ['PC—lint', 'PDA/Handhelds', 'PHP', 'PL/1', 'PL/SQL',
        'PLC', 'PPPoE', 'PSTN', 'PTC-Creo-Elements/Direct', 'Pagemaker',
        'Perl', 'PhotoImpact', 'Planner', 'PostgreSQL', 'Power-BI',
        'PowerBuilder', 'PowerPCB', 'PowerPoint', 'Premiere', 'Pro*C',
        'Pro/E', 'Progress', 'Project', 'Protel', 'Publisher',
        'Python', 'QAD－MFG/PRO', 'QTP', 'Quark-Express', 'R',
        'RDBMS', 'RF', 'RIP', 'RMI', 'RPG',
        'RTL', 'RTSP', 'Rails', 'Rational-Robot', 'Rational-Test-RealTime',
        'ReactJS', 'ReactNative', 'Redux', 'Revit', 'Rexx',
        'Rhino', 'RoHS', 'Robot', 'Routers', 'Ruby',
        'SAN', 'SAN/NAS', 'SAP', 'SAPDB', 'SAS',
        'SDLC', 'SMS', 'SMT', 'SNA', 'SNMP',
        'SOAP', 'SOLIDWORKS-Electrical', 'SPC', 'SPICE', 'SPSS',
        'SQR', 'STL', 'SUN-OS', 'SWIFT', 'SYSBASE']
key6 = ['Sass', 'Scala', 'Screaming Frog SEO Spider', 'Scribus', 'Security',
        'Servlets', 'Shell', 'Shtml', 'Silverlight', 'Silverstream',
        'SimilarWeb', 'Sketch', 'Sketch up', 'Sniffer', 'Socket',
        'Softimage', 'Solaris', 'SolidWorks', 'Sonet', 'Spring',
        'Squid', 'Struts', 'Sublime', 'Sun Solaris', 'SuperGIS',
        'Sybase', 'Synopsys', 'Systems Administration', 'Systems Analysis', 'Systems Analyst',
        'TCL', 'TCP IP', 'TIBCO', 'TK', 'TS16949',
        'Tableau', 'Tandem', 'TcpDump', 'Telecom', 'Teradata',
        'Test Scripts', 'TestBed', 'Toad', 'Tomcat', 'UDP',
        'UML', 'UNIX', 'USB OTG', 'USB技術', 'Unigraphics',
        'Unity3D', 'Unreal Engine', 'V Ray', 'VBA', 'VBScript',
        'VERITAS', 'VHDL', 'VLAN', 'VM', 'VMS',
        'VPN', 'VSAM', 'Verilog', 'Version Control', 'Visio',
        'Visual Basic', 'Visual Basic .net', 'Visual C#', 'Visual C++', 'Visual Foxpro']
key7 = ['Visual-J#', 'Visual-SourceSafe', 'Visual-Studio', 'Visual-Studio-.net', 'Vmware',
        'VoIP', 'VueJS', 'VxWorks', 'WAN', 'WAP',
        'WIN-CE', 'WLAN', 'WML', 'WPS', 'Web-Master/Developer',
        'WebAssembly', 'WebLogic', 'WebMethods', 'WebSphere', 'Win32',
        'WinForm', 'Windows-10', 'Windows-2000', 'Windows-2003', 'Windows-7',
        'Windows-8', 'Windows-95', 'Windows-98', 'Windows-Mobile', 'Windows-NT',
        'Windows-Server-2008', 'Windows-Server-2012', 'Windows-Server-2019', 'Windows-Vista', 'Windows-XP',
        'Word', 'Wordperfect', 'X++', 'X.25', 'XHTML',
        'XML', 'XML-Web-services', 'XSL', 'XSLT', 'Xmind',
        'Zbrush', 'Zeplin', 'e-commerce', 'hadoop', 'iOS',
        'iptables', 'jQuery', 'ssh', '上華ERP系統', '中文打字100~125',
        '中文打字125~150', '中文打字150以上', '中文打字20~50', '中文打字20以下', '中文打字50~75',
        '中文打字75~100', '天心資訊', '德安資訊ERP', '德安飯店餐飲管理系統', '文中系統',
        '正航', '浪潮', '用友U8', '英文打字100~125', '英文打字125~150',
        '英文打字150以上', '英文打字20~50', ' 英文打字20以下', '英文打字50~75', '英文打字75~100',
        '金旭飯店管裡系統', '金蝶', '鉅茂', '鼎基-ERP', '鼎新']
key8 = ['機器學習', '深度學習', '演算法', '監督式', '機率', 
        '人工智慧', '決策樹', '數據分析', '資料探勘', '正規化', 
        '過度配適', '特徵工程', '特徵選區', 'svm', 'random forest', 
        '隨機森林', 'sklearn', '矩陣', '自然語言處理', 'nlp', 
        'tfidf', 'word2vec', 'bert', 'logistic regression', 'linear regression', 
        '迴歸', 'elmo', 'seq2seq', 'rnn', 'cnn', 
        'knn', 'k means', '程式', 'ai', 'pca', 
        '主成分分析', '統計', 'cart', 'maximum likelihood estimation', 'gan', 
        'reinforcement learning', 'sigmoid', '資料庫', 'vscode', 'ubuntu', 
        'Decision Tree', 'ID3', 'Naive Bayes', 'Xgboost', 'NN', 
        'Polynomial Regression', 'Lasso Regression', 'Ridge Regression', 'ElasticNet Regression', 'DBSCAN', 
        'EM', 'SVD', 'PCA', 'T-SNE']

alinks=[]
results=[]

driver.get('https://ithelp.ithome.com.tw/search?tab=article')


def input_search(key):
    input_txt=driver.find_element(By.CSS_SELECTOR,'div >form >input.form-control')
    input_txt.send_keys(key, Keys.ENTER)


def next(key):
    for i in range(200):
        try:
            key_url='https://ithelp.ithome.com.tw/search?tab=article&search='+key+'&page='+str(i)
            # print(key_url)
            driver.get(key_url)
            # next_page=driver.find_element(By.CSS_SELECTOR,'div > div.text-center > ul > li:nth-child(4) > a')
            # next_page.click()
            sleep(1)

            links = driver.find_elements(By.CSS_SELECTOR,'body > div > div > div > div > div > div > div> h3 > a')
            for i in range(len(links)):
                url=links[i].get_attribute('href')
                alinks.append(url)
            if links == []:
                break
        except:
            break
            

def get_text():

    title=driver.find_element(By.CSS_SELECTOR,'body > div > div > div > div> div > div> div > h2').get_attribute('innerText')
    post=driver.find_element(By.CSS_SELECTOR,'body > div > div > div > div > div > div > div.qa-markdown > div > div').get_attribute('innerText').replace('\n','')
    inner_post={

        '文章標題':title,
        '文章內容':post,

    }
    results.append(inner_post)


if __name__ == '__main__':

    # key1 sunny 70
    # key2 noah 70
    # key3 mm 70
    # key4 xiong 70
    # key5 yen 70
    # key6 yuan 70
    # key7 kevin 80
    for i in range(20,len(key2)):  # 改這行 (0, 70) or 80
        key = key2[i]  # 改這行
        input_search(key)

        next(key)
        for j in range(len(alinks)):
            try:
                driver.get(alinks[j])
                sleep(1)
                get_text()
                # print(results)
            except:
                continue
        if results == []:
            print(str(i)+'.txt 空檔案 不存')
        else:
            with open(str(i)+'.txt', 'w', encoding='utf-8') as fp:
                for r in results:
                    fp.write("%s\n" % r)
                print(str(i)+'.txt 已存檔')
        results = []
        alinks = []

        driver.get('https://ithelp.ithome.com.tw/search?tab=article')
        sleep(2)