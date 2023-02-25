import os
import re
import csv
import json

jobNum = input('請輸入編號(ex:經營/人資類，輸入 1)：')
jobCSV = input('輸入職業類別編號前4碼：')
dirpath = 'C:/Selenium/Mednium/4/'
pathfile = os.listdir(dirpath)
# print(f"pathfile = {pathfile}")
r = re.compile(rf"^"+jobCSV)
csvlist = list(filter(r.match, pathfile))
print(csvlist)
csv_file = []

for filepath in csvlist:
    for filename in os.listdir(filepath):
        csv_file.append(filename)

print(len(csv_file))

def merge_CSVFiles(csv_file):
    count=0
    skip_num = 0
    rows = 0
    result = list()
    csvresult = []
    for fp in csvlist:
        print("f2= " + fp)
        rg = re.compile("^"+fp)
        for f1 in list(filter(rg.match, csv_file)):
            print(dirpath+"\\"+ fp + "\\" +f1)
            if f1.endswith(".csv"):
                with open(dirpath+"\\"+ fp + "\\" +f1, 'r', encoding='utf-8') as infile:
                    reader = csv.reader(infile)
                    for row in reader:
                        if reader.line_num <= skip_num:
                            continue
                        csvresult.append(row)
                        rows += 1
                    skip_num = 1
            
            else:
                with open(dirpath+"\\"+ fp + "\\" +f1, 'r', encoding='utf-8') as infile:
                    x = json.load(infile)
                    if len(x)<=0:
                        continue
                    result.extend(x)
                    count+=len(x)
            
            
    with open('job' + jobNum + '_all.csv', 'w', newline="", encoding='utf-8') as output_file_csv:
        writer = csv.writer(output_file_csv)
        for row in csvresult:
            writer.writerow(row)
        print("csv檔案寫好！")
        print(rows)

    with open('job' + jobNum + '_all.json', 'w', encoding='utf-8') as output_file:
        json.dump(result, output_file, ensure_ascii=False, indent=4)
        print("json檔案寫好！")
        print(count)


merge_CSVFiles(csv_file)