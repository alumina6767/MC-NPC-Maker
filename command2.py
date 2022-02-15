#!/usr/bin/env python3
# tellraw 生成プログラム MOB用

# from _typeshed import WriteableBuffer
import json
import pyperclip

SELECTOR='@a[distance=..10]'

# print("ファイル名を入力してください")
# file_name = input()

def write_command(no):
    # out_file_name = r'command/' + file_name.split('.')[0] + '.mcfunction'
    no = str(no)
    out_file_name = r'command/' + no + '.mcfunction' 
    file_name = no + '.json'
    with open(file_name, mode='r') as f, open(out_file_name, mode='w') as out_f:
        d = json.load(f)

        execute = rf'execute at @e[type=villager,name="[{d["name"]}]",distance=0..,limit=1]'
        name_template = rf'''tellraw @a[distance=..10] ["",{{"text":"<","color":"{d["name_color"]}"}},{{"text":" {d["name"]} "}},{{"text":">","color":"{d["name_color"]}"}},'''

        result = ''
        

        for t in d["texts"]:
            body = t.strip(' 「」 ')
            if body != "":
                    
                tellraw = name_template + rf'''{{"text":"  {body}","color":"{d["text_color"]}"}}]'''
                result += execute + ' run ' + tellraw + '\n'

                # 一列が長いときは間隔を設ける
                if 25 < len(body):
                    result += ' \n'

        out_f.write(result) 
        pyperclip.copy(result)

for i in range():
    write_command(i)
