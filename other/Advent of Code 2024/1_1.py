list_1, list_2 = [], []
while True:
    try:
        num1, num2 = [int(el) for el in input().split()]
        list_1.append(num1)
        list_2.append(num2)
    except EOFError:
        break

list_1.sort()
list_2.sort()
res = 0

for i in range(len(list_1)):
    res += abs(list_1[i] - list_2[i])

print(res)
