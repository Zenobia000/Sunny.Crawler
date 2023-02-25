import json

json_file = []  # 放所有檔名


def merge_JsonFiles(json_file):
    result = list()
    for f1 in json_file:
        with open(f1, 'r', encoding='utf-8') as infile:
            result.extend(json.load(infile))

    with open('job16_all.json', 'w', encoding='utf-8') as output_file:
        json.dump(result, output_file, ensure_ascii=False, indent=4)
        print("檔案寫好！")


merge_JsonFiles(json_file)
