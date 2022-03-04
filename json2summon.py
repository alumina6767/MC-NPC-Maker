#!/usr/bin/env python3
# IN_PATHのJSONファイルすべてからsummonコマンドを作る

import json
import glob

from messsage import print_error, print_warn

PROFESSION = ('none', 'armorer', 'butcher', 'cartographer', 'cleric', 'farmer', 'fisherman', 'fletcher',
              'leatherworker', 'librarian', 'mason', 'nitwit', 'shepherd', 'toolsmith', 'weaponsmith')
BIOME = ('desert', 'jungle', 'plains', 'savanna', 'snow', 'swamp', 'taiga')


def json2summon(file_path):
    with open(file_path, encoding="utf-8") as f:
        d = json.load(f)

        keys = ('name', 'name_color', 'profession', 'biome')
        for k in keys:
            if k not in d:
                print_error(f'{file_path}に{k}の指定が存在しません。')
                exit()

        name = d['name']
        name_c = d['name_color']

        # 役職の正当性を確認
        profession = d['profession'].lower()
        if profession == 'unemployed':
            profession = 'none'
        elif profession not in PROFESSION:
            print_warn(f'{file_path}のprofessionの指定{profession}という役職は存在しません。')

        # バイオームの正当性を確認
        biome = d['biome'].lower()
        if biome not in BIOME:
            print_warn(f'{file_path}のbiome指定{biome}というバイオームは存在しません。')

        com = rf"summon villager ~ ~ ~ {{Invulnerable: 1b, NoAI: 1b, CustomName: '[{{\"text\":\"[\",\"color\":\"{name_c}\"}},{{\"text\":\"{name}\",\"color\":\"white\"}},{{\"text\":\"]\",\"color\":\"{name_c}\"}}]', VillagerData: {{profession: \"minecraft:{profession}\", type: \"minecraft:{biome}\"}}, Offers: {{}}}}".replace(
            r'\"', r'"')

    return com + '\n'


if __name__ == '__main__':
    # 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
    IN_PATH = 'input'
    for f in glob.glob(IN_PATH + '/*.json'):
        print(f)
        print(json2summon(f))
