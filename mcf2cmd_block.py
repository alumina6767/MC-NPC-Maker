# -*- coding: utf-8 -*-
"""mcfunction をワールドで使えるコマンドブロック群に変換


"""

import pyperclip
from connect_commands import add_backslash, connect_commands

def mcf2list(file):
    D = []
    cmd = []
    is_scene_region = False
    for s in file:
        if not is_scene_region :
            if s[:15] == '#region [scene]':
                is_scene_region = True

        else:
            if s[:10] == '#endregion':
                break

            elif s[:10] == '## !scene=':
                D.append(cmd)
                cmd = []

            elif s[0] != '#':
                cmd.append(s)
    
    D.append(cmd)
    return D

def mcf2cmd_block(file_paths):
    """
    .mcfunctionに書かれた複数行のコマンドをコマンドブロック群に変換する
    """

    set_cmds = []
    dz = 0
    for fp in file_paths:
        with open(fp, 'r', encoding='utf-8') as in_f:
            print(fp + 'を読み込みました。')

            # 一度リストに変換
            D = mcf2list(in_f)
    
            # データについて処理
            for d in D:
                x = dx = 0
                end_x = 16
                y = 2
                z = 2*dz

                # 開始の機構
                set_cmd = [
                    f"setblock ~{x} ~{y+1} ~{z} comparator[facing=west]",
                    f'setblock ~{x+1} ~{y} ~{z} command_block{{Command:\"setblock ~-1 ~ ~1 red_stained_glass\",TrackOutput:0b}}',
                    f"setblock ~{x} ~{y} ~{z+1} red_stained_glass",
                    f'setblock ~{x-1} ~{y} ~{z+1} structure_block[mode=load]{{integrity:1.0f,mode:"LOAD",name:"minecraft:timer",posX:0,posY:1,posZ:-1,showboundingbox:1b,sizeX:1,sizeY:3,sizeZ:1}}',
                    f'setblock ~{x+15} ~{y-1} ~{z} command_block{{Command:\"fill ~-16 ~2 ~ ~-16 ~4 ~ air\",TrackOutput:0b}}']
                set_cmds += set_cmd
                dx += 2

                for s in d:
                    x = dx
                    set_cmd = []

                    if dx % 16 == 0:
                        # 赤石信号の限界で更新
                        set_cmd = [
                            f'setblock ~{x} ~{y} ~{z} structure_block[mode=load]{{integrity:1.0f,mode:"LOAD",name:"minecraft:timer",posX:0,posY:1,posZ:0,showboundingbox:1b,sizeX:1,sizeY:3,sizeZ:1}}',
                            f"setblock ~{x+1} ~{y+1} ~{z} comparator[facing=west]",
                            f'setblock ~{x+15} ~{y-1} ~{z} command_block{{Command:\"fill ~-15 ~2 ~ ~-15 ~4 ~ air\",TrackOutput:0b}}']
                        dx += 3
                        x += 3
                        end_x += 17

                    if s.strip() == '':
                        # 空行のときはコマブロ無し
                        dx += 1
                        continue

                    else:
                        s = s.strip()
                        # \の数を調整する めちゃややこい
                        cmd = add_backslash(s, 1)
                        set_cmd += [
                            f"setblock ~{x} ~{y} ~{z} command_block[facing=up]{{Command:{cmd},TrackOutput:0b}}"]

                    set_cmds += set_cmd
                    dx += 1

                # リピーター
                set_cmds += [f"setblock ~{dx} ~3 ~{dz*2} repeater[facing=west]"]
                # 塗りつぶし
                set_cmds += [
                    f"fill ~-1 ~2 ~{dz*2} ~{end_x} ~2 ~{dz*2+1} gray_terracotta replace air"]
                # 赤石
                set_cmds += [f"fill ~-1 ~3 ~{dz*2} ~{end_x} ~3 ~{dz*2} redstone_wire[east=side,power=0,west=side] replace air"]
                
                dz += 1
            
    return connect_commands(set_cmds)


if __name__ == '__main__':
    import glob

    IN_PATH = '分岐なし整形済みのmcf'
    file_paths = glob.glob(IN_PATH + '/*.mcfunction')
    all_results = mcf2cmd_block(file_paths)

    # 出力ファイルへ保存
    out_fp = 'output\\connected.mcfunction'
    with open(out_fp, 'w', encoding='utf-8') as out_f:
        out_f.write('\n\n'.join(all_results))
        print(out_fp + 'へ出力を行いました。')

    print(f'結果は{len(all_results)}個のコマンドになりました。')
    print('クリップボードに結果をコピーしますか？ [y or n]')
    if input().strip() == 'y':
        print('コマンド毎にクリップボードにコピーします。エンターを押すと次のコマンドをコピーします。')
        for i, result in enumerate(all_results):
            pyperclip.copy(result)
            print(f'クリップボードに{i+1}つ目のコマンドをコピーしました。')
            input()
