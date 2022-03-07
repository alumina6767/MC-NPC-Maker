# JSONから色々なコマンドを作成する

import glob
import json
import os
from json2book import json2book
from json2button import json2button
from json2storage import get_ifs
from json2summon import json2summon
from json2tellraw import json2tellraw
from messsage import print_error, print_warn

# 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
IN_PATH = 'input'


def get_initial(ifs, json_data):
    '''
    data modify storage event:test tmp set value [{"if":'help',"then":'say end'},{"if":'execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p oak_button 0',"then":'data modify storage event:test tmp set from storage event:test scene1'}]
    '''
    load_cmd = f"data modify storage event:{json_data['ID']} tmp set from storage event:{json_data['ID']}" + ' ' + 'scene{}'
    value = [
        f'{{\"if\":\'{ifs[key]}\',\"then\":\'{load_cmd.format(n+1)}\'}}' for n, key in enumerate(ifs)]
    result = f"data modify storage event:{json_data['ID']} tmp set value [{','.join(value[::-1])}]"
    return result


def check_json(json_data):
    keys = ('name', 'name_color', 'text_color',
            'texts', 'ID', 'profession', 'biome')
    flag = True
    for k in keys:
        if k not in json_data:
            print_error(f'{k}の指定が存在しません。')
            flag = False

    return flag


def gen_meta_region(json_data):
    s = '#region [meta] プログラムが使用するメタデータゾーン\n'
    s += f'## !ID={json_data["ID"]}\n'
    s += '#endregion\n\n'
    return s


def gen_etc_region(summons):
    s = '#region [etc] こまごまとしたコマンドゾーン (mcf2のプログラム類で処理されません)\n'
    for summon in summons:
        s += '\n'.join(['## 召喚コマンド', summon])
    s += '#endregion\n\n'
    return s


def gen_ifs_region(scenes, ifs):
    s = '#region [if] 条件分岐ゾーン (上から順に条件コマンドの結果が真なら該当のシーンのみが再生されます helpコマンドは常に真を表します)\n'
    for scene in scenes:
        s += '## !if=' + scene + '\n'
        if ifs and scene in ifs:
            s += ifs[scene] + '\n'
        else:
            s += '#条件分岐用のコマンドが見つかりませんでした。\n'
            print_warn(f'scene{scene}の条件分岐用のコマンドが見つかりませんでした。\n')
    s += '#endregion\n\n'
    return s


def gen_scene_region(scenes, tellraw, book):
    s = ''
    for scene in scenes:
        s += '## !scene=' + scene + '\n'
        s += '\n'.join(tellraw[scene]) + '\n'
        if book:
            s += book[scene] + '\n'
        if button:
            s += button + '\n'
    return s


def def_scene_region(s):
    return '#region [scene] 会話シーンコマンドゾーン\n' + s + '#endregion\n\n'


def json2conversation(d):
    '''
    JSONから会話形式のコマンドを追加する
    '''

    # metaの生成
    meta_region = gen_meta_region(d)

    # summonの生成
    summons = []
    for speaker in d['speakers']:
        summons.append(json2summon(d['speakers'][speaker]))
    summon_region = gen_etc_region(summons)

    # 条件分岐のファイル指定がある時 ifsの生成
    if 'ifs' in d:
        ifs = get_ifs(d)
    else:
        ifs = {}

    ifs_region = gen_ifs_region(d['texts'].keys(), ifs)

    # tellrawの生成
    tellraws = ""
    for scene in d['texts'].keys():
        # シーン名の挿入
        tellraws += '## !scene=' + scene + '\n'
        for speaker in d['texts'][scene].keys():
            name = str(speaker).strip('0123456789０１２３４５６７８９')
            if name not in d['speakers']:
                print_error(f'{name}の定義がspeakersに有りません。')
                exit()
            name_c = d['speakers'][name]['name_color']
            text_c = d['speakers'][name]['text_color']

            dd = {
                'texts': {
                    speaker: d['texts'][scene][speaker]
                },
                'name_color': name_c,
                'text_color': text_c,
                'name': name,
                'profession': d['speakers'][name]['profession'],
                'biome': d['speakers'][name]['biome']
            }

            # tellraws += f'### {speaker}\n'
            tellraw = json2tellraw(dd)
            for key in tellraw:
                tellraws += '\n'.join(tellraw[key]) + '\n'

    result = ''
    result += meta_region
    result += summon_region
    if ifs_region:
        result += ifs_region + '\n'

    result += def_scene_region(tellraws)

    return result


if __name__ == '__main__':
    for path in glob.glob(IN_PATH + '/*.json'):
        with open(path, mode='r', encoding="utf-8") as in_f:
            print(path + 'を読み込みました。')

            # JSONとして読み込み
            try:
                json_data = json.load(in_f)
            except json.JSONDecodeError as e:
                print(e)
                print_error('JSONの記述に誤りがあります。')
                exit()

            file_name = path.split('\\')[-1]

            if 'speakers' in json_data:
                print('会話形式のファイルとして認識しました。')
                s = json2conversation(json_data)

            else:
                # 要素が足りているかチェック
                if not check_json(json_data):
                    exit()

                # コマンドに変換
                summon = json2summon(json_data)
                tellraw = json2tellraw(json_data)
                button = json2button(json_data)

                # 本は著者とタイトルがあるときだけ作成
                if 'author' in json_data:
                    book = json2book(path)
                else:
                    book = None

                # 条件分岐のファイル指定がある時
                if 'ifs' in json_data:
                    ifs = get_ifs(json_data)
                else:
                    ifs = None

                s = gen_meta_region(json_data)
                s += gen_etc_region([summon])
                s += gen_ifs_region(json_data['texts'].keys(), ifs)
                s += def_scene_region(gen_scene_region(
                    json_data['texts'].keys(), tellraw, book))

        # 出力ディレクトリの用意
        out_dir = 'command'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            print(f'フォルダ {out_dir}を作成しました。')

        out_file = out_dir + '/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            of.write(s)
            print(f'{out_file}に出力を行いました。')
