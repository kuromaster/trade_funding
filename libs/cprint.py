from datetime import datetime as dt
from .vars import VarsInMemory

class bcolors:
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    GRAY = '\033[90m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    ENDC2 = '\x1b[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    # BG - Background
    BG_GRAY = '\x1b[30;40m'
    BG_RED = '\x1b[30;41m'
    BG_GREEN = '\x1b[30;42m'
    BG_YELLOW = '\x1b[30;43m'
    BG_BLUE = '\x1b[30;44m'
    BG_PURPLE = '\x1b[30;45m'
    BG_CYAN = '\x1b[30;46m'
    BG_WHITE = '\x1b[30;47m'
    # BBG - Bright Background
    BBG_GRAY = '\x1b[6;30;40m'
    BBG_RED = '\x1b[6;30;41m'
    BBG_GREEN = '\x1b[6;30;42m'
    BBG_YELLOW = '\x1b[6;30;43m'
    BBG_BLUE = '\x1b[6;30;44m'
    BBG_PURPLE = '\x1b[6;30;45m'
    BBG_CYAN = '\x1b[6;30;46m'
    BBG_WHITE = '\x1b[6;30;47m'

# print(bcolors.CYAN +''+ bcolors.ENDC)

def cprint(status, text):
    if VarsInMemory.debug_on_cprint:
        data = dt.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        if status == 'GREEN':
            print(bcolors.GREEN +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'YELLOW':
            print(bcolors.YELLOW +'[W] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'HEADER':
            print(bcolors.GREEN +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'RED':
            print(bcolors.RED +'[E] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'BLUE':
            print(bcolors.BLUE +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'PURPLE':
            print(bcolors.PURPLE +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'CYAN':
            print(bcolors.CYAN +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'BOLD':
            print(bcolors.BOLD +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'UNDERLINE':
            print(bcolors.UNDERLINE +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'WHITE':
            print(bcolors.ENDC +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'BBG_GRAY':
            print(bcolors.BBG_GRAY +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'BBG_BLUE':
            print(bcolors.BBG_BLUE +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'GRAY':
            print(bcolors.GRAY +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
        if status == 'BBG_YELLOW':
            print(bcolors.BBG_YELLOW +'[I] [{}] {}'.format(data,text) + bcolors.ENDC)
