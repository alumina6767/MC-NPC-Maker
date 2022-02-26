import os
import pyperclip


def output2file(out_dir, out_file, s):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        print(f'フォルダ {out_dir}を作成しました。')

    out_file = f'{out_dir}/' + 'connected.mcfunction'
    with open(out_file, mode="w", encoding="utf-8") as of:

        of.write(s)
        print(f'{out_file}に出力しました。')

    return True


def output2clipboard(all_results):
    print(f'結果は{len(all_results)}個のコマンドになりました。')
    print('クリップボードに結果をコピーしますか？ [y or n]')
    if input().strip() == 'y':
        print('コマンド毎にクリップボードにコピーします。エンターを押すと次のコマンドをコピーします。')
        for i, result in enumerate(all_results):
            pyperclip.copy(result)
            print(f'クリップボードに{i+1}つ目のコマンドをコピーしました。')
            input()

    return True
