def read_blocks():
    res = []
    cur_block = []
    while True:
        try:
            line = input()
            if line == 'EXIT':
                if cur_block:
                    res.append(cur_block)
                return res
            if line == "":
                if cur_block:
                    res.append(cur_block)
                cur_block = []
                continue
            cur_block.append(line)
        except EOFError:
            if cur_block:
                res.append(cur_block)
            break
    return res


def get_pos_numbers_from_line(line):
    res = []
    cur = []
    for c in line:
        if c.isdigit():
            cur.append(c)
        elif cur:
            res.append(int("".join(cur)))
            cur = []
    if cur:
        res.append(int("".join(cur)))
    return res

def get_words_from_line(line):
    res = []
    cur = []
    for c in line:
        if c.isdigit() or c.isalpha():
            cur.append(c)
        elif cur:
            res.append("".join(cur))
            cur = []
    if cur:
        res.append("".join(cur))
    return res

def get_strict_words_from_line(line):
    res = []
    cur = []
    for c in line:
        if c.isalpha():
            cur.append(c)
        elif cur:
            res.append("".join(cur))
            cur = []
    if cur:
        res.append("".join(cur))
    return res