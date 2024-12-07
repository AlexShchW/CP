n = int(input())
w = input()
try:
    s = input()
except:
    s = ''

round_opened = [0]
square_opened = [0]

cur_res = list(s)
stack = []
for el in s:
    if el == '(':
        stack.append(el)
        round_opened[0] += 1
    if el == '[':
        stack.append(el)
        square_opened[0] += 1
    if el == ')':
        stack.pop()
        round_opened[0] -= 1
    if el == ']':
        stack.pop()
        square_opened[0] -= 1


def can_use(candidate):
    if candidate == '(':
        would_be_needed_to_close = round_opened[0] + square_opened[0] + 1
        if would_be_needed_to_close > n - (len(cur_res) + 1):
            return False
        round_opened[0] += 1
        stack.append(candidate)
        return True
    if candidate == '[':
        would_be_needed_to_close = round_opened[0] + square_opened[0] + 1
        if would_be_needed_to_close > n - (len(cur_res) + 1):
            return False
        square_opened[0] += 1
        stack.append(candidate)
        return True
    if candidate == ')':
        if not stack or stack[-1] != '(':
            return False
        stack.pop()
        round_opened[0] -= 1
        return True
    if candidate == ']':
        if not stack or stack[-1] != '[':
            return False
        stack.pop()
        square_opened[0] -= 1
        return True

while len(cur_res) < n:
    for candidate in w:
        if can_use(candidate):
            cur_res.append(candidate)
            break

print(''.join(cur_res))
