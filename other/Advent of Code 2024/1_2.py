import collections
list_1, list_2 = [], []
while True:
    try:
        num1, num2 = [int(el) for el in input().split()]
        list_1.append(num1)
        list_2.append(num2)
    except EOFError:
        break

c2 = collections.Counter(list_2)
res = 0

for el in list_1:
    res += el * c2[el]

print(res)
