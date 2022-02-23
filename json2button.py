

def json2button(json_data):
    '''
    execute at @e[type=villager, name="[ムキムキのお兄さん]", distance=0.., limit=1] rotated ~ 0 run setblock ^ ^ ^1 acacia_button[face=floor]
    '''

    F_SELECTOR = '@e[type=villager, name=\"[NAME]\", distance=0.., limit=1]' 
    set_button = 'setblock ^ ^ ^1 acacia_button[face=floor]'
    execute = ' '.join(['execute at', F_SELECTOR.replace("NAME", json_data["name"]), 'rotated ~ 0'])
    cmd = ' '.join([execute, 'run', set_button])
    return cmd
