import re


DIGIT = 'D'
ENGLISH = 'E'
pnum = re.compile(rf'[１２３４５６７８９０\d]+')
peng = re.compile(rf'[a-zA-Z]+')
p_pairpuc = re.compile(r'''
    (?P<p_pairpuc>
    【[\w\s\d]+】
    |〖[\w\s\d]+〗
    |〈[\w\s\d]+〉
    |＜[\w\s\d]+＞
    |<[\w\s\d]+>
    |〔[\w\s\d]+〕
    |﹝[\w\s\d]+﹞
    |［[\w\s\d]+］
    |\[[\w\s\d]+\]
    |（[\w\s\d]+）
    |\([\w\s\d]+\)
    |\{[\w\s\d]+\}
    )''', re.UNICODE | re.VERBOSE)  # 标准对


def readtext_raw(file, m=0, encoding='utf-8'):
    data = []
    n = 0
    with open(file, 'r', encoding=encoding) as f:
        for line in f.readlines():
            line = line.strip()
            data.append(line)
            n += 1
            if n > m and m != 0:
                break
    return data


def readtext_clean(file, repeng=True, repnum=True):
    data = []
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            if repeng:
                line = peng.sub(ENGLISH, line)
            if repnum:
                line = pnum.sub(DIGIT, line)
            line = line.replace(" ", "")
            line = line.replace("　　", "")
            line = line.replace(u"\u3000", "")
            line = line.replace("\"", "“")
            line = line.replace("”", "“")
            line = line.replace("……", "…")
            line = p_pairpuc.sub("", line)
            if len(line) == 0:
                continue
            data.append(line)
    return data
