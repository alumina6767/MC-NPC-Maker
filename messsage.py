def print_error(s):
    ''' 色付きエラー表示を行う '''
    return print('\033[31m[ERROR] ' + s + '\033[0m')

def print_warn(s):
    ''' 色付き警告表示を行う '''
    return print('\033[31m[WARN] ' + s + '\033[0m')