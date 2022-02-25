
from connect_commands import add_backslash


def tellraw2storage(tellraw, ID):
    """
    tellrawをストレージに変換する
    """

    all_results = {}
    is_end_row = True
    for n, scene in enumerate(tellraw):
        cmds = []

        # テキスト表示のコマンド
        for cmd in tellraw[scene]:
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

            cmds.append('\'' + add_backslash(cmd, 0) +'\'' )

        all_results[scene] = f"data modify storage event:{ID} scene{n+1} set value [{','.join(cmds[-1::-1])}]"
    return all_results


def json2storage(json_data):
    ifs_f = json_data['ifs']
    d = {}

    with open(ifs_f, mode='r', encoding="utf-8") as ifs:
        for l in ifs:
            l = l.strip()
            if l == "":
                continue
            elif l[0:3] == '# !':
                scene = l[3:]
            else :
                d[scene] = l
    return d
