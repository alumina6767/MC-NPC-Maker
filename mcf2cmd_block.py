# -*- coding: utf-8 -*-
"""mcfunction をワールドで使えるコマンドブロック群に変換

Todo:
    * 15を超えるコマンドでの動作
    * レッドストーンダストの配置

"""

import pyperclip
from connect_commands import add_backslash, connect_commands


def mcf2cmd_block(file_paths):
    """
    .mcfunctionに書かれた複数行のコマンドをコマンドブロック群に変換する
    """

    set_cmds = []

    for dz,  fp in enumerate(file_paths):
        with open(fp, 'r', encoding='utf-8') as in_f:
            dx = 1
            for s in in_f:
                x = f'~{dx}'
                y = '~2' 
                z = f'~{2*dz}'

                if s[0] == '#':
                    # コメントのときは無視
                    continue
                elif s.strip() == '': 
                    # 空行のときはコマブロ無し
                    set_cmd = f"setblock {x} {y} {z} gray_terracotta"
                else:
                    s = s.strip()
                    # \の数を調整する めちゃややこい
                    com = add_backslash(s)

                    set_cmd = rf"setblock {x} {y} {z} command_block[facing=up]{{Command:\'{com}\',TrackOutput:0b}}"

                set_cmds.append(set_cmd)
                dx += 1

    return connect_commands(set_cmds)


if __name__ == '__main__':
    import glob

    IN_PATH = 'input/command'
    file_paths = glob.glob(IN_PATH + '/*.mcfunction')
    result = mcf2cmd_block(file_paths)
    print(result)
    print('クリップボードに結果をコピーしました。')
    pyperclip.copy(result)