# JSONから色々なコマンドを作成する

from doctest import IGNORE_EXCEPTION_DETAIL
import glob
import json
import os
from connect_commands import add_backslash, connect_commands
from json2book import json2book
from json2button import json2button
from json2storage import json2storage, tellraw2storage
from json2summon import json2summon
from json2tellraw import json2tellraw

# 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
IN_PATH = 'input'

def get_initial(ifs,json_data):
    '''
    data modify storage event:test tmp set value [{"if":'help',"then":'say end'},{"if":'execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p oak_button 0',"then":'data modify storage event:test tmp set from storage event:test scene1'}]
    '''
    load_cmd = f"data modify storage event:{json_data['ID']} tmp set from storage event:{json_data['ID']}" + ' ' + 'scene{}'
    value = [f'{{\"if\":\'{ifs[key]}\',\"then\":\'{load_cmd.format(n+1)}\'}}' for n, key in enumerate(ifs)]
    result = f"data modify storage event:{json_data['ID']} tmp set value [{','.join(value[::-1])}]"
    return result


if __name__ == '__main__':
    for path in glob.glob(IN_PATH + '/*.json'):
        with open(path, mode='r', encoding="utf-8") as in_f:
            print(path + 'を読み込みました。')
            json_data = json.load(in_f)
            file_name = path.split('\\')[-1]
            #print(file_name)

            summon = json2summon(path)
            #print(summon)

            tellraw = json2tellraw(json_data)
            # print(tellraw)

            book = json2book(path)
            #print(book)

            button = json2button(json_data)
            # print(button)
            # 条件分岐のファイル指定がある時
            if 'ifs' in json_data:
                # print(json_data['ifs'])
                ifs = json2storage(json_data)
                initial = get_initial(ifs,json_data)
                # print(initial)
                # print(storage)
                # print(tellraw)
                storage_then = tellraw2storage(tellraw, json_data)
                # print(storage_then)
        
        out_dir = 'command'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            print(f'フォルダ {out_dir}を作成しました。')

        out_file = out_dir + '/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            s = ''
            s += '\n'.join(['# 召喚コマンド', summon])
            s += '\n'

            # s += '# 台詞\n'
            # for key in tellraw:
            #     s += '# !' + key + '\n'
            #     s += '\n'.join(tellraw[key]) + '\n'
            # s += '\n'
            s += f'# !ID={json_data["ID"]}\n'

            for scene in json_data['texts']:
                s += '# !scene=' + scene + '\n'
                s += '\n'.join(tellraw[scene]) + '\n'
                s += book[scene] + '\n'
                s += button + '\n'

            # of.write('\n'.join(['# 召喚コマンド', summon, '# 台詞', tellraw, '# 本', book, '# storage', storage_then]))
            # of.write('\n'.join(connect_commands([add_backslash(storage_then[key],0) for key in storage_then])) + '\n' + initial)
            of.write(s)
            print(f'{out_file}に出力を行いました。')