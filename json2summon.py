#!/usr/bin/env python3
# IN_PATHのJSONファイルすべてからsummonコマンドを作る

import json
import glob

def json2summon(file_path):
    with open(file_path, encoding="utf-8") as f:
        d = json.load(f)
        name = d['name']
        name_c = d['name_color'] 
        biome = d['biome']
        profession = d['profession']

        com = rf"summon villager ~ ~ ~ {{Invulnerable: 1b, NoAI: 1b, CustomName: '[{{\"text\":\"[\",\"color\":\"{name_c}\"}},{{\"text\":\"{name}\",\"color\":\"white\"}},{{\"text\":\"]\",\"color\":\"{name_c}\"}}]', VillagerData: {{profession: \"minecraft:{profession}\", type: \"minecraft:{biome}\"}}, Offers: {{}}}}".replace(r'\"', r'"')

    return com + '\n'

if __name__ == '__main__':
    # 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
    IN_PATH = 'input'
    for f in glob.glob(IN_PATH + '/*.json'):
        print(f)
        print(json2summon(f))