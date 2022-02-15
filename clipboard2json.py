#!/usr/bin/env python3
# クリップボードのプレーンテキストを改行とダブルクォーテーションで囲う

import pyperclip

def string_to_json(s):
    result = ',\n'.join(
        [r'"' + ss.strip() + r'"'for ss in s.split('\n') if ss.strip() != ""])
    return result

if __name__ == '__main__':
    result = string_to_json(pyperclip.paste())
    pyperclip.copy(result)
