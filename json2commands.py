# JSONから色々なコマンドを作成する

import glob
import json
import os
from json2book import json2book
from json2button import json2button
from json2storage import json2storage
from json2summon import json2summon
from json2tellraw import json2tellraw

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


if __name__ == '__main__':
    for path in glob.glob(IN_PATH + '/*.json'):
        with open(path, mode='r', encoding="utf-8") as in_f:
            print(path + 'を読み込みました。')
            json_data = json.load(in_f)
            file_name = path.split('\\')[-1]

            summon = json2summon(path)
            tellraw = json2tellraw(json_data)
            button = json2button(json_data)

            # 本は著者とタイトルがあるときだけ作成
            if 'author' in json_data:
                book = json2book(path)
            else:
                book = False

            # 条件分岐のファイル指定がある時
            if 'ifs' in json_data:
                ifs = json2storage(json_data)

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
                if scene in ifs:
                    s += ifs[scene] + '\n'
                else:
                    s += '#条件分岐用のコマンドが見つかりませんでした。\n'
                    print(f'シーン{scene}の条件分岐用のコマンドが見つかりませんでいた。\n')
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
