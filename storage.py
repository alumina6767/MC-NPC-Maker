# -*- coding: utf-8 -*-
"""mcfunction をワールドで使えるコマンドブロック群に変換


"""

from operator import is_
from tkinter.tix import Tree
import pyperclip
from connect_commands import add_backslash, connect_commands


def mcf2cmd_block(file_paths):
    """
    .mcfunctionに書かれた複数行のコマンドをコマンドブロック群に変換する
    """

    all_results = []
    for fp in file_paths:
        is_end_row = True
        cmds = []
        with open(fp, 'r', encoding='utf-8') as in_f:
            print(fp + 'を読み込みました。')
            for s in in_f:
                cmd = s.strip()
                # 末尾の空行を削除
                if is_end_row and cmd == "":
                    continue
                else :
                    is_end_row = False

                if cmd == "":
                    # 空行はダミーコマンドへ
                    cmd = "help"
                elif cmd[0] == '#':
                    # コメントは無視
                    continue

                cmds.append('\'' + cmd + '\'')

        all_results = f"data modify storage event:test scene1 set value [{','.join(cmds[-1::-1])}]"
    return all_results


if __name__ == '__main__':
    import glob

    IN_PATH = 'input2'
    file_paths = glob.glob(IN_PATH + '/*.mcfunction')
    all_results = mcf2cmd_block(file_paths)
    print(all_results)
    pyperclip.copy(all_results)
    # 出力ファイルへ保存
#    out_fp = 'output\\connected.mcfunction'
#    with open(out_fp, 'w', encoding='utf-8') as out_f:
#        out_f.write(''.join(['\n\n'.join(r) for r in all_results]))
#        print(out_fp + 'へ出力を行いました。')
    # print('クリップボードに結果をコピーしました。')
    # pyperclip.copy(result)