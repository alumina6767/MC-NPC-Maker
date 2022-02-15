#!/usr/bin/env python3
# tellraw 生成プログラム
# IN_PATH内のJSONファイルをすべてcommandフォルダのmcfunctionに変換する

import json
import glob

# 設定
# 話す人 (From) デフォルトでは村人の特定の名前を持つやつ
# 話す人を探すセレクタ nameはJSONから取ってくるのでいじらん方がいい
F_SELECTOR = r'@e[type=villager, name="[NAME]", distance=0.., limit=1]' 

# 聞く人 (To)
# 聞こえる人を探すセレクタ 
T_SELECTOR = r'@a[distance=..10]'

# 名前の表示形式
T_NAME = r'{"text":"<","color":"NAME_COLOR"}, {"text":" NAME "}, {"text":">  ","color":"NAME_COLOR"}'

# これ以上長い一文だと遅延を入れる
# ある文字数以上の行は改行する 改行したところはコマブロを1つおかないようにすると次の分まで遅延させれる
S_LIM = 25


# この下は触らない
def json2tellraw(file_path):
    global F_SELECTOR, T_SELECTOR, T_NAME, S_LIM, IN_PATH

    with open(IN_PATH +'/'+file_path, mode='r', encoding="utf-8") as in_f:
        d = json.load(in_f)

        execute = ' '.join(['execute at', F_SELECTOR.replace("NAME", d["name"])])

        T_NAME = T_NAME.replace("NAME_COLOR", d["name_color"]).replace("NAME", d["name"])
        name_template = ' '.join(['tellraw', T_SELECTOR, r'["",', T_NAME, ','])

        result = ''
        
        for scene in d["texts"].keys():
            # シーン名
            result += f'## {scene}' + '\n'
            for t in d["texts"][scene]:
                body = t.strip('「」')
                if body != "":
                    tellraw = name_template + r'{"text":"body","color":"t_color"}]'.replace("body", body).replace("t_color", d["text_color"])
                    result += ' '.join([execute, 'run', tellraw]) + '\n'

                    # 一列が長いときは間隔を設ける
                    if S_LIM < len(body):
                        result += ' \n'

        # out_f.write(result)
        return result

if __name__ == "__main__":
    # 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
    IN_PATH = 'input'

    for f in glob.glob(IN_PATH + '/*.json'):
        ff = f.split('\\')[-1]
        print(ff)
        print(json2tellraw(ff))
