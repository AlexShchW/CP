def res_for_s(s):
    res = 0
    i = 0
    while i + 3 < len(s):
        if s[i : i + 4] != 'mul(':
            i += 1
            continue
        a = []
        a_idx = i + 4
        while s[a_idx].isdigit():
            a.append(s[a_idx])
            a_idx += 1
        if s[a_idx] != ',':
            i = a_idx
            continue
        b = []
        b_idx = a_idx + 1
        while s[b_idx].isdigit():
            b.append(s[b_idx])
            b_idx += 1
        if s[b_idx] != ')':
            i = b_idx
            continue
        res += int(''.join(a)) * int(''.join(b))
        i = b_idx + 1
    return res

s = []
while True:
    try:
        ss = input()
        s.append(ss)
    except EOFError:
        break

res = res_for_s(''.join(s))
print(res)