res = 0

def is_safe(arr):
    if len(arr) < 2:
        return True
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == 0 or abs(arr[i] - arr[i-1]) > 3:
                return False
        return True
    return False

while True:
    try:
        arr = [int(el) for el in input().split()]
        for i in range(len(arr)):
            new_arr = arr[:i] + arr[i + 1:]
            if is_safe(new_arr):
                res += 1
                break
    except EOFError:
        break


print(res)