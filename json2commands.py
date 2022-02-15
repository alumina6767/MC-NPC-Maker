# JSONから色々なコマンドを作成する

import glob
from json2book import json2book
from json2summon import json2summon
from json2tellraw import json2tellraw

# 入力ファイルがあるフォルダ フォルダ内のファイルをすべて処理する
IN_PATH = 'input'


if __name__ == '__main__':
    for path in glob.glob(IN_PATH + '/*.json'):
        file_name = path.split('\\')[-1]
        print(file_name)

        summon = json2summon(path)
        print(summon)

        tellraw = json2tellraw(file_name)
        print(tellraw)

        book = json2book(path)
        print(book)

        out_file = './command/' + file_name.split('.')[0] + '.mcfunction'
        with open(out_file, mode="w", encoding="utf-8") as of:
            of.write('\n'.join(['# 召喚コマンド', summon, '# 台詞', tellraw, '# 本', book]))