res = 0

def get_res(line):
    target = []
    for i, el in enumerate(line):
        if el == ':':
            idx = i
            break
        target.append(el)
    target = ''.join(target)
    target = int(target)

    equation = line[idx + 1:].split()
    equation = [int(el) for el in equation]
    
    def go(cur, idx):
        if idx == len(equation):
            if cur == target:
                return True
            return False
        
        return go(cur + equation[idx], idx + 1) or go(cur * equation[idx], idx + 1) or go(int(str(cur) + str(equation[idx])), idx + 1)
    
    bool_res = go(equation[0], 1)
    if bool_res:
        return target
    return 0

while True:
    try:
        line = input()
        if not line:
            break
        res += get_res(line)
    except EOFError:
        break

print(res)