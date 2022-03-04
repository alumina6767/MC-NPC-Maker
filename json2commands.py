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
    keys = ('name', 'name_color', 'text_color', 'texts', 'ID', 'profession', 'biome')
    flag = True
    for k in keys:
        if k not in json_data:
            print_error(f'{k}の指定が存在しません。')
            flag = False

    return flag

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
            else :
                ifs = None

        # 出力ディレクトリの用意
        out_dir = 'command'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            print(f'フォルダ {out_dir}を作成しました。')

        out_file = out_dir + '/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            s = '#region [meta] プログラムが使用するメタデータゾーン\n'
            s += f'## !ID={json_data["ID"]}\n'
            s += '#endregion\n\n'

            s += '#region [etc] こまごまとしたコマンドゾーン (mcf2のプログラム類で処理されません)\n'
            s += '\n'.join(['## 召喚コマンド', summon])
            s += '#endregion\n\n'

            s += '#region [if] 条件分岐ゾーン (上から順に条件コマンドの結果が真なら該当のシーンのみが再生されます helpコマンドは常に真を表します)\n'
            for scene in json_data['texts']:
                s += '## !if=' + scene + '\n'
                if ifs and scene in ifs:
                    s += ifs[scene] + '\n'
                else:
                    s += '#条件分岐用のコマンドが見つかりませんでした。\n'
                    print_warn(f'scene{scene}の条件分岐用のコマンドが見つかりませんでした。\n')
            s += '#endregion\n\n'

            s += '#region [scene] 会話シーンコマンドゾーン\n'
            for scene in json_data['texts']:
                s += '## !scene=' + scene + '\n'
                s += '\n'.join(tellraw[scene]) + '\n'
                if book:
                    s += book[scene] + '\n'
                s += button + '\n'
            s += '#endregion\n\n'

            of.write(s)
            print(f'{out_file}に出力を行いました。')
