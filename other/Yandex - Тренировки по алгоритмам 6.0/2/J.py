from random import randint

n = int(input())

a_arr = [int(el) for el in input().split()]

m, k = [int(el) for el in input().split()]

x_arr = [int(el) for el in input().split()]

best_idx = 0

res = [0] * n
movements_between_same = 0

for i in range(1, n):
    if a_arr[i] == a_arr[i - 1]:
        if movements_between_same < k:
            res[i] = best_idx
            movements_between_same += 1
        else:
            while movements_between_same >= k:
                if a_arr[best_idx] == a_arr[best_idx + 1]:
                    movements_between_same -= 1
                best_idx += 1
            res[i] = best_idx
            movements_between_same += 1
        continue
    if a_arr[i] < a_arr[i - 1]:
        best_idx = i
        res[i] = best_idx
        movements_between_same = 0
        continue
    res[i] = best_idx
print(*[res[el - 1] + 1 for el in x_arr])


def my_func(n, a_arr, m, k, x_arr):
    best_idx = 0

    res = [0] * n
    movements_between_same = 0

    for i in range(1, n):
        if a_arr[i] == a_arr[i - 1]:
            if movements_between_same < k:
                res[i] = best_idx
                movements_between_same += 1
            else:
                while movements_between_same >= k:
                    if a_arr[best_idx] == a_arr[best_idx + 1]:
                        movements_between_same -= 1
                    best_idx += 1
                res[i] = best_idx
                movements_between_same += 1
            continue
        if a_arr[i] < a_arr[i - 1]:
            best_idx = i
            res[i] = best_idx
            movements_between_same = 0
            continue
        res[i] = best_idx
    return [res[el - 1] + 1 for el in x_arr]

def brute_force(n, a_arr, m, k, x_arr):
    res = []
    for el in x_arr:
        cur_idx = el - 1
        took_same = 0
        while cur_idx > 0:
            if a_arr[cur_idx] < a_arr[cur_idx - 1]:
                res.append(cur_idx)
                break
            if a_arr[cur_idx] == a_arr[cur_idx - 1]:
                if took_same == k:
                    res.append(cur_idx)
                    break
                took_same += 1
            cur_idx -= 1
        else:
            res.append(cur_idx)
            
    return [el + 1 for el in res]


def check():
    for _ in range(10000):
        n = randint(1, 25)
        a_arr = [randint(1, 100) for _ in range(n)]
        m, k = randint(1, 10), randint(0, 10)
        x_arr = [randint(1, n) for _ in range(m)]
        my_res = my_func(n, a_arr, m, k, x_arr)
        brute_res = brute_force(n, a_arr, m, k, x_arr)
        if my_res != brute_res:
            print(n)
            print(*a_arr)
            print(m, k)
            print(*x_arr)
            print(*my_res)
            print(*brute_res)
            break

#check()
