from json2commands import def_scene_region, gen_etc_region, gen_ifs_region, gen_meta_region
from json2storage import get_ifs
from json2summon import json2summon
from json2tellraw import json2tellraw


def json2conversation(d):
    '''
    JSONから会話形式のコマンドを追加する
    '''

    # metaの生成
    meta_region = gen_meta_region(d)

    # summonの生成
    summons = []
    for speaker in d['speakers']:
        summons.append(json2summon(d['speakers'][speaker]))
    summon_region = gen_etc_region(summons)

    # 条件分岐のファイル指定がある時 ifsの生成
    if 'ifs' in d:
        ifs = get_ifs(d)
        ifs_region = gen_ifs_region(d['texts'].keys(), ifs)
    else:
        ifs_region = None

    # tellrawの生成
    tellraws = ""
    for scene in d['texts'].keys():
        for speaker in d['texts'][scene].keys():
            name = str(speaker).strip('0123456789')
            name_c = d['speakers'][name]['name_color']
            text_c = d['speakers'][name]['text_color']

            dd = {
                'texts': {
                    speaker: d['texts'][scene][speaker]
                },
                'name_color': name_c,
                'text_color': text_c,
                'name': name,
                'profession': d['speakers'][name]['profession'],
                'biome': d['speakers'][name]['biome']
            }

            tellraw = json2tellraw(dd)
            for key in tellraw:
                tellraws += '\n'.join(tellraw[key]) + '\n'

    result = ''
    result += meta_region
    result += summon_region
    if ifs_region:
        result += ifs_region + '\n'

    result += def_scene_region(tellraws)

    return result
