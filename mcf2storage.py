'''
 mcfunction のコマンド群をストーレージに保存する
'''

from doctest import IGNORE_EXCEPTION_DETAIL
import glob
import json
from connect_commands import add_backslash, connect_commands
from json2book import json2book
from json2button import json2button
from json2storage import json2storage, tellraw2storage
from json2summon import json2summon
from json2tellraw import json2tellraw

# 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
IN_PATH = 'command'


def get_initial(ifs, ID):
    '''
    data modify storage event:test tmp set value [{"if":'help',"then":'say end'},{"if":'execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p oak_button 0',"then":'data modify storage event:test tmp set from storage event:test scene1'}]
    '''
    load_cmd = f"data modify storage event:{ID} tmp set from storage event:{ID}" + ' ' + 'scene{}'
    value = [
        f'{{\"if\":\'{ifs[key]}\',\"then\":\'{load_cmd.format(n+1)}\'}}' for n, key in enumerate(ifs)]
    result = f"data modify storage event:{ID} tmp set value [{','.join(value[::-1])}]"
    return result


def mcf2storage(file):
    '''
    mcfunction から storage用のコマンドを作る
    # !ID=hogehoge
    # !シーン１
    1行目はif につかうコマンド
    2行目以降は実際に実行するコマンド
    空行は遅延

    # !シーン２
    の繰り返しから読みこむ
    '''

    d = {}

    scene = ""
    blank = 0

    for l in map(lambda l: l.strip(), file):

        if l[0:6] == '# !ID=':
            # IDの保存
            ID = l[6:].strip()
            d['ID'] = ID
            blank = 0

        elif l[0:3] == '# !':
            # 区切りのコメント
            scene = l[3:].strip()
            blank = 0

        elif l == '':
            # 空行の数を保持
            blank += 1

        elif scene != '':
            # それまでの空行分のコマンドとコマンドを追加
            if scene not in d:
                d[scene] = []
            d[scene] = d[scene] + ['help'] * blank + [l]
            blank = 0

    return d


if __name__ == '__main__':
    for path in glob.glob(IN_PATH + '/*.mcfunction'):
        with open(path, mode='r', encoding="utf-8") as in_f:
            print(f'{path}を読みこみました')

            # json_data = json.load(in_f)
            file_name = path.split('\\')[-1]
            # print(file_name)

            # summon = json2summon(path)
            # print(summon)

            # tellraw = json2tellraw(json_data)
            # print(tellraw)

            # book = json2book(path)
            # print(book)

            # button = json2button(json_data)
            # print(button)

            cmds = mcf2storage(in_f)

            if 'ID' not in cmds:
                print(f'[WARNING] IDのないファイルをスキップします: {path}')
                continue

            # ID を消す
            ID = cmds.pop('ID')
            print(cmds)
            # バックスラッシュを追加する
            for key in cmds:
                cmds[key] = [add_backslash(c, 0) for c in cmds[key]]
            ifs = {scene: cmds[scene][0] for scene in cmds}
            initial = get_initial(ifs, ID)
            storage_then = tellraw2storage(cmds, ID)
            # print(storage_then)

        out_file = './output3/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            # of.write('\n'.join(['# 召喚コマンド', summon, '# 台詞', tellraw, '# 本', book, '# storage', storage_then]))
            s = []
            for key in storage_then:
                s.append(storage_then[key])
                # s.append(json.dumps(storage_then[key], ensure_ascii=False))
            # of.write('\n'.join(connect_commands(s)))
            of.write('\n'.join(s))
            # of.write('\n'.join(connect_commands([add_backslash(c, 0) for c in [cmds[key] for key in cmds]])) + '\n' + initial)
