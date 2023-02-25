import os
import re
import json

jobNum = input('請輸入編號(ex:經營/人資類，輸入 1)：')
jobJson = input('輸入職業類別編號前4碼：')
# 要讀取的json檔案位置
dirpath = r'C:\Users\student\Desktop\104網路爬蟲\9.資材／物流／運輸類'
pathfile = os.listdir(dirpath)
r = re.compile("^"+jobJson)
json_file = list(filter(r.match, pathfile))
print(len(json_file))


def merge_JsonFiles(json_file):
    count = 0
    result = list()
    for f1 in json_file:
        print(f1)
        print(dirpath + "\\" + f1)
        with open(dirpath + "\\" + f1, 'r', encoding='utf-8') as infile:
            x = json.load(infile)
            if len(x) <= 0:
                continue
            result.extend(x)
            # result.extend(json.load(infile))
            count += len(x)

    with open('job' + jobNum + '_all.json', 'w', encoding='utf-8') as output_file:
        json.dump(result, output_file, ensure_ascii=False, indent=4)
        print("檔案寫好！")
        print(count)


merge_JsonFiles(json_file)
