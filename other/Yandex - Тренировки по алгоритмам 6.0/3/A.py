s = input()
stack = []

for el in s:
    if el == '(' or el == '[' or el == '{':
        stack.append(el)
    if el == ')':
        if not stack or stack[-1] != '(':
            print('no')
            break
        stack.pop()
    if el == ']':
        if not stack or stack[-1] != '[':
            print('no')
            break
        stack.pop()
    if el == '}':
        if not stack or stack[-1] != '{':
            print('no')
            break
        stack.pop()
else:
    if stack:
        print('no')
    else:
        print('yes')

