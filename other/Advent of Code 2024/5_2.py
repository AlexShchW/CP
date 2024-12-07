import collections

needs = collections.defaultdict(set)


def reorder_for_res(arr):
    s_arr = set(arr)
    candidates = []
    for el in s_arr:
        for prerequisite in needs[el]:
            if prerequisite in s_arr:
                break
        else:
            candidates.append(el)
    res = candidates
    we_have = set(res)
    while len(res) < len(s_arr):
        for el in arr:
            if el in we_have:
                continue
            for prerequisite in needs[el]:
                if prerequisite not in s_arr:
                    continue
                if prerequisite not in we_have:
                    break
            else:
                res.append(el)
                we_have.add(el)

    return res[len(res) // 2]

def get_res(arr):
    s_arr = set(arr)
    processed = set()
    for el in arr:
        for prerequisite in needs[el]:
            if prerequisite not in s_arr:
                continue
            if prerequisite not in processed:
                return reorder_for_res(arr)
        processed.add(el)
    return 0




res = 0

while True:
    try:
        input_line = input()
        if '|' in input_line:
            u, v = [int(el) for el in input_line.split('|')]
            needs[v].add(u)
        elif ',' in input_line:
            arr = [int(el) for el in input_line.split(',')]
            res += get_res(arr)
    except EOFError:
        break

print(res)