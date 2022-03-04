""" 
リストで与えられたコマンドを連結する
"""

import re


def add_backslash(s, now):
    """バックスラッシュを追加する
    シングルクォーテーションでコマンドを囲むので、\nとか\'の数を調整する必要がある。
    """

    # '単一の場合\を追加する
    s = re.sub(r"(?<=[^\\])'", r"\\'", s)
    bs_count = now        # コマンド中にある連続バックスラッシュ
    bs_add = [1, 3]     # 元の数に対して増やすバックスラッシュ数
    if now == 0:
        bs_add = [0] + bs_add

    # 最大bs連続数をカウント
    while '\\' * bs_count in s:
        bs_add.append(bs_add[bs_count]*2+bs_count+1)
        bs_count += 1

    # bsの追加 特定のbs連続文字を指定の連続数に置き換え
    for i in range(bs_count-1, 0, -1):
        s = re.sub(rf"(?<=[^\\])\\{{{i}}}(?=[^\\])", r'\\'*bs_add[i], s)

    if now == 1:
        if '\"' not in s and '\'' not in s:
            s = '\\\'' + s + '\\\''
        else:
            s = '\\\'' + s + '\\\''

    return s


def connect_commands(commands):
    """ 
    リストで与えられたコマンドを連結する
    連結する際にシングルクォーテーションで囲むので、そのへんの処理が必要
    """

    BASE = \
        r'summon falling_block ~ ~1 ~ {Time:1,BlockState:{Name:redstone_block},Passengers:[' + \
        r'{id:armor_stand,Health:0,Passengers:[' + \
        r'{id:falling_block,Time:1,BlockState:{Name:activator_rail},Passengers:['

    KILL = \
        r'''{id:command_block_minecart,Command:'setblock ~ ~1 ~ command_block{auto:1,Command:"fill ~ ~ ~ ~ ~-2 ~ air"}'},''' + \
        r'''{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}'''

    # コマンドの連結。コマンドブロックの文字数に気をつけないとだめ 大きすぎるとサーバーに蹴られる
    CHAR_LIM = 32500 - len(BASE) - len(KILL) - 1000
    results = [""]
    now_char = 0

    for cmd in (rf"{{id:command_block_minecart,Command:'{c}'}}," for c in commands):
        now_char += len(cmd)

        if CHAR_LIM < now_char:
            results.append("")
            now_char = len(cmd)

        results[-1] += cmd

    results = [BASE + r + KILL for r in results]

    return results
