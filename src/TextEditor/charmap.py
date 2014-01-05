'''
Created on Dec 31, 2013

@author: Justin
'''

from Game import *

char_INSERT = defaultdict(lambda :None)
char_INSERT.update({ \
        K_q:'q', \
        K_w:'w', \
        K_e:'e', \
        K_r:'r', \
        K_t:'t', \
        K_y:'y', \
        K_u:'u', \
        K_i:'i', \
        K_o:'o', \
        K_p:'p', \
        K_a:'a', \
        K_s:'s', \
        K_d:'d', \
        K_f:'f', \
        K_g:'g', \
        K_h:'h', \
        K_j:'j', \
        K_k:'k', \
        K_l:'l', \
        K_z:'z', \
        K_x:'x', \
        K_c:'c', \
        K_v:'v', \
        K_b:'b', \
        K_n:'n', \
        K_m:'m', \
        K_BACKQUOTE:'`', \
        K_1:'1', \
        K_2:'2', \
        K_3:'3', \
        K_4:'4', \
        K_5:'5', \
        K_6:'6', \
        K_7:'7', \
        K_8:'8', \
        K_9:'9', \
        K_0:'0', \
        K_MINUS:'-', \
        K_EQUALS:'=', \
        K_LEFTBRACKET:'[', \
        K_RIGHTBRACKET:']', \
        K_BACKSLASH:'\\', \
        K_SEMICOLON:';', \
        K_QUOTE:'\'', \
        K_COMMA:',', \
        K_PERIOD:'.', \
        K_SLASH:'/', \
        K_TAB:'\t', \
        K_RETURN:'\r', \
        K_SPACE:' ', \
        K_ESCAPE:go_normal, \
        K_BACKSPACE:cursor.delete_left
        })

shift_INSERT = defaultdict(lambda x:x)
shift_INSERT.update({
        'q':'Q', \
        'w':'W', \
        'e':'E', \
        'r':'R', \
        't':'T', \
        'y':'Y', \
        'u':'U', \
        'i':'I', \
        'o':'O', \
        'p':'P', \
        'a':'A', \
        's':'S', \
        'd':'D', \
        'f':'F', \
        'g':'G', \
        'h':'H', \
        'j':'J', \
        'k':'K', \
        'l':'L', \
        'z':'Z', \
        'x':'X', \
        'c':'C', \
        'v':'V', \
        'b':'B', \
        'n':'N', \
        'm':'M', \
        '`':'~', \
        '1':'!', \
        '2':'@', \
        '3':'#', \
        '4':'$', \
        '5':'%', \
        '6':'^', \
        '7':'&', \
        '8':'*', \
        '9':'(', \
        '0':')', \
        '-':'_', \
        '=':'+', \
        '[':'{', \
        ']':'}', \
        '\\':'|', \
        ';':':', \
        '\'':'"', \
        ',':'<', \
        '.':'>', \
        '/':'?', \
        '\t':'\t', \
        '\r':'\r', \
        ' ':' ', \
        })

char_NORMAL = defaultdict(lambda :None)
char_NORMAL.update({ \
        K_h:cursor.go_left, \
        K_k:cursor.go_right, \
        })

char_NORMAL.update({ \
        K_i:go_insert, \
        K_a:go_append, \
        })

shift_NORMAL = defaultdict(lambda x:x)

char_VISUAL = defaultdict(lambda :None)

shift_VISUAL = defaultdict(lambda x:x)

chr = (char_INSERT, char_NORMAL, char_VISUAL)

shift = (shift_INSERT, shift_NORMAL, shift_VISUAL)