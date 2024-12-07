n, b = [int(el) for el in input().split()]

arr = [int(el) for el in input().split()]

cur_clients = 0
res = 0

for el in arr:
    cur_clients += el
    res += cur_clients
    cur_clients -= b 
    cur_clients = max(cur_clients, 0)

res += cur_clients

print(res)
