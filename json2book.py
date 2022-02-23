#!/usr/bin/env python3

import json
import glob

# 一行の幅
WITH = 12

# 本１ページの行数
HEIGHT = 14

# 一度に渡す本の数
BOOK_COUNT = 5

def json2book(in_file_name):
    with open(in_file_name,mode='r', encoding="utf-8") as f:
        d = json.load(f)

        result = ''
        results = {}
        
        for scene in d["texts"].keys():
            # 本の初期化
            row = 0
            page = ''
            pages = []

            # results += rf'## {scene}' + '\n'
            for t in d["texts"][scene]:

                body = t.strip(' 「」 ')

                if body == "":
                    # 空行を無視
                    continue

                # 消費する行
                c_row = -1*(-1*len(body) // WITH)
                if HEIGHT < row + c_row:
                    # 改ページ
                    pages.append(page)
                    page = ''
                    row = 0

                # 文を追加    
                page += body

                if len(body) % WITH == 1:
                    # 句読点だけの行をなくす
                    page.rstrip('。、.,')

                page += r'\\n\\n'
                row += c_row + 1

            if row != 0:
                # pageが1の時の例外処理
                pages.append(page)

            # コマンドを生成
            result = r"pages:['"
            result += r"','".join([rf'{{"text":"{p}"}}' for p in pages])
            result += r"']," + rf'title:"{scene}",author:"{d["author"]}"'
            result = rf'execute at @e[type=villager,name="[{d["name"]}]",distance=0..,limit=1] run summon item ^ ^1.5 ^1 {{NoGravity:1b,Glowing:1b,PickupDelay:60,Motion:[0.0,-0.05,0.0],Item:{{id:"written_book",tag:{{{result}}},Count:{BOOK_COUNT}b}}}}'
            results[scene] = result

        return results
        
if __name__ == '__main__':
    IN_PATH = 'input'
    for f in glob.glob(IN_PATH + '/*.json'):
        print(f)
        print(json2book(f))
