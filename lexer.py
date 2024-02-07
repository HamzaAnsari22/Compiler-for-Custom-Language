import sys
import re
import tokens
import collections
from word2number import w2n
Token = collections.namedtuple('Token', ['type','value'])

def open_file(filename):
    data = open(filename, "r").read()
    return data

def lex(data):
    data = data.split('\n')
    tokenized = []
    for i in range(len(data)-1):
        tokenized.append(lexify(data[i], (i+1)))

    token_list = []
    for line in tokenized:
        if line != []:
            token_line = []
            line.pop()
            for pair in line:
                token_line.append(Token(pair[1], pair[0]))
            token_list.append(token_line)
    return token_list

def lexify(data, line_num):
    data=data+' @'
    pos = 0
    token_list = []
    str = ''
    stri=''
    flag=False
    token_exprs = tokens.token_exprs
    while pos < len(data):
        match = None
        for i in range(len(token_exprs)-2):
            pattern, tag = token_exprs[i]
            regex = re.compile(pattern)
            match = regex.match(data, pos)
            if match:
                str = match.group(0)
                if tag:
                    try:
                        if w2n.word_to_num(str): 
                            stri=stri+" "+str
                            continue
                    except ValueError:
                        if stri=='':
                            token_list.append((str,tag))
                            break
                        else:
                            token_list.append((w2n.word_to_num(stri),'INT'))
                            token_list.append((str,tag))
                            stri=''
                            flag=True
                            break
                    if flag:
                        token_list.append((w2n.word_to_num(stri),'INT'))
                        stri=''
                        flag=False
                        break
                break
        if not match :
            print('Illegal character in line',line_num,'at position',pos,
                ':\n'+ data,'\n'+ ' '*(pos-1), '^')
            sys.exit()
        else:
            pos = match.end(0)
    return token_list

