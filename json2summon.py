#!/usr/bin/env python3
# IN_PATHのJSONファイルすべてからsummonコマンドを作る

import json
import glob

from messsage import print_warn

PROFESSION = ('none', 'armorer', 'butcher', 'cartographer', 'cleric', 'farmer', 'fisherman', 'fletcher',
              'leatherworker', 'librarian', 'mason', 'nitwit', 'shepherd', 'toolsmith', 'weaponsmith')
BIOME = ('desert', 'jungle', 'plains', 'savanna', 'snow', 'swamp', 'taiga')


def json2summon(json_data):
    name = json_data['name']
    name_c = json_data['name_color']

    # 役職の正当性を確認
    profession = json_data['profession'].lower()
    if profession == 'unemployed':
        profession = 'none'
    elif profession not in PROFESSION:
        print_warn(f'professionの指定{profession}という役職は存在しません。')

    # バイオームの正当性を確認
    biome = json_data['biome'].lower()
    if biome not in BIOME:
        print_warn(f'biome指定{biome}というバイオームは存在しません。')

    com = rf"summon villager ~ ~ ~ {{Silent:1b,Invulnerable:1b,NoAI:1b,CustomName:'[{{\"text\":\"[\",\"color\":\"{name_c}\"}},{{\"text\":\"{name}\",\"color\":\"white\"}},{{\"text\":\"]\",\"color\":\"{name_c}\"}}]', VillagerData:{{profession:\"minecraft:{profession}\",type:\"minecraft:{biome}\"}},Offers:{{}}}}".replace(
        r'\"', r'"')

    return com + '\n'


if __name__ == '__main__':
    # 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
    IN_PATH = 'input'
    for f in glob.glob(IN_PATH + '/*.json'):
        print(f)
        print(json2summon(f))
