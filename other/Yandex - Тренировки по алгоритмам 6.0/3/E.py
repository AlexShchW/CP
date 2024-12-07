s = input()
N = len(s)

good = set()
for digit in range(10):
    good.add(str(digit))
good.update(['+', '-', '*', ')', '(', ' '])

def get_priority(el):
    if el == '+' or el == '-':
        return 1
    if el == '*':
        return 2
    return -1

def get_res():
    opened = 0
    for el in s:
        if el not in good:
            return 'WRONG'
        if el == ')':
            if not opened:
                return 'WRONG'
            opened -= 1
        if el == '(':
            opened += 1
    if opened:
        return 'WRONG'
    signs = set(['+', '*', '-'])
    space_idx = 0
    while space_idx < N:
        while space_idx < N and s[space_idx] != ' ':
            space_idx += 1
        if space_idx == N:
            break 
        l, r = space_idx, space_idx
        while l >= 0 and s[l] == ' ':
            l -= 1
        while r < N and s[r] == ' ':
            r += 1
        if l >= 0 and r < N:
            if s[l].isdigit() and s[r].isdigit():
                return 'WRONG'
            if s[l] in signs and s[r] in signs:
                return 'WRONG'
        space_idx = r 
    arr = []
    for i, el in enumerate(s):
        if el == ' ':
            continue 
        arr.append(el)
    arr_with_actual_numbers = [] 
    cur = None
    for i, el in enumerate(arr):
        if el.isdigit():
            if cur is None:
                cur = int(el)
            else:
                cur *= 10
                cur += int(el)
            continue
        if cur is not None:
            arr_with_actual_numbers.append(cur)
            cur = None
        if el in signs:
            if (i == 0 and el != '-') or arr[i - 1] in signs or (arr[i - 1] == '(' and el != '-'):
                return 'WRONG'
            if i == len(arr) - 1 or arr[i + 1] in signs or arr[i + 1] == ')':
                return 'WRONG'
            arr_with_actual_numbers.append(el)
            continue 
        arr_with_actual_numbers.append(el)
    if cur is not None:
        arr_with_actual_numbers.append(cur)
    
    fixed_arr = []
    for i, el in enumerate(arr_with_actual_numbers):
        if el == '-':
            if i == 0 or arr_with_actual_numbers[i - 1] == '(':
                fixed_arr.append(0)
        fixed_arr.append(el)

    arr_with_actual_numbers = fixed_arr
    #print(''.join([str(el) for el in fixed_arr]))
    postfix_result_stack = []
    postfix_service_stack = []
    for el in arr_with_actual_numbers:
        if str(el).isdigit():
            postfix_result_stack.append(el)
            continue
        if el == '(':
            postfix_service_stack.append(el)
            continue
        if el == ')':
            while postfix_service_stack[-1] != '(':
                postfix_result_stack.append(postfix_service_stack.pop())
            postfix_service_stack.pop()
            continue
        while postfix_service_stack and get_priority(el) <= get_priority(postfix_service_stack[-1]):
            postfix_result_stack.append(postfix_service_stack.pop())
        postfix_service_stack.append(el)
    while postfix_service_stack:
        postfix_result_stack.append(postfix_service_stack.pop())
    # print(postfix_result_stack)
    res = []
    for el in postfix_result_stack:
        if str(el).isdigit():
            res.append(el)
            continue
        b = res.pop()
        a = res.pop()
        if el == '+':
            res.append(a + b)
        elif el == '-':
            res.append(a - b)
        elif el == '*':
            res.append(a * b)
    # print(res)
    if not res:
        return 'WRONG'
    return res[0]

print(get_res())
