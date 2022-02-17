""" 
リストで与えられたコマンドを連結する
"""

import re

def add_backslash(s):
    """バックスラッシュを追加する
    シングルクォーテーションでコマンドを囲むので、\nとか\'の数を調整する必要がある。
    """

    # '単一の場合\を追加する
    s = re.sub(r"(?<=[^\\])'", r"\\'", s)
    bs_count = 1        # コマンド中にある連続バックスラッシュ
    bs_add = [1, 3]     # 元の数に対して増やすバックスラッシュ数

    # 最大bs連続数をカウント
    while '\\' * bs_count in s:
        bs_add.append(bs_add[bs_count]*2+bs_count+1) 
        bs_count += 1

    # bsの追加 特定のbs連続文字を指定の連続数に置き換え
    for i in range(bs_count-1, 0, -1):
        s = re.sub(rf"(?<=[^\\])\\{{{i}}}(?=[^\\])", r'\\'*bs_add[i], s)

    return s


def connect_commands(merges):
    """ 
    リストで与えられたコマンドを連結する
    連結する際にシングルクォーテーションで囲むので、そのへんの処理が必要
    """
 
    BASE = r'summon falling_block ~ ~1 ~ {BlockState:{Name:activator_rail},Time:1,'
    KILL = r'kill @e[type=command_block_minecart,distance=..3]'

    # summonコマンドの生成
    result = BASE + r'Passengers:[{id:"command_block_minecart",' * len(merges)

    # killコマンドの追加
    result += r'Passengers:[{id:"command_block_minecart",' + rf'Command:"{KILL}"}}],'

    # mergeコマンドの追加
    for m in merges:
        mm = m.strip()
        result +=  rf"Command:'{mm}'}}],"
    result = result.rstrip(',')
    result += '}'
    result += '\n\n\n'

    return result



