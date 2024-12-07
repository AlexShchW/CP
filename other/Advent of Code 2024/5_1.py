import collections

needs = collections.defaultdict(set)

def get_res(arr):
    s_arr = set(arr)
    processed = set()
    for el in arr:
        for prerequisite in needs[el]:
            if prerequisite not in s_arr:
                continue
            if prerequisite not in processed:
                return 0
        processed.add(el)
    return arr[len(arr) // 2]

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