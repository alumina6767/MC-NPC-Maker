'''
 mcfunction のコマンド群をストーレージに保存する
'''

import glob
import os
from connect_commands import add_backslash, connect_commands
from json2storage import tellraw2storage

# 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
IN_PATH = '分岐ありの整形済みmcf'


def get_initial(ifs, ID):
    '''
    data modify storage event:test tmp set value [{"if":'help',"then":'say end'},{"if":'execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] run clear @p oak_button 0',"then":'data modify storage event:test tmp set from storage event:test scene1'}]
    '''
    load_cmd = f"data modify storage event:{ID} tmp set from storage event:{ID}" + ' ' + 'scene{}'
    value = [
        f'{{\"if\":\'{ifs[key]}\',\"then\":\'{load_cmd.format(n+1)}\'}}' for n, key in enumerate(ifs)]
    result = f"data modify storage event:{ID} tmp set value [{','.join(value[::-1])}]"
    return result.replace('\'', '\\\\\'')


def mcf2set(cmds, ifs):
    initial = get_initial(ifs, cmds['ID'])
    dx = 0
    dy = 2
    dz = 0
    ID = cmds['ID']

    set1 = [
        f'setblock ~{dx+1} ~{dy} ~{dz} red_stained_glass',
        f'setblock ~{dx} ~{dy} ~{dz} command_block[facing=up]{{Command:\"setblock ~1 ~ ~ red_stained_glass\",TrackOutput:0b}}',
        f'setblock ~{dx} ~{dy+1} ~{dz} chain_command_block[facing=up]{{Command:\'{initial}\',auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx} ~{dy+2} ~{dz} chain_command_block[facing=east]{{Command:\"setblock ~2 ~-2 ~ redstone_block\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+1} ~{dy+2} ~{dz} chain_command_block[facing=east]{{Command:\"fill ~1 ~-1 ~ ~1 ~2 ~ air\",auto:1b,TrackOutput:0b}}'
    ]

    set2 = [
        f'setblock ~{dx+2} ~{dy} ~{dz} red_stained_glass',
        f'setblock ~{dx+3} ~{dy} ~{dz} command_block[facing=east]{{Command:\"setblock ~-1 ~ ~ air\",TrackOutput:0b}}',
        f'setblock ~{dx+4} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"data modify block ~3 ~ ~ Command set from storage event:{ID} tmp[-1].if\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+5} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"data modify block ~4 ~1 ~ Command set from storage event:{ID} tmp[-1].then\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+6} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"data remove storage event:{ID} tmp[-1]\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+7} ~{dy} ~{dz} chain_command_block[facing=east]{{auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+8} ~{dy} ~{dz} chain_command_block[conditional=true,facing=east]{{Command:\"setblock ~1 ~ ~ chain_command_block[facing=up]\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+9} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"setblock ~ ~ ~ chain_command_block[facing=east]\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+10} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"setblock ~-8 ~ ~ redstone_block\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+11} ~{dy} ~{dz} chain_command_block[facing=east]{{Command:\"say noo\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+9} ~{dy+1} ~{dz} chain_command_block[facing=west]{{auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+8} ~{dy+1} ~{dz} chain_command_block[facing=west]{{Command:\"setblock ~-6 ~ ~ redstone_block\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+7} ~{dy+1} ~{dz} chain_command_block[facing=west]{{Command:\"setblock ~-5 ~-1 ~ red_stained_glass\",auto:1b,TrackOutput:0b}}'
    ]

    set3 = [
        f'setblock ~{dx+3} ~{dy+1} ~{dz} comparator[facing=west]',
        f'setblock ~{dx+4} ~{dy+1} ~{dz} iron_block',
        f'setblock ~{dx+5} ~{dy+1} ~{dz} iron_block',
        f'setblock ~{dx+4} ~{dy+2} ~{dz} redstone_wire[east=side,west=side]',
        f'setblock ~{dx+5} ~{dy+2} ~{dz} redstone_wire[east=side,west=side]',
        f'setblock ~{dx+6} ~{dy+1} ~{dz} command_block[facing=up]{{Command:\"fill ~-4 ~2 ~ ~-4 ~ ~ air\",TrackOutput:0b}}',
        f'setblock ~{dx+6} ~{dy+2} ~{dz} chain_command_block[facing=east]{{Command:\"data modify block ~4 ~-1 ~ Command set from storage event:{ID} tmp[-1]\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+7} ~{dy+2} ~{dz} chain_command_block[facing=east]{{Command:\"data remove storage event:{ID} tmp[-1]\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+8} ~{dy+2} ~{dz} chain_command_block[conditional=true,facing=east]{{Command:\"setblock ~2 ~ ~ redstone_block\",auto:1b,TrackOutput:0b}}',
    ]

    set4 = [
        f'setblock ~{dx+10} ~{dy+2} ~{dz} red_stained_glass',
        f'setblock ~{dx+10} ~{dy+1} ~{dz} command_block[facing=east]{{TrackOutput:0b}}',
        f'setblock ~{dx+11} ~{dy+1} ~{dz} chain_command_block[facing=east]{{Command:\"setblock ~-1 ~1 ~ red_stained_glass\",auto:1b,TrackOutput:0b}}',
        f'setblock ~{dx+11} ~{dy+2} ~{dz} structure_block[mode=load]{{integrity:1.0f,mode:"LOAD",name:"event:timer",posX:-9,posY:-1,posZ:0,showboundingbox:0b,sizeX:2,sizeY:3,sizeZ:1}}'
    ]

    return set1 + set2 + set3 + set4


def get_ifs(file):
    is_if = False
    ifs = {}
    for l in file:
        if l[:7] == '## !if=':
            # 区切りのコメント
            scene = l[7:].strip()
            is_if = True

        elif l != '' and is_if:
            # コマンドを追加
            ifs[scene] = l
            is_if = False

    return ifs


def mcf2storage(file):
    '''
    mcfunction から storage用のコマンドを作る
    #region [meta]
    ## !ID=hogehoge
    #endregion

    #region [if]
    ## !if=シーン１
    条件用コマンド
    ## !if=シーン２
    #endregion

    #region [scene]
    ## !scene=シーン１
    実際に実行するコマンド
    空行は遅延
    ## !scene=シーン２
    の繰り返しから読みこむ
    #endregion
    '''

    d = {}

    scene = ""
    blank = 0

    for l in file:
        if l[0:7] == '## !ID=':
            # IDの保存
            ID = l[7:].strip()
            d['ID'] = ID
            blank = 0

        elif l[0:10] == '## !scene=':
            # 区切りのコメント
            scene = l[10:].strip()
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

            file_name = path.split('\\')[-1]

            lines = [l.strip() for l in in_f]
            cmds = mcf2storage(lines)
            ifs = get_ifs(lines)

            if 'ID' not in cmds:
                print(f'[WARNING] IDのないファイルをスキップします: {path}')
                continue

            sets = mcf2set(cmds, ifs)

            # ID を消す
            ID = cmds.pop('ID')

            # バックスラッシュを追加する
            for key in cmds:
                cmds[key] = [add_backslash(c, 0) for c in cmds[key]]

            storage_then = tellraw2storage(cmds, ID)

        # 出力ディレクトリの用意
        out_dir = 'ストレージ利用のコマンド出力先'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
            print(f'フォルダ {out_dir}を作成しました。')

        out_file = f'{out_dir}/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            s = []
            s += connect_commands([storage_then[key].replace('\'', '\\\'')
                                  for key in storage_then] + [add_backslash(set, 0) for set in sets])
            of.write('\n'.join(s))
            print(f'{out_file}に出力しました。')
