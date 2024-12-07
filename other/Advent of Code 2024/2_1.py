res = 0

while True:
    try:
        arr = [int(el) for el in input().split()]
        if len(arr) == 1:
            res += 1
            continue
        if arr == sorted(arr) or arr == sorted(arr, reverse=True):
            for i in range(1, len(arr)):
                if abs(arr[i] - arr[i-1]) == 0 or abs(arr[i] - arr[i-1]) > 3:
                    break
            else:
                res += 1
    except EOFError:
        break


print(res)